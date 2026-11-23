import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

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
    """Parse text and append runs with bold/italic styling"""
    format_tokens = re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', text)
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
        cell_pad_lr = 140

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
            is_numeric = bool(re.match(r'^-?\d+(\.\d+)?%?$', cell_value) or cell_value in ['-', 'loc', 'scale'])
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

def create_appendix_document():
    md_file_path = 'Appendix/APPENDIX.md'
    out_docx_path = 'Appendix/APPENDIX.docx'

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

        # Appendix Document Main Title
        if stripped.startswith('# APPENDIX'):
            p1 = doc.add_paragraph()
            p1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p1.paragraph_format.line_spacing = 1.5
            p1.paragraph_format.space_before = Pt(24)
            p1.paragraph_format.space_after = Pt(6)
            p1.paragraph_format.first_line_indent = Pt(0)
            r1 = p1.add_run("APPENDIX")
            r1.font.name = 'Times New Roman'
            r1.font.size = Pt(14)
            r1.bold = True
            
            p2 = doc.add_paragraph()
            p2.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p2.paragraph_format.line_spacing = 1.5
            p2.paragraph_format.space_before = Pt(0)
            p2.paragraph_format.space_after = Pt(24)
            p2.paragraph_format.first_line_indent = Pt(0)
            r2 = p2.add_run("SUPPLEMENTARY DATA AND EXTENDED RESULTS")
            r2.font.name = 'Times New Roman'
            r2.font.size = Pt(14)
            r2.bold = True
            prev_was_heading_or_block = True
            i += 1
            continue

        # Major Appendix Sections (## Appendix A, ## Appendix B)
        if stripped.startswith('## Appendix'):
            heading_text = stripped[3:].strip()
            # Add page break before Appendix B
            if 'Appendix B' in heading_text:
                doc.add_page_break()
                
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

        # Subsections (### A.1, ### A.2)
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

        # Regular Body Paragraph
        p = doc.add_paragraph()
        p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        
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
    create_appendix_document()
