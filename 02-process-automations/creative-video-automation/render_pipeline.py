"""
Pipeline de Renderização de Variações Criativas em Lote
Autor: Juan Santos Oliveira
Descrição: Injeta dados dinâmicos de ofertas em templates HTML/CSS para
produzir criativos em escala para campanhas de Meta Ads e TikTok.
"""

import json
from pathlib import Path

def generate_creative_variant(template_path: str, output_path: str, data: dict):
    html_content = Path(template_path).read_text(encoding="utf-8")
    
    # Substituição semântica de marcadores dinâmicos
    rendered = html_content.replace("Oportunidade B2B", data.get("badge", "DESTAQUE"))
    rendered = rendered.replace(
        "Expanda sua Operação no <span>Melhor Ponto Comercial</span>",
        data.get("headline", "Confira a Oferta")
    )
    rendered = rendered.replace(
        "Fluxo qualificado de mais de 450 mil consumidores/mês",
        data.get("prop1", "Vantagem 1")
    )
    
    Path(output_path).write_text(rendered, encoding="utf-8")
    print(f"Variação criada: {output_path}")

if __name__ == "__main__":
    variants = [
        {
            "badge": "Franquias de Alimentação",
            "headline": "Abra sua Loja em uma <span>Praça de Alta Rentabilidade</span>",
            "prop1": "Consumo consolidado e estrutura pronta para instalação"
        },
        {
            "badge": "Varejo de Moda",
            "headline": "Seu Ponto de Venda no <span>Coração da Zona Sul</span>",
            "prop1": "Vitrine para mais de 15 mil visitantes diários"
        }
    ]
    
    base_template = Path(__file__).parent / "template_video.html"
    for i, var in enumerate(variants):
        out = Path(__file__).parent / f"variant_{i+1}.html"
        generate_creative_variant(str(base_template), str(out), var)
