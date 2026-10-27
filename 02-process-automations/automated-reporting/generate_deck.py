"""
Gerador Automatizado de Relatórios de Mídia em PPTX
Autor: Juan Santos Oliveira
Descrição: Converte dados consolidados de tráfego pago em apresentações executivas
em PowerPoint seguindo diretrizes visuais profissionais de forma determinística.
"""

import sys
import json
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Paleta de Cores Institucional
COLOR_PRIMARY = RGBColor(15, 23, 42)     # Slate 900 (Fundo escuro / Títulos)
COLOR_ACCENT = RGBColor(14, 165, 233)    # Sky 500 (Destaque)
COLOR_TEXT_MUTED = RGBColor(100, 116, 139) # Slate 500
COLOR_BG_CARD = RGBColor(241, 245, 249)  # Slate 100
COLOR_CARD_BORDER = RGBColor(203, 213, 225) # Slate 300
COLOR_GREEN = RGBColor(34, 197, 94)      # Emerald 500

def create_report_deck(report_data: dict, output_path: str = "relatorio_executivo.pptx") -> str:
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]
    
    # --- SLIDE 1: Capa Executiva ---
    slide1 = prs.slides.add_slide(blank_layout)
    
    # Fundo escuro na capa
    bg = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_PRIMARY
    bg.line.fill.background()
    
    # Título
    tx_box = slide1.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(11.0), Inches(2.0))
    tf = tx_box.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = "Relatório Executivo de Performance"
    p.font.size = Pt(40)
    p.font.bold = True
    p.font.color.rgb = RGBColor(255, 255, 255)
    
    p2 = tf.add_paragraph()
    p2.text = f"{report_data.get('account_name', 'Cliente')} | Ciclo: {report_data.get('period', 'Mensal')}"
    p2.font.size = Pt(22)
    p2.font.color.rgb = COLOR_ACCENT
    p2.space_before = Pt(12)
    
    p3 = tf.add_paragraph()
    p3.text = f"Governança Operacional e Inteligência de Tráfego Pago | Gestão: Juan Santos Oliveira"
    p3.font.size = Pt(14)
    p3.font.color.rgb = COLOR_TEXT_MUTED
    p3.space_before = Pt(28)
    
    # --- SLIDE 2: Visão Geral de KPIs ---
    slide2 = prs.slides.add_slide(blank_layout)
    
    # Cabeçalho
    header_box = slide2.shapes.add_textbox(Inches(1.0), Inches(0.8), Inches(11.3), Inches(1.0))
    htf = header_box.text_frame
    hp = htf.paragraphs[0]
    hp.text = "Visão Geral de Performance & KPIs"
    hp.font.size = Pt(28)
    hp.font.bold = True
    hp.font.color.rgb = COLOR_PRIMARY
    
    # Cards de Métricas
    kpis = [
        {"label": "Investimento Total", "val": f"R$ {report_data.get('spend_total', 0):,.2f}", "detail": "Ritmo de pacing alinhado"},
        {"label": "Volume de Conversões", "val": str(report_data.get('conversions_count', 0)), "detail": "Leads e vendas validados"},
        {"label": "CPA Médio Real", "val": f"R$ {report_data.get('cpa_actual', 0):.2f}", "detail": f"Meta: R$ {report_data.get('cpa_target', 0):.2f}"},
        {"label": "ROAS Consolidado", "val": f"{report_data.get('roas_blended', 0):.2f}x", "detail": "Retorno direto mensurado"}
    ]
    
    card_w = Inches(2.6)
    card_h = Inches(3.2)
    card_top = Inches(2.2)
    spacing = Inches(0.3)
    start_left = Inches(1.0)
    
    for i, kpi in enumerate(kpis):
        left = start_left + (i * (card_w + spacing))
        shape = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, card_top, card_w, card_h)
        shape.fill.solid()
        shape.fill.fore_color.rgb = COLOR_BG_CARD
        shape.line.color.rgb = COLOR_CARD_BORDER
        shape.line.width = Pt(1)
        
        stf = shape.text_frame
        stf.word_wrap = True
        
        sp1 = stf.paragraphs[0]
        sp1.text = kpi["label"]
        sp1.font.size = Pt(14)
        sp1.font.color.rgb = COLOR_TEXT_MUTED
        sp1.alignment = PP_ALIGN.CENTER
        
        sp2 = stf.add_paragraph()
        sp2.text = kpi["val"]
        sp2.font.size = Pt(24)
        sp2.font.bold = True
        sp2.font.color.rgb = COLOR_PRIMARY
        sp2.alignment = PP_ALIGN.CENTER
        sp2.space_before = Pt(20)
        
        sp3 = stf.add_paragraph()
        sp3.text = kpi["detail"]
        sp3.font.size = Pt(11)
        sp3.font.color.rgb = COLOR_GREEN
        sp3.alignment = PP_ALIGN.CENTER
        sp3.space_before = Pt(16)
        
    prs.save(output_path)
    return str(Path(output_path).resolve())

if __name__ == "__main__":
    sample_data = {
        "account_name": "Operação E-Commerce & Varejo",
        "period": "Outubro 2026",
        "spend_total": 24800.00,
        "conversions_count": 482,
        "cpa_actual": 51.45,
        "cpa_target": 65.00,
        "roas_blended": 4.88
    }
    output = create_report_deck(sample_data)
    print(f"Relatório gerado com sucesso em: {output}")
