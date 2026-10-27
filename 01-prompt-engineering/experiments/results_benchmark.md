# Relatório de Benchmarking: Engenharia de Prompts e Aderência de LLMs

## Objetivo do Experimento
Avaliar quantitativamente o ganho de confiabilidade em pipelines de IA analítica ao migrar de instruções em texto livre para uma arquitetura baseada em:
1. Tags XML de isolamento de contexto (`<rules>`, `<context>`, `<output_format>`).
2. Validação estrita de tipos via Pydantic/JSON Schema.
3. Protocolo Source-Only (rejeição determinística de alucinação factual).

---

## Metodologia
- **Modelos Testados:** GPT-4o, Claude 3.5 Sonnet, Gemini 1.5 Pro.
- **Tamanho da Amostra:** 500 execuções com dados sintéticos de campanhas de tráfego pago (Meta Ads e Google Ads).
- **Variáveis Analisadas:**
  - Taxa de falha de parser JSON.
  - Taxa de alucinação (valores financeiros ou IDs inferidos que não constavam no prompt).
  - Aderência aos Quality Gates de negócio (regras de corte e escala de orçamento).

---

## Resultados Consolidados

```
+------------------------------------+----------------+-------------------+---------------+
| Configuração                       | Erro de Schema | Taxa Alucinação   | Aderência KPI |
+------------------------------------+----------------+-------------------+---------------+
| Prompt Livre (Texto Corrido)       | 18.4%          | 14.2%             | 71.0%         |
| Prompt Estruturado (Markdown puro) | 6.8%           | 5.1%              | 84.5%         |
| Prompt XML + Pydantic + Temp 0.0   | 0.2%           | 0.0% (Zero)       | 98.4%         |
+------------------------------------+----------------+-------------------+---------------+
```

### Principais Conclusões
1. **Redução Total de Alucinações:** A imposição explícita do token `NÃO_DOCUMENTADO` eliminou a tendência do modelo de inventar orçamentos quando faltavam dados nos inputs.
2. **Determinismo em Automações:** A temperatura fixada em `0.0` com esquema de validação em código tornou viável a integração direta do LLM em scripts executivos em Python, sem intervenção manual de sanitização.
