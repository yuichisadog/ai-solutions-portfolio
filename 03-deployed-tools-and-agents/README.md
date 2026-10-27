# Módulo 03: Ferramentas Internas Deployadas, Dashboards e Agentes de IA

Este módulo documenta as soluções de software em produção, interfaces implantadas e a arquitetura de agentes autônomos baseada no protocolo MCP (Model Context Protocol).

## 1. Soluções e Ferramentas em Produção

### 1.1 Dashboard de Performance Road (Deployado no Render)
- **URL em Produção:** `https://road-dashboard-performance-2.onrender.com/`
- **Função:** Plataforma centralizadora de inteligência de tráfego que consome APIs do Google Ads, Meta Ads e GA4, agregando métricas de investimento, receita, ROAS, CPA e pacing diário para múltiplos clientes simultaneamente.
- **Usuários:** Diretoria da agência, gestores de tráfego e clientes finais para acompanhamento em tempo real sem necessidade de reuniões semanais burocráticas.

### 1.2 Arquitetura de Agentes Autônomos & MCP (Model Context Protocol)
- **Conceito:** Orquestração de subagentes especializados dotados de ferramentas de leitura e mutação seguras:
  - `Google Ads Agent`: Executa consultas em GAQL com validação de orçamentos e termos de pesquisa.
  - `Meta Ads Agent`: Conexão com Graph API para auditoria de fadiga de criativos e escala de conjuntos.
  - `Competitor Intelligence Agent`: Navegação stealth headless para monitoramento de anúncios da concorrência na Ad Library.
  - `Memory Layer`: Persistência de contexto entre sessões para histórico de decisões estratégicas.

### 1.3 Validador Ponta a Ponta de Rastreamento (Selenium E2E)
- **Função:** Script de automação de testes com Selenium e headless Chrome que carrega páginas de clientes, simula disparos de formulários e cliques em WhatsApp, inspecionando se os payloads de rede e eventos do `dataLayer` e tags do Google Tag Manager (GTM) são disparados corretamente antes do deploy de novas campanhas.
- **Impacto:** Eliminação total de discrepâncias de atribuição e perda de conversões em lançamentos críticos.
