# 🚀 Guia de Produção

## Deploy em Servidor

### Opção 1: Direct Server

```bash
# Clone ou copie o projeto
cd /caminho/para/project

# Instale dependências
pip install -r requirements.txt

# Use Gunicorn para produção
pip install gunicorn

# Inicie com Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Opção 2: Docker

```bash
# Build da imagem
docker build -t agent-api .

# Execute container
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=sk-... \
  agent-api
```

### Opção 3: Docker Compose

```bash
# Inicie com Docker Compose
docker-compose up -d

# Logs
docker-compose logs -f

# Parar
docker-compose down
```

## Variáveis de Ambiente

```env
# Obrigatório
API_PORT=8000
API_HOST=0.0.0.0

# Opcional (para GPT)
OPENAI_API_KEY=sk-...

# Produção
DEBUG=False
ENVIRONMENT=production
```

## Nginx Reverse Proxy

```nginx
upstream agent_backend {
    server 127.0.0.1:8000;
}

server {
    listen 80;
    server_name api.seudomain.com;

    location / {
        proxy_pass http://agent_backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

## Systemd Service

Criar arquivo `/etc/systemd/system/agent-api.service`:

```ini
[Unit]
Description=Agent API Service
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/agent-api
ExecStart=/opt/agent-api/venv/bin/python app.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Iniciar:
```bash
sudo systemctl start agent-api
sudo systemctl enable agent-api
```

## Monitoramento

### Logs
```bash
# Arquivo de log
tail -f /var/log/agent-api.log

# Com systemd
journalctl -u agent-api -f
```

### Métricas
```bash
# Health check
curl http://localhost:8000/health

# Info
curl http://localhost:8000/
```

## Scaling

### Load Balancer (HAProxy)

```
global
    maxconn 4096

frontend front
    bind 0.0.0.0:80
    default_backend agent_servers

backend agent_servers
    balance roundrobin
    server server1 127.0.0.1:8001
    server server2 127.0.0.1:8002
    server server3 127.0.0.1:8003
```

## Backup & Persistência

Se usar BD, implementar:
- Daily backups
- Replicação
- WAL (Write-Ahead Logging)

## Security Checklist

- [ ] HTTPS/SSL configurado
- [ ] CORS ajustado por domínio
- [ ] Rate limiting implementado
- [ ] API keys rotacionadas
- [ ] Firewall configurado
- [ ] Updates de segurança instalados
- [ ] Logs monitorados
- [ ] Backups testados

## Performance Optimization

```python
# Em config.py
CACHE_ENABLED = True
CACHE_TTL = 3600  # 1 hora

# Use Redis se necessário
# pip install redis
```

## CI/CD (GitHub Actions)

Criar `.github/workflows/deploy.yml`:

```yaml
name: Deploy

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to server
        run: |
          # Seu script de deploy
```

## Troubleshooting Produção

### Porta já em uso
```bash
lsof -i :8000
kill -9 <PID>
```

### Memory leak
```bash
# Monitor memoria
watch -n 1 'ps aux | grep python'
```

### API lenta
```bash
# Aumentar workers
gunicorn -w 8 -b 0.0.0.0:8000 app:app
```

## Backup Histórico

Se precisar persistir histórico:

```python
# Implementar em app.py
import json
from datetime import datetime

def backup_history():
    backup_file = f"backups/history_{datetime.now().isoformat()}.json"
    with open(backup_file, 'w') as f:
        json.dump(agents_history, f, indent=2)
```

## Métricas Recomendadas

- Request/segundo
- Latência média
- Taxa de erro
- CPU usage
- Memory usage
- Requisições pendentes

## Alertas

Configurar alertas para:
- Taxa de erro > 1%
- Latência > 1000ms
- CPU > 80%
- Memória > 80%
- Disco > 90%

---

Pronto para produção! 🚀
