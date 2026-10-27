# Módulo 02: Automações de Processos com Economia Real de Horas

Este módulo documenta as soluções de automação e engenharia de software desenvolvidas para eliminar gargalos manuais na operação de marketing de performance, gestão de dados e governança de contas de anúncios.

## 1. O Problema Operacional
Na gestão de múltiplas contas de alta complexidade (Google Ads, Meta Ads, GA4), analistas gastavam cerca de **3 horas por cliente toda semana** coletando prints, transcrevendo métricas de dashboards para slides, calculando pacing financeiro e conferindo saldo de boleto. Com uma carteira de 7 a 20 contas, isso consumia de **15 a 25 horas semanais por profissional**, gerando sobrecarga, fadiga e risco de erro humano em relatórios enviados à diretoria e clientes.

---

## 2. As Soluções Desenvolvidas

### 2.1 Geração Automatizada de Relatórios Executivos (`python-pptx`)
- **Funcionamento:** Pipeline em Python que consome dados consolidados de APIs de mídia, valida contra esquema JSON e instancia dinamicamente apresentações em PowerPoint (`.pptx`) completas (capa, cartões de KPI, tabelas comparativas e próximos passos) seguindo o guia visual da marca.
- **Impacto:** O tempo de geração de um relatório caiu de 3 horas para **menos de 4 minutos**. Economia consolidada superior a **15 horas semanais** por analista.

### 2.2 Motor de Auditoria Diária & Alerta de Runway Financeiro (RAIO X)
- **Funcionamento:** Script que executa auditoria em lote nas contas ativas, calculando ritmo diário de gasto (pacing), saldo disponível e runway em dias.
- **Regra de Negócio Crítica:** Dispara alertas preventivos quando o runway é menor que 7 dias (ponto de pedido de boleto/PI) e alerta urgente com menos de 3 dias, evitando a paralisação de campanhas em momentos de alta conversão.

### 2.3 Renderização Determinística de Criativos de Vídeo (HyperFrames)
- **Funcionamento:** Framework que renderiza variações de vídeos para anúncios em batch diretamente de especificações em HTML, CSS e JavaScript, integrando chamadas da API do Canva para criação de carrosséis e banners modulares.
- **Impacto:** Aceleração de 5x no ciclo de criação e teste de novos ângulos de anúncios.

### 2.4 Rotina de Backup em Nuvem e Telemetria Operacional
- **Funcionamento:** Job automatizado rodando em Máquina Virtual Oracle Cloud (Linux) com agendamento cron diário, realizando snapshot de bancos de dados locais, índices de memória de longo prazo e enviando relatórios de status via Bot do Telegram para o time.

---

## 3. Matriz de Impacto em Tempo

| Processo Operacional | Tempo Manual Anterior | Tempo com Automação | Economia Real Mensal |
| :--- | :--- | :--- | :--- |
| **Relatórios Semanais/Mensais PPTX** | 12h / mês por cliente | 15 min / mês por cliente | **~60h / mês** (carteira) |
| **Auditoria Diária de Pacing e Saldo** | 45 min / dia | 2 min / dia (automático) | **~18h / mês** |
| **Validação de Tags de Conversão** | 2h por lançamento | 3 min (Selenium E2E) | **~8h / mês** |
| **Produção de Variações de Criativos** | 4h por pacote | 20 min (código em lote) | **~15h / mês** |
| **TOTAL CONSOLIDADO ESTIMADO** | | | **~100+ horas economizadas/mês** |
