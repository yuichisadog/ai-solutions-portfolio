"""
Orquestrador Multiagente com Protocolo MCP
Autor: Juan Santos Oliveira
"""

import json
from typing import Dict, Any, List
from tools.ads_mcp_tool import query_campaign_metrics
from tools.competitor_browser_tool import inspect_competitor_creatives

class AgentOrchestrator:
    def __init__(self):
        self.registered_tools = {
            "query_campaign_metrics": query_campaign_metrics,
            "inspect_competitor_creatives": inspect_competitor_creatives
        }

    def execute_agent_task(self, agent_role: str, task_description: str, tool_name: str, tool_args: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executa uma ação delegada a um subagente especializado através de MCP.
        """
        if tool_name not in self.registered_tools:
            return {"error": f"Ferramenta '{tool_name}' não autorizada no protocolo."}

        print(f"[{agent_role.upper()}] Iniciando tarefa: {task_description}")
        tool_func = self.registered_tools[tool_name]
        result = tool_func(**tool_args)
        
        return {
            "agent": agent_role,
            "status": "COMPLETO",
            "execution_payload": result
        }

if __name__ == "__main__":
    orchestrator = AgentOrchestrator()
    # Teste de execução de ferramenta de auditoria de mídia
    response = orchestrator.execute_agent_task(
        agent_role="Auditor de Performance",
        task_description="Consultar CPA dos últimos 7 dias",
        tool_name="query_campaign_metrics",
        tool_args={"account_id": "act_55210948", "days": 7}
    )
    print(json.dumps(response, indent=2))
