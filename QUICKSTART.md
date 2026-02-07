# 🚀 Quick Start Guide

## Setup Rápido (5 minutos)

### 1. Instale as dependências
```bash
pip install -r requirements.txt
```

### 2. Configure o arquivo .env (opcional)
```bash
# Se quiser usar OpenAI GPT, adicione sua API key
echo "OPENAI_API_KEY=sk-..." >> .env
```

### 3. Inicie o servidor
```bash
python app.py
```

Pronto! A API está em `http://localhost:8000`

---

## Testando Rapidamente

### Opção 1: Usando o Cliente Python
```bash
python client.py
```

### Opção 2: Usando cURL
```bash
# Criar agente
curl -X POST http://localhost:8000/agent/create \
  -H "Content-Type: application/json" \
  -d '{"agent_name": "test"}'

# Fazer pergunta (ASK)
curl -X POST http://localhost:8000/agent/test/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Olá"}'
```

### Opção 3: Documentação Interativa
Acesse: `http://localhost:8000/docs`

---

## Executar Testes
```bash
python test_agents.py
```

---

## Modos Disponíveis

### 🔵 ASK (Resposta Direta)
```bash
curl -X POST http://localhost:8000/agent/test/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Qual é a capital do Brasil?"}'
```

### 🟢 STUDY (Análise Profunda)
```bash
curl -X POST http://localhost:8000/agent/test/study \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explique machine learning",
    "context": "para iniciantes"
  }'
```

### 🟡 PLAN (Plano de Ação)
```bash
curl -X POST http://localhost:8000/agent/test/plan \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Aprender Python",
    "goals": ["sintaxe", "POO", "projetos"]
  }'
```

---

## Estrutura de Arquivos

```
/home/bruno/Copilot_code/
├── app.py                    # 🎯 Aplicação principal (FastAPI)
├── agent.py                  # 🤖 Classes de agentes
├── llm_agent.py             # 🧠 Agente com integração GPT
├── config.py                # ⚙️  Configurações
├── client.py                # 💻 Cliente para teste
├── example.py               # 📚 Exemplos de uso
├── test_agents.py           # 🧪 Testes unitários
├── requirements.txt         # 📦 Dependências
├── .env                     # 🔑 Variáveis de ambiente
├── Dockerfile               # 🐳 Docker
├── docker-compose.yml       # 🐳 Docker Compose
├── .gitignore              # 📝 Git ignore
├── README.md               # 📖 Documentação completa
└── QUICKSTART.md           # ⚡ Este arquivo
```

---

## Exemplos em Python

```python
from agent import SimpleAgent

# Criar agente
agent = SimpleAgent(name="MeuAgente")

# Modo ASK
response = agent.ask("Qual é a capital do Brasil?")
print(response.response)

# Modo STUDY
response = agent.study("Explique IA", context="para iniciantes")
print(response.response)

# Modo PLAN
response = agent.plan("Aprender Python", goals=["sintaxe", "POO"])
print(response.response)

# Ver histórico
print(agent.get_history())
```

---

## Próximos Passos

1. ✅ Crie seus próprios agentes customizados estendendo `BaseAgent`
2. 📊 Integre com dados do seu sistema
3. 🧠 Configure OpenAI GPT para respostas mais inteligentes
4. 🚀 Deploy em um servidor
5. 🔗 Integre com seu frontend

---

## Troubleshooting

### Porta 8000 já está em uso
```bash
# Use outra porta
API_PORT=8001 python app.py
```

### Módulos não encontrados
```bash
pip install --upgrade -r requirements.txt
```

### Erro de conexão com OpenAI
```bash
# Verifique sua API key no .env
cat .env
```

---

## Suporte

Para mais informações, veja `README.md`

---

Desenvolvido com ❤️
