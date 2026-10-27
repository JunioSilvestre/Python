# 08-monitoramento-e-observabilidade

Área de estudo de Python aplicada a Linux, engenharia e infraestrutura.

## Subáreas
- `coleta-de-metricas/` — psutil, prometheus-client — métricas do host e exposição para Prometheus.
- `parsing-de-logs/` — structlog, re — logs estruturados e extração de padrões.
- `prometheus/` — prometheus-client, requests — publicar métricas e consultar APIs.
- `grafana/` — requests — integração com a API HTTP do Grafana.
- `alertas/` — requests, httpx — integração com webhooks e APIs de notificação.
- `health-checks-e-diagnosticos/` — psutil, requests — verificar recursos locais e endpoints.

Instale dependências em um ambiente virtual por projeto; não instale tudo globalmente.
