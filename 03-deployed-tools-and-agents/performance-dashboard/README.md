# Dashboard Integrado de Performance (Deploy em Produção)

## 1. Visão Geral
Aplicação web analítica hospedada em nuvem pública (Render) projetada para unificar o fluxo de dados de performance da agência.

- **Link de Acesso:** `https://road-dashboard-performance-2.onrender.com/`
- **Ambiente de Hospedagem:** Render Cloud Platform
- **Público Ativo:** Liderança operacional da agência, analistas e clientes corporativos

---

## 2. Funcionalidades Principais
1. **Consolidação Multicanal:** Integração direta de dados de Meta Ads (Facebook e Instagram), Google Ads (Search e PMax) e Google Analytics 4.
2. **Monitoramento de Pacing em Tempo Real:** Cálculo automático do ritmo de gasto projetado contra a verba mensal contratada, destacando desvios acima de 15%.
3. **Visão Financeira por Cliente:** Exibição clara de Investimento, Receita Direta, Blended ROAS, CPL e CAC de fechamento.
4. **Governança de Saldo e Boleto:** Indicadores visuais de runway de saldo em dias para prevenir pausas operacionais.

---

## 3. Arquitetura da Solução

```
[ APIs de Mídia (Meta / Google / GA4) ]
                   │
                   ▼ (ETL Agendado / Webhooks)
[ Camada de Ingestão & Validação (Python / Pandas) ]
                   │
                   ▼ (Dados Tratados)
[ Dashboard Web (FastAPI / Render) ]
                   │
                   ▼ (Visualização em Tempo Real)
[ Gestores de Tráfego / Diretoria / Clientes ]
```
