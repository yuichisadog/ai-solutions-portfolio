"""
Experimento de Avaliação de Temperatura e Top-P em LLMs
Autor: Juan Santos Oliveira
Objetivo: Medir a variabilidade sintática, taxa de parse de JSON e aderência a schemas
em diferentes configurações de amostragem de LLMs para extração de dados analíticos.
"""

import json
import statistics
from typing import Dict, Any, List
from pydantic import BaseModel, Field, ValidationError

class MockMarketingKPI(BaseModel):
    account_name: str
    spend_total: float = Field(ge=0)
    conversions_count: int = Field(ge=0)
    cpa_actual: float = Field(ge=0)
    status_alignment: str

def simulate_llm_response(temperature: float, iteration: int) -> str:
    """
    Simula o comportamento estocástico de um LLM sob diferentes temperaturas
    para uma tarefa de extração de dados tabulares de mídia.
    """
    if temperature == 0.0:
        # Determinismo puro: 100% de consistência sintática
        return json.dumps({
            "account_name": "E-Commerce Moda & Casa",
            "spend_total": 24800.50,
            "conversions_count": 482,
            "cpa_actual": 51.45,
            "status_alignment": "DENTRO_DA_META"
        })
    elif temperature <= 0.5:
        # Baixa variação: pequenas variações de arredondamento mas estrutura preservada
        jitter = (iteration % 3) * 0.01
        return json.dumps({
            "account_name": "E-Commerce Moda & Casa",
            "spend_total": round(24800.50 + jitter, 2),
            "conversions_count": 482,
            "cpa_actual": round(51.45 + jitter, 2),
            "status_alignment": "DENTRO_DA_META"
        })
    else:
        # Alta temperatura (>= 0.8): risco de markdown residual e quebra de tipos
        if iteration % 4 == 0:
            return '```json\n{"account_name": "E-Commerce Moda & Casa", "spend_total": "R$ 24.800", "conversions_count": 482, "cpa_actual": 51.45, "status_alignment": "EXCELENTE"}\n```'
        return json.dumps({
            "account_name": "E-Commerce Moda & Casa",
            "spend_total": 24800.50,
            "conversions_count": 482,
            "cpa_actual": 51.45,
            "status_alignment": "DENTRO_DA_META"
        })

def run_experiment(temperatures: List[float], trials: int = 50) -> Dict[str, Any]:
    results = {}
    
    for temp in temperatures:
        valid_json_count = 0
        pydantic_valid_count = 0
        cpa_values = []
        
        for i in range(trials):
            raw_output = simulate_llm_response(temp, i)
            # Limpeza básica de markdown caso ocorra
            cleaned = raw_output.replace("```json", "").replace("```", "").strip()
            
            try:
                data = json.loads(cleaned)
                valid_json_count += 1
                validated = MockMarketingKPI(**data)
                pydantic_valid_count += 1
                cpa_values.append(validated.cpa_actual)
            except (json.JSONDecodeError, ValidationError):
                pass
                
        std_dev = statistics.stdev(cpa_values) if len(cpa_values) > 1 else 0.0
        results[f"temp_{temp}"] = {
            "json_success_rate": f"{(valid_json_count / trials) * 100:.1f}%",
            "pydantic_valid_rate": f"{(pydantic_valid_count / trials) * 100:.1f}%",
            "metric_variance_stdev": round(std_dev, 4)
        }
        
    return results

if __name__ == "__main__":
    test_temps = [0.0, 0.3, 0.7, 1.0]
    benchmarks = run_experiment(test_temps, trials=100)
    print("=== RESULTADOS DO BENCHMARK DE TEMPERATURA ===")
    print(json.dumps(benchmarks, indent=2))
