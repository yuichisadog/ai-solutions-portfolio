"""
Validador Automatizado E2E de Tags e Conversões (Selenium + Headless Chrome)
Autor: Juan Santos Oliveira
Descrição: Carrega páginas de destino de clientes em modo headless, simula interações
críticas (clique de WhatsApp, envio de lead) e audita o disparo de eventos no dataLayer.
"""

from typing import Dict, Any, List

def mock_audit_datalayer(events: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Função representativa da rotina de auditoria que inspeciona o objeto window.dataLayer
    extraído do navegador via driver.execute_script('return window.dataLayer;').
    """
    found_events = [e.get("event") for e in events if "event" in e]
    has_pageview = "page_view" in found_events or "gtm.js" in found_events
    has_lead_submission = "generate_lead" in found_events or "contact_click" in found_events

    status = "APROVADO" if (has_pageview and has_lead_submission) else "REPROVADO"
    return {
        "status": status,
        "events_captured": found_events,
        "is_safe_to_publish": status == "APROVADO",
        "diagnostic": "Fluxo de conversão íntegro e validado." if status == "APROVADO" else "Evento crítico de conversão ausente."
    }

if __name__ == "__main__":
    sample_datalayer = [
        {"event": "gtm.js", "gtm.start": 1729000000},
        {"event": "page_view", "page_path": "/contato"},
        {"event": "generate_lead", "lead_type": "B2B_FRANQUIA", "expected_value": 350.00}
    ]
    resultado = mock_audit_datalayer(sample_datalayer)
    print(f"Status da Validação GTM: {resultado['status']}")
    print(f"Eventos Identificados: {resultado['events_captured']}")
    print(f"Seguro para Deploy: {resultado['is_safe_to_publish']}")
