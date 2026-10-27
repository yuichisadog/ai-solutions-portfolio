"""
Testes Automatizados para Avaliação de Prompts e Schemas Pydantic
Autor: Juan Santos Oliveira
"""

import json
import pytest
from pydantic import BaseModel, Field, ValidationError

class MarketingAuditReport(BaseModel):
    account_id: str
    account_name: str
    pacing_rate_percentage: float = Field(ge=0, le=300)
    runway_days_remaining: float = Field(ge=0)
    requires_budget_alert: bool
    recommended_action: str

def test_valid_llm_structured_output():
    payload = {
        "account_id": "act_82910481",
        "account_name": "Operacao Varejo Sul",
        "pacing_rate_percentage": 98.4,
        "runway_days_remaining": 6.2,
        "requires_budget_alert": False,
        "recommended_action": "MANTER_RITMO"
    }
    report = MarketingAuditReport(**payload)
    assert report.account_id == "act_82910481"
    assert report.requires_budget_alert is False
    assert report.runway_days_remaining == 6.2

def test_rejection_of_hallucinated_negative_runway():
    invalid_payload = {
        "account_id": "act_82910481",
        "account_name": "Operacao Varejo Sul",
        "pacing_rate_percentage": 105.0,
        "runway_days_remaining": -2.5,  # Impossível fisicamente
        "requires_budget_alert": True,
        "recommended_action": "SOLICITAR_BOLETO"
    }
    with pytest.raises(ValidationError):
        MarketingAuditReport(**invalid_payload)

def test_rejection_of_missing_critical_keys():
    incomplete_payload = {
        "account_name": "Operacao Varejo Sul",
        "pacing_rate_percentage": 105.0
    }
    with pytest.raises(ValidationError):
        MarketingAuditReport(**incomplete_payload)
