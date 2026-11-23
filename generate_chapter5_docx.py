import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from lxml import etree
import latex2mathml.converter

# Initialize Microsoft MathML to OMML XSLT transformer
XSLT_PATH = r'C:\Program Files\Microsoft Office\root\Office16\MML2OMML.XSL'
xslt_doc = etree.parse(XSLT_PATH)
transform_omml = etree.XSLT(xslt_doc)

def latex_to_omml(latex_code):
    """Convert LaTeX formula to native Office OpenXML Math (<m:oMath>)"""
    try:
        clean_code = latex_code.strip()
        mathml = latex2mathml.converter.convert(clean_code)
        tree = etree.fromstring(mathml)
        omml = transform_omml(tree)
        return parse_xml(etree.tostring(omml.getroot()))
    except Exception as e:
        print(f"Warning: Failed to convert LaTeX '{latex_code}': {e}")
        return None

def set_cell_margins(cell, top=100, bottom=100, left=130, right=130):
    """Set cell padding in dxa (1 pt = 20 dxa)"""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    """Set background color of a cell"""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_table_borders(table, color="B0B0B0", sz="6", val="single"):
    """Set clean subtle borders for table"""
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'  <w:insideV w:val="none"/>'
            f'  <w:left w:val="none"/>'
            f'  <w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_formatted_content_to_paragraph(p, text, base_font_size=12, force_bold=False):
    """
    Parse a body paragraph containing text, markdown formatting (**bold**, *italic*),
    and inline math ($...$), appending runs and native OMML objects in exact sequence.
    """
    math_tokens = re.split(r'(\$[^$\n]+\$)', text)
    
    for m_tok in math_tokens:
        if not m_tok:
            continue
            
        if m_tok.startswith('$') and m_tok.endswith('$') and len(m_tok) > 2:
            latex = m_tok[1:-1].strip()
            omml_elm = latex_to_omml(latex)
            if omml_elm is not None:
                p._p.append(omml_elm)
            else:
                r = p.add_run(latex)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(base_font_size)
                r.italic = True
                if force_bold:
                    r.bold = True
        else:
            format_tokens = re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', m_tok)
            for f_tok in format_tokens:
                if not f_tok:
                    continue
                is_bold = force_bold
                is_italic = None
                clean_text = f_tok
                
                if f_tok.startswith('**') and f_tok.endswith('**'):
                    is_bold = True
                    clean_text = f_tok[2:-2]
                elif f_tok.startswith('*') and f_tok.endswith('*'):
                    is_italic = True
                    clean_text = f_tok[1:-1]
                    
                run = p.add_run(clean_text)
                run.font.name = 'Times New Roman'
                run.font.size = Pt(base_font_size)
                run.font.color.rgb = RGBColor(0, 0, 0)
                if is_bold:
                    run.bold = True
                if is_italic:
                    run.italic = True

def add_display_equation(doc, raw_eq):
    """
    Render a display equation ($$ ... $$) into the document as native Word Office Math.
    If an equation tag like \tag{5.1} is present, uses a borderless table layout to keep
    the formula centered and the tag flush right.
    """
    tag = ""
    tag_match = re.search(r'\\tag\{([^}]+)\}', raw_eq)
    if tag_match:
        tag = f"({tag_match.group(1).strip()})"
        raw_eq = raw_eq[:tag_match.start()] + raw_eq[tag_match.end():]
        raw_eq = raw_eq.strip()
        
    omml_elm = latex_to_omml(raw_eq)
    if omml_elm is None:
        print(f"Error rendering equation: {raw_eq}")
        return

    if tag:
        tbl = doc.add_table(rows=1, cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl.autofit = False
        tbl.columns[0].width = Inches(5.0)
        tbl.columns[1].width = Inches(0.75)
        
        tblPr = tbl._element.xpath('w:tblPr')[0]
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'  <w:top w:val="none"/><w:left w:val="none"/><w:bottom w:val="none"/>'
            f'  <w:right w:val="none"/><w:insideH w:val="none"/><w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)
        
        c0 = tbl.cell(0, 0)
        c0.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(c0, top=60, bottom=60, left=0, right=0)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p0.paragraph_format.line_spacing = 1.0
        p0.paragraph_format.space_before = Pt(4)
        p0.paragraph_format.space_after = Pt(4)
        p0.paragraph_format.first_line_indent = Pt(0)
        p0._p.append(omml_elm)
        
        c1 = tbl.cell(0, 1)
        c1.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_margins(c1, top=60, bottom=60, left=0, right=0)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        p1.paragraph_format.line_spacing = 1.0
        p1.paragraph_format.space_before = Pt(4)
        p1.paragraph_format.space_after = Pt(4)
        p1.paragraph_format.first_line_indent = Pt(0)
        r_tag = p1.add_run(tag)
        r_tag.font.name = 'Times New Roman'
        r_tag.font.size = Pt(12)
    else:
        p = doc.add_paragraph()
        p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.first_line_indent = Pt(0)
        p._p.append(omml_elm)

def render_markdown_table(doc, table_lines):
    """Parse Markdown table and output a beautifully formatted Word table"""
    rows_data = []
    for line in table_lines:
        line_clean = line.strip()
        if not line_clean.startswith('|'):
            continue
        cells = [c.strip() for c in line_clean.split('|')[1:-1]]
        if all(re.match(r'^:?-+:?$', c) for c in cells):
            continue
        rows_data.append(cells)
        
    if not rows_data:
        return
        
    num_rows = len(rows_data)
    num_cols = len(rows_data[0])
    
    # Adaptive font size based on column count
    if num_cols >= 7:
        table_font_size = 9.0
        cell_pad_lr = 100
    elif num_cols >= 5:
        table_font_size = 9.5
        cell_pad_lr = 120
    else:
        table_font_size = 10.0
        cell_pad_lr = 150

    table = doc.add_table(rows=num_rows, cols=num_cols)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table, color="B0B0B0", sz="6", val="single")
    
    for r_idx, row in enumerate(rows_data):
        is_header = (r_idx == 0)
        table_row = table.rows[r_idx]
        
        trPr = table_row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
        if is_header:
            trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
            
        for c_idx, cell_value in enumerate(row):
            if c_idx >= num_cols:
                break
            cell = table_row.cells[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            set_cell_margins(cell, top=100, bottom=100, left=cell_pad_lr, right=cell_pad_lr)
            
            if is_header:
                set_cell_shading(cell, "F2F4F7")
                
            p = cell.paragraphs[0]
            # Center header or short numeric/code cells, left-align text
            is_numeric = bool(re.match(r'^-?\d+(\.\d+)?%?$', cell_value) or cell_value in ['-', 'PE3', 'GEV', 'GLO', 'GNO', 'GPA', 'K4D'])
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER if (is_header or is_numeric) else WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.first_line_indent = Pt(0)
            
            add_formatted_content_to_paragraph(p, cell_value, base_font_size=table_font_size, force_bold=is_header)
                
    p_spacer = doc.add_paragraph()
    p_spacer.paragraph_format.line_spacing = 1.0
    p_spacer.paragraph_format.space_before = Pt(0)
    p_spacer.paragraph_format.space_after = Pt(6)
    p_spacer.paragraph_format.first_line_indent = Pt(0)

def create_chapter5_document():
    md_file_path = 'Chapter 5 - RESULTS AND DISCUSSION/CHAPTER 5.md'
    out_docx_path = 'Chapter 5 - RESULTS AND DISCUSSION/CHAPTER 5.docx'
    doc_dir = os.path.dirname(os.path.abspath(md_file_path))

    with open(md_file_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    doc = docx.Document()

    # Set UniSZA standard margins (Left: 1.5 in / 3.8 cm; Right, Top, Bottom: 1.0 in / 2.5 cm)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.5)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.27)
        section.page_height = Inches(11.69)

    # Base Normal Style Configuration
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)

    lines = md_text.split('\n')
    i = 0
    prev_was_heading_or_block = True

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped or stripped == '---':
            i += 1
            continue

        # Chapter Title (# CHAPTER 5: RESULTS AND DISCUSSION)
        if stripped.startswith('# CHAPTER 5'):
            p1 = doc.add_paragraph()
            p1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p1.paragraph_format.line_spacing = 1.5
            p1.paragraph_format.space_before = Pt(24)
            p1.paragraph_format.space_after = Pt(6)
            p1.paragraph_format.first_line_indent = Pt(0)
            r1 = p1.add_run("CHAPTER 5")
            r1.font.name = 'Times New Roman'
            r1.font.size = Pt(14)
            r1.bold = True
            
            p2 = doc.add_paragraph()
            p2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p2.paragraph_format.line_spacing = 1.5
            p2.paragraph_format.space_before = Pt(0)
            p2.paragraph_format.space_after = Pt(24)
            p2.paragraph_format.first_line_indent = Pt(0)
            r2 = p2.add_run("RESULTS AND DISCUSSION")
            r2.font.name = 'Times New Roman'
            r2.font.size = Pt(14)
            r2.bold = True
            prev_was_heading_or_block = True
            i += 1
            continue

        # Heading 1 (## 5.X)
        if stripped.startswith('## '):
            heading_text = stripped[3:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Pt(0)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(heading_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(13)
            r.bold = True
            prev_was_heading_or_block = True
            i += 1
            continue

        # Heading 2 (### 5.X.X)
        if stripped.startswith('### '):
            heading_text = stripped[4:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.first_line_indent = Pt(0)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(heading_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True
            prev_was_heading_or_block = True
            i += 1
            continue

        # Heading 3 (#### 5.X.X.X)
        if stripped.startswith('#### '):
            heading_text = stripped[5:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.first_line_indent = Pt(0)
            p.paragraph_format.keep_with_next = True
            r = p.add_run(heading_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True
            r.italic = True
            prev_was_heading_or_block = True
            i += 1
            continue

        # Table Captions (Placed ABOVE table, Left-aligned, bold title)
        if stripped.startswith('**Table '):
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.first_line_indent = Pt(0)
            p.paragraph_format.keep_with_next = True
            add_formatted_content_to_paragraph(p, stripped, base_font_size=11, force_bold=False)
            prev_was_heading_or_block = True
            i += 1
            continue

        # Markdown Table Detection
        if stripped.startswith('|'):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            render_markdown_table(doc, table_lines)
            prev_was_heading_or_block = True
            continue

        # Table Note (*Note: ...*)
        if stripped.startswith('*Note:') or stripped.startswith('*Note :'):
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(10)
            p.paragraph_format.first_line_indent = Pt(0)
            add_formatted_content_to_paragraph(p, stripped, base_font_size=10, force_bold=False)
            prev_was_heading_or_block = True
            i += 1
            continue

        # Figure Images: ![caption](path)
        img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
        if img_match:
            img_caption_alt = img_match.group(1).strip()
            img_path = img_match.group(2).strip()
            img_full_path = os.path.join(doc_dir, img_path)
            if not os.path.exists(img_full_path):
                img_full_path = img_path
                
            if os.path.exists(img_full_path):
                p_img = doc.add_paragraph()
                p_img.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                p_img.paragraph_format.line_spacing = 1.0
                p_img.paragraph_format.space_before = Pt(14)
                p_img.paragraph_format.space_after = Pt(4)
                p_img.paragraph_format.first_line_indent = Pt(0)
                run_img = p_img.add_run()
                run_img.add_picture(img_full_path, width=Inches(5.75))
            else:
                print(f"Warning: Image file not found: {img_full_path}")
            prev_was_heading_or_block = True
            i += 1
            continue

        # Figure Captions (Placed BELOW figure, Centered/Justified)
        if stripped.startswith('**Figure '):
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(14)
            p.paragraph_format.first_line_indent = Pt(0)
            add_formatted_content_to_paragraph(p, stripped, base_font_size=11, force_bold=False)
            prev_was_heading_or_block = True
            i += 1
            continue

        # Display Equation ($$ ... $$)
        if stripped.startswith('$$'):
            eq_lines = []
            if stripped.endswith('$$') and len(stripped) > 4:
                raw_eq = stripped[2:-2].strip()
                add_display_equation(doc, raw_eq)
                i += 1
                prev_was_heading_or_block = True
                continue
            else:
                i += 1
                while i < len(lines) and not lines[i].strip().endswith('$$'):
                    eq_lines.append(lines[i].strip())
                    i += 1
                if i < len(lines):
                    eq_tail = lines[i].strip()[:-2].strip()
                    if eq_tail:
                        eq_lines.append(eq_tail)
                    i += 1
                raw_eq = " ".join(eq_lines)
                add_display_equation(doc, raw_eq)
                prev_was_heading_or_block = True
                continue

        # Regular Body Paragraph
        p = doc.add_paragraph()
        p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        
        # Apply standard 0.5-inch paragraph indentation unless immediately following a heading or block element
        if prev_was_heading_or_block:
            p.paragraph_format.first_line_indent = Pt(0)
        else:
            p.paragraph_format.first_line_indent = Inches(0.5)
            
        add_formatted_content_to_paragraph(p, stripped, base_font_size=12, force_bold=False)
        prev_was_heading_or_block = False
        i += 1

    doc.save(out_docx_path)
    print(f"Successfully generated formatted document: {out_docx_path}")

if __name__ == '__main__':
    create_chapter5_document()
