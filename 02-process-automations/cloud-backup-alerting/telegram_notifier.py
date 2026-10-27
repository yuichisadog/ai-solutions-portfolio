"""
Módulo de Notificação Operacional via Telegram Bot
Autor: Juan Santos Oliveira
"""

import os

def send_ops_notification(message: str) -> bool:
    """
    Envia alertas operacionais e sumários diários para o grupo de governança.
    Usa variáveis de ambiente para preservar segredos de API.
    """
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN", "MOCK_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID", "MOCK_CHAT_ID")
    
    if bot_token == "MOCK_TOKEN":
        print(f"[TELEGRAM SIMULADO]:\n{message}")
        return True
        
    import requests
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message, "parse_mode": "Markdown"}
    
    try:
        res = requests.post(url, json=payload, timeout=10)
        return res.status_code == 200
    except Exception as e:
        print(f"Erro ao disparar alerta Telegram: {e}")
        return False
