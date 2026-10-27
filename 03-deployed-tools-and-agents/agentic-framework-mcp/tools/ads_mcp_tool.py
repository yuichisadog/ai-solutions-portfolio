"""
MCP Tool: Consultor Analítico de Mídia Paga
Autor: Juan Santos Oliveira
"""

from typing import Dict, Any

def query_campaign_metrics(account_id: str, days: int = 7) -> Dict[str, Any]:
    """
    Simula a consulta tipada via MCP às APIs de Meta e Google Ads.
    """
    return {
        "account_id": account_id,
        "window_days": days,
        "metrics": {
            "spend_brl": 4850.20,
            "impressions": 142000,
            "clicks": 3890,
            "ctr_percent": 2.74,
            "cpc_average": 1.24,
            "conversions": 114,
            "cpa_actual": 42.54,
            "roas": 3.45
        },
        "quality_gate": {
            "cpa_within_target": True,
            "frequency": 2.1
        }
    }
