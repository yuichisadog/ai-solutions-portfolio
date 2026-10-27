"""
Engine de Auditoria e Diagnóstico de Contas de Mídia (RAIO X)
Autor: Juan Santos Oliveira
Descrição: Executa auditorias em lote em contas de Meta Ads e Google Ads,
calculando ritmo de gasto (pacing), saúde financeira e runway de fundos.
"""

from typing import Dict, Any, List
from rules_engine import evaluate_account_pacing, evaluate_runway_risk

class AccountAuditor:
    def __init__(self, accounts_data: List[Dict[str, Any]]):
        self.accounts = accounts_data

    def run_full_audit(self) -> List[Dict[str, Any]]:
        audit_results = []
        for acc in self.accounts:
            pacing_evaluation = evaluate_account_pacing(
                spend_month=acc["spend_month_to_date"],
                budget_planned=acc["monthly_budget_target"],
                day_of_month=acc["current_day_of_month"],
                total_days_in_month=acc["total_days_in_month"]
            )
            
            runway_evaluation = evaluate_runway_risk(
                balance_available=acc["balance_available"],
                daily_spend_rate=acc["average_daily_spend"]
            )
            
            audit_results.append({
                "account_name": acc["account_name"],
                "channel": acc["channel"],
                "pacing": pacing_evaluation,
                "financial_runway": runway_evaluation,
                "requires_urgent_action": runway_evaluation["is_urgent"] or pacing_evaluation["is_critical"]
            })
        return audit_results

if __name__ == "__main__":
    mock_accounts = [
        {
            "account_name": "Operacao B2B Petroquimica",
            "channel": "Meta + Google",
            "spend_month_to_date": 8200.00,
            "monthly_budget_target": 12000.00,
            "current_day_of_month": 27,
            "total_days_in_month": 31,
            "balance_available": 3800.00,
            "average_daily_spend": 385.00
        },
        {
            "account_name": "Shopping Center Regional",
            "channel": "Meta Ads",
            "spend_month_to_date": 9200.00,
            "monthly_budget_target": 9750.00,
            "current_day_of_month": 27,
            "total_days_in_month": 31,
            "balance_available": 550.00,
            "average_daily_spend": 315.00
        }
    ]
    
    auditor = AccountAuditor(mock_accounts)
    relatorio = auditor.run_full_audit()
    for item in relatorio:
        print(f"\n--- Conta: {item['account_name']} ({item['channel']}) ---")
        print(f"Pacing: {item['pacing']['status']} (Índice: {item['pacing']['pacing_index']:.2f})")
        print(f"Runway: {item['financial_runway']['runway_days']} dias restantes.")
        print(f"Alerta: {item['financial_runway']['alert_level']} -> {item['financial_runway']['action_required']}")
