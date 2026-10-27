# Especificação da Suíte de Testes E2E de Rastreamento

## 1. Objetivo
Garantir que nenhuma campanha de tráfego pago vá ao ar sem a validação mecânica de que as conversões primárias (leads, compras, cliques em botões de WhatsApp) estão sendo capturadas pelo Google Tag Manager (GTM) e enviadas para o GA4 e Meta CAPI.

---

## 2. Eventos Auditados na Janela do Navegador

| Nome do Evento | Gatilho no Site | Parâmetros Obrigatórios no `dataLayer` |
| :--- | :--- | :--- |
| `page_view` | Carregamento da página | `page_location`, `page_title` |
| `contact_click` | Clique em botão de WhatsApp | `button_id`, `destination_phone` |
| `generate_lead` | Submissão de formulário B2B | `form_id`, `expected_value`, `lead_type` |
| `purchase` | Página de confirmação de pedido | `transaction_id`, `value`, `currency`, `items` |

---

## 3. Protocolo de Bloqueio de Deploy
Se o teste automatizado não detectar o evento `generate_lead` ou `purchase` após a simulação de clique no elemento DOM correspondente, o agente de CI/CD reprova a publicação do container do GTM, emitindo alerta para correção imediata do desenvolvedor.
