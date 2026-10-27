# Módulo 01: Prompt Engineering & Experimentação com LLMs

Este módulo documenta a metodologia, padrões arquiteturais e experimentos práticos com Modelos de Linguagem de Larga Escala (LLMs) aplicados a sistemas críticos de tomada de decisão, análise de dados e geração de conteúdo.

## 1. Princípios Arquiteturais Adotados

### 1.1 Protocolo Source-Only (Anti-Alucinação)
Para tarefas de auditoria de mídia e finanças, o modelo é instruído sob restrição de delimitação factual estrita. Se um dado ou ID não estiver explícito no contexto injetado, o modelo deve emitir o token `NÃO_DOCUMENTADO` ou `INSUFICIENTE`, impedindo inferências criativas sobre métricas de investimento.

### 1.2 Delimitação Estruturada (XML & Markdown Tags)
Utilização de tags XML explícitas (`<context>`, `<instructions>`, `<rules>`, `<schema>`, `<output_format>`) para separar instruções de sistema, contexto de negócio e dados do usuário. Isso previne injeção de prompt indireta e melhora a aderência estrutural do modelo.

### 1.3 Saídas Determinísticas via JSON Schema (Structured Outputs)
Em pipelines de produção que alimentam bancos de dados ou rotinas de código (como geração de relatórios PPTX), todas as respostas são forçadas contra um JSON Schema validado via Pydantic, garantindo tipos estritos (float, int, ISO datetime).

### 1.4 Calibração de Hiperparâmetros (Temperature & Top-p)
- **Extração analítica e auditoria financeira:** `temperature=0.0`, `top_p=0.1` (foco em determinismo e reprodutibilidade).
- **Estratégia criativa e variação de anúncios:** `temperature=0.7`, `top_p=0.9` (espaço para recombinação semântica e ângulos inovadores de copy).

---

## 2. Estrutura dos Arquivos Deste Módulo

```
01-prompt-engineering/
├── README.md                           # Visão geral e fundamentação técnica
├── prompts/
│   ├── diagnostic-reasoning.xml        # Prompt com CoT para diagnóstico e recomendação de mídia
│   ├── creative-strategy-eval.md       # Avaliação psicológica e técnica de criativos
│   ├── prompt-builder-system.md        # Meta-prompt para refinamento de briefings
│   └── structured-kpi-extractor.json   # JSON Schema oficial para extração de métricas
└── experiments/
    ├── temperature_eval.py             # Script de teste de estabilidade paramétrica
    ├── test_prompt_eval.py             # Suite de testes com pytest para validação de esquemas
    └── results_benchmark.md            # Resultados empíricos de acurácia e redução de alucinações
```

---

## 3. Principais Resultados dos Experimentos

| Métrica Avaliada | Baseline (Prompt Livre) | Com XML + Source-Only + JSON Schema | Ganho |
| :--- | :--- | :--- | :--- |
| **Taxa de Alucinação Factual** | 14.2% | **0.0%** (zero alucinação em 500 testes) | -100% |
| **Erros de Parse JSON** | 8.6% | **0.2%** | -97.6% |
| **Aderência às Regras de Negócio** | 71.0% | **98.4%** | +38.6% |
| **Tempo de Validação Humana** | 12 min/análise | **1.5 min/análise** | -87.5% |
