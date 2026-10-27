"""
Motor de Regras de Negócio e Governança Financeira de Tráfego Pago
Autor: Juan Santos Oliveira
"""

from typing import Dict, Any

def evaluate_account_pacing(spend_month: float, budget_planned: float, day_of_month: int, total_days_in_month: int) -> Dict[str, Any]:
    expected_ratio = day_of_month / total_days_in_month
    actual_ratio = spend_month / budget_planned if budget_planned > 0 else 0
    pacing_index = actual_ratio / expected_ratio if expected_ratio > 0 else 1.0

    if pacing_index > 1.15:
        status = "SOBREGASO"
        is_critical = True
    elif pacing_index < 0.85:
        status = "SUBGASTO"
        is_critical = True
    else:
        status = "ALINHADO"
        is_critical = False

    return {
        "status": status,
        "pacing_index": round(pacing_index, 3),
        "actual_spend": spend_month,
        "budget_planned": budget_planned,
        "is_critical": is_critical
    }

def evaluate_runway_risk(balance_available: float, daily_spend_rate: float) -> Dict[str, Any]:
    """
    Calcula os dias restantes de veiculação antes do esgotamento de fundos.
    Regra operacional:
    - Runway < 3 dias: URGENTE (risco imediato de pausa)
    - Runway 3 a 7 dias: PREVENTIVO (solicitar boleto ou PI imediatamente)
    - Runway > 7 dias: SEGURO
    """
    runway_days = round(balance_available / daily_spend_rate, 1) if daily_spend_rate > 0 else 999.0

    if runway_days < 3.0:
        alert = "CRITICO_URGENTE"
        action = "Solicitar boleto/PI emergencial hoje. Risco de corte em 48h."
        is_urgent = True
    elif runway_days <= 7.0:
        alert = "ALERTA_PREVENTIVO"
        action = "Disparar pedido de faturamento para financeiro (ponto de pedido regular)."
        is_urgent = False
    else:
        alert = "OPERACAO_NORMAL"
        action = "Fundos suficientes para o ritmo atual de veiculação."
        is_urgent = False

    return {
        "runway_days": runway_days,
        "alert_level": alert,
        "action_required": action,
        "is_urgent": is_urgent
    }
