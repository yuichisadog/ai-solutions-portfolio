# Arquitetura de Agentes Autônomos & MCP (Model Context Protocol)

## 1. Visão Geral
Estrutura de orquestração multiagente projetada para delegar tarefas especializadas de mídia paga com isolamento estrito de contexto, memória de longo prazo e chamadas de ferramentas seguras.

## 2. Princípios de Engenharia de Agentes
- **Isolamento de Contexto:** Cada subagente opera com uma janela de contexto limpa e ferramentas específicas para seu domínio, prevenindo degradação de atenção do LLM.
- **Protocolo MCP:** Ferramentas são expostas como contratos de schema tipados (JSON Schema) que validam argumentos antes da execução de requisições externas.
- **Memória de Longo Prazo:** Histórico de decisões estratégicas e regras aprendidas são persistidos em disco e recuperados por relevância semântica.
