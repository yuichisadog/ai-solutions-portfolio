"""
Camada de Memória Semântica e Persistência de Contexto
Autor: Juan Santos Oliveira
"""

import json
from pathlib import Path
from typing import Dict, Any, List

class AgentMemoryStore:
    def __init__(self, storage_path: str = "memory_store.json"):
        self.storage_file = Path(storage_path)
        if not self.storage_file.exists():
            self.storage_file.write_text(json.dumps({"strategic_learnings": []}), encoding="utf-8")

    def record_learning(self, category: str, rule: str, evidence: str):
        data = json.loads(self.storage_file.read_text(encoding="utf-8"))
        data["strategic_learnings"].append({
            "category": category,
            "rule": rule,
            "evidence": evidence
        })
        self.storage_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def retrieve_rules(self, category: str) -> List[Dict[str, Any]]:
        data = json.loads(self.storage_file.read_text(encoding="utf-8"))
        return [item for item in data.get("strategic_learnings", []) if item["category"] == category]

if __name__ == "__main__":
    mem = AgentMemoryStore()
    mem.record_learning(
        category="CRIATIVOS",
        rule="Vídeos verticais com ganchos nos primeiros 2s têm CTR 45% superior a estáticos.",
        evidence="Validação com R$ 25k em e-commerce (Lojas Dália)."
    )
    print("Memória atualizada e gravada em disco.")
