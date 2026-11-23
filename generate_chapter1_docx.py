import os
import re
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from lxml import etree
import latex2mathml.converter

# Initialize the official Microsoft MathML to OMML XSLT transformer
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
                if is_bold:
                    run.bold = True
                if is_italic:
                    run.italic = True

def create_chapter1_document():
    doc = docx.Document()
    
    # 1. Page Setup (UniSZA Guidelines: A4, Left 4.0cm, Right 2.5cm, Top 2.5cm, Bottom 2.5cm)
    for section in doc.sections:
        section.page_width = Inches(8.27)    # 21.0 cm
        section.page_height = Inches(11.69)  # 29.7 cm
        section.left_margin = Inches(1.575)   # 4.0 cm
        section.right_margin = Inches(0.984)  # 2.5 cm
        section.top_margin = Inches(0.984)    # 2.5 cm
        section.bottom_margin = Inches(0.984) # 2.5 cm
        section.header_distance = Inches(0.59) # 1.5 cm
        section.footer_distance = Inches(0.59) # 1.5 cm

    style_normal = doc.styles['Normal']
    style_normal.font.name = 'Times New Roman'
    style_normal.font.size = Pt(12)
    style_normal.font.color.rgb = RGBColor(0, 0, 0)
    
    md_path = 'Chapter 1 - INTRODUCTION/CHAPTER 1.md'
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        stripped = line.strip()
        
        # Empty lines or horizontal rules
        if not stripped or stripped == '---':
            i += 1
            continue
            
        # Chapter Title (# CHAPTER 1: INTRODUCTION)
        if stripped.startswith('# CHAPTER 1'):
            p0 = doc.add_paragraph()
            p0.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p0.paragraph_format.line_spacing = 1.0
            p0.paragraph_format.space_before = Pt(24)
            p0.paragraph_format.space_after = Pt(12)
            p0.paragraph_format.first_line_indent = Pt(0)
            r0 = p0.add_run('CHAPTER 1')
            r0.font.name = 'Times New Roman'
            r0.font.size = Pt(14)
            r0.bold = True
            
            p1 = doc.add_paragraph()
            p1.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p1.paragraph_format.line_spacing = 1.0
            p1.paragraph_format.space_before = Pt(0)
            p1.paragraph_format.space_after = Pt(36)
            p1.paragraph_format.first_line_indent = Pt(0)
            r1 = p1.add_run('INTRODUCTION')
            r1.font.name = 'Times New Roman'
            r1.font.size = Pt(14)
            r1.bold = True
            i += 1
            continue
            
        # Heading 1 (## 1.X TITLE)
        if stripped.startswith('## '):
            h_text = stripped[3:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(18)
            p.paragraph_format.space_after = Pt(12)
            p.paragraph_format.first_line_indent = Pt(0)
            r = p.add_run(h_text.upper())
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True
            i += 1
            continue
            
        # Heading 2 (### 1.X.X Title)
        if stripped.startswith('### '):
            h_text = stripped[4:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Pt(0)
            r = p.add_run(h_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True
            i += 1
            continue

        # Heading 3 (#### 1.X.X.X Title)
        if stripped.startswith('#### '):
            h_text = stripped[5:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.first_line_indent = Pt(0)
            r = p.add_run(h_text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.bold = True
            r.italic = True
            i += 1
            continue

        # Concluding disclaimer note
        if stripped.startswith('*(') and stripped.endswith(')*'):
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(24)
            p.paragraph_format.space_after = Pt(12)
            p.paragraph_format.first_line_indent = Pt(0)
            r = p.add_run(stripped[2:-2])
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            r.italic = True
            i += 1
            continue

        # Numbered items like i., ii., iii., iv.
        numbered_match = re.match(r'^([ivx]+\.|\d+\.)\s+(.*)$', stripped, re.IGNORECASE)
        if numbered_match:
            item_num = numbered_match.group(1)
            item_text = numbered_match.group(2)
            p = doc.add_paragraph()
            p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.left_indent = Inches(0.5)
            p.paragraph_format.first_line_indent = Inches(-0.25)
            
            run_num = p.add_run(item_num + '\t')
            run_num.font.name = 'Times New Roman'
            run_num.font.size = Pt(12)
            run_num.bold = True
            
            add_formatted_content_to_paragraph(p, item_text, base_font_size=12)
            i += 1
            continue

        # Regular Body Paragraph
        p = doc.add_paragraph()
        p.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.first_line_indent = Inches(0.5)  # 1.27 cm Standard Indent
        
        add_formatted_content_to_paragraph(p, stripped, base_font_size=12)
        i += 1

    output_path = 'Chapter 1 - INTRODUCTION/CHAPTER 1.docx'
    doc.save(output_path)
    print(f"Successfully generated formatted document: {output_path}")

if __name__ == '__main__':
    create_chapter1_document()
