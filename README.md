# Agent API - Backend com Agentes Inteligentes

Uma API backend em Python com agentes que operam em três modos diferentes: **Ask**, **Study** e **Plan**.

## 📋 Características

- ✅ **Modo ASK**: Respostas diretas e rápidas
- ✅ **Modo STUDY**: Análises profundas e detalhadas
- ✅ **Modo PLAN**: Criação de planos de ação estruturados
- ✅ **Histórico**: Mantém registro de todas as conversações
- ✅ **Múltiplos Agentes**: Crie e gerencie vários agentes
- ✅ **Documentação Interativa**: Swagger UI integrada
- ✅ **Integração com GPT**: Suporte para OpenAI GPT (opcional)

## 🚀 Início Rápido

### 1. Instalação

```bash
# Clone ou navegue até o diretório
cd /home/bruno/Copilot_code

# Instale as dependências
pip install -r requirements.txt
```

### 2. Configuração

Edite o arquivo `.env` com suas configurações:

```env
OPENAI_API_KEY=sua_chave_api_aqui  # Opcional, apenas se quiser usar GPT
API_PORT=8000
API_HOST=0.0.0.0
```

### 3. Execute o Servidor

```bash
python app.py
```

A API estará disponível em: **http://localhost:8000**

### 4. Documentação Interativa

Acesse: **http://localhost:8000/docs**

## 📚 Estrutura do Projeto

```
/home/bruno/Copilot_code/
├── app.py              # Aplicação FastAPI principal
├── agent.py            # Classes base de agentes (BaseAgent, SimpleAgent)
├── llm_agent.py        # Agente integrado com OpenAI GPT
├── config.py           # Configurações
├── example.py          # Exemplos de uso
├── requirements.txt    # Dependências
├── .env               # Variáveis de ambiente
└── README.md          # Esta documentação
```

## 🤖 Modos de Operação

### 1️⃣ Modo ASK - Resposta Direta

Ideal para perguntas que precisam de respostas rápidas e concisas.

**Endpoint:**
```
POST /agent/{agent_name}/ask
```

**Request:**
```json
{
  "prompt": "Qual é a capital do Brasil?"
}
```

**Response:**
```json
{
  "mode": "ask",
  "prompt": "Qual é a capital do Brasil?",
  "response": "Resposta para: Qual é a capital do Brasil?...",
  "metadata": {"processed": true}
}
```

### 2️⃣ Modo STUDY - Análise Profunda

Ideal para tópicos que precisam ser explorados em profundidade.

**Endpoint:**
```
POST /agent/{agent_name}/study
```

**Request:**
```json
{
  "prompt": "Explique como funciona machine learning",
  "context": "Para iniciantes em programação"
}
```

**Response:**
```json
{
  "mode": "study",
  "prompt": "Explique como funciona machine learning",
  "response": "Análise profunda sobre: Explique como funciona machine learning...",
  "metadata": {
    "depth": "detailed",
    "context_provided": true
  }
}
```

### 3️⃣ Modo PLAN - Plano de Ação

Ideal para criar estratégias e planos estruturados.

**Endpoint:**
```
POST /agent/{agent_name}/plan
```

**Request:**
```json
{
  "prompt": "Aprender Python do zero",
  "goals": [
    "Dominar sintaxe básica",
    "Aprender POO",
    "Criar projetos reais"
  ]
}
```

**Response:**
```json
{
  "mode": "plan",
  "prompt": "Aprender Python do zero",
  "response": "Plano de ação para: Aprender Python do zero...",
  "metadata": {
    "goals_count": 3
  }
}
```

## 🔌 Endpoints da API

### Gerenciamento de Agentes

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/agent/create` | Cria um novo agente |
| GET | `/agent/list` | Lista todos os agentes |
| GET | `/agent/{agent_name}` | Retorna info de um agente |
| DELETE | `/agent/{agent_name}` | Deleta um agente |

### Operações de Agentes

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/agent/{agent_name}/ask` | Modo ASK |
| POST | `/agent/{agent_name}/study` | Modo STUDY |
| POST | `/agent/{agent_name}/plan` | Modo PLAN |
| GET | `/agent/{agent_name}/history` | Retorna histórico |
| DELETE | `/agent/{agent_name}/history` | Limpa histórico |

### Utilidade

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Info da API |
| GET | `/health` | Health check |

## 💻 Exemplos de Uso

### Com cURL

```bash
# Criar agente
curl -X POST http://localhost:8000/agent/create \
  -H "Content-Type: application/json" \
  -d '{"agent_name": "assistente"}'

# Modo ASK
curl -X POST http://localhost:8000/agent/assistente/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Qual é a capital do Brasil?"}'

# Modo STUDY
curl -X POST http://localhost:8000/agent/assistente/study \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explique machine learning",
    "context": "para iniciantes"
  }'

# Modo PLAN
curl -X POST http://localhost:8000/agent/assistente/plan \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Aprender Python",
    "goals": ["sintaxe", "POO", "projetos"]
  }'

# Ver histórico
curl http://localhost:8000/agent/assistente/history

# Listar agentes
curl http://localhost:8000/agent/list
```

### Com Python

```python
import requests

BASE_URL = "http://localhost:8000"

# Criar agente
requests.post(f"{BASE_URL}/agent/create", json={"agent_name": "meu_agente"})

# Modo ASK
response = requests.post(
    f"{BASE_URL}/agent/meu_agente/ask",
    json={"prompt": "Como funciona Python?"}
)
print(response.json())

# Modo STUDY
response = requests.post(
    f"{BASE_URL}/agent/meu_agente/study",
    json={
        "prompt": "Explique POO",
        "context": "com exemplos práticos"
    }
)
print(response.json())

# Modo PLAN
response = requests.post(
    f"{BASE_URL}/agent/meu_agente/plan",
    json={
        "prompt": "Criar um app em Django",
        "goals": ["setup", "models", "views", "deploy"]
    }
)
print(response.json())
```

### Com JavaScript/Node.js

```javascript
const BASE_URL = "http://localhost:8000";

// Modo ASK
async function askAgent() {
  const response = await fetch(`${BASE_URL}/agent/meu_agente/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ prompt: "Como funciona Python?" })
  });
  const data = await response.json();
  console.log(data);
}

// Modo STUDY
async function studyAgent() {
  const response = await fetch(`${BASE_URL}/agent/meu_agente/study`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      prompt: "Explique POO",
      context: "com exemplos práticos"
    })
  });
  const data = await response.json();
  console.log(data);
}

// Modo PLAN
async function planAgent() {
  const response = await fetch(`${BASE_URL}/agent/meu_agente/plan`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      prompt: "Criar um app em Django",
      goals: ["setup", "models", "views", "deploy"]
    })
  });
  const data = await response.json();
  console.log(data);
}
```

## 🔧 Personalização

### Criar um Agente Customizado

```python
from agent import BaseAgent, AgentMode, AgentResponse
from typing import Optional

class MeuAgente(BaseAgent):
    def ask(self, prompt: str) -> AgentResponse:
        # Sua lógica aqui
        response = f"Resposta customizada para: {prompt}"
        agent_response = AgentResponse(
            mode=AgentMode.ASK,
            prompt=prompt,
            response=response
        )
        self.add_to_history(AgentMode.ASK, prompt, response)
        return agent_response
    
    def study(self, prompt: str, context: Optional[str] = None) -> AgentResponse:
        # Sua lógica aqui
        response = f"Análise customizada para: {prompt}"
        agent_response = AgentResponse(
            mode=AgentMode.STUDY,
            prompt=prompt,
            response=response
        )
        self.add_to_history(AgentMode.STUDY, prompt, response)
        return agent_response
    
    def plan(self, prompt: str, goals: Optional[list] = None) -> AgentResponse:
        # Sua lógica aqui
        response = f"Plano customizado para: {prompt}"
        agent_response = AgentResponse(
            mode=AgentMode.PLAN,
            prompt=prompt,
            response=response
        )
        self.add_to_history(AgentMode.PLAN, prompt, response)
        return agent_response
```

### Integração com OpenAI GPT

1. Obtenha uma chave de API em: https://platform.openai.com/api-keys
2. Adicione ao arquivo `.env`:
   ```env
   OPENAI_API_KEY=sk-...
   ```
3. Use a classe `GPTAgent`:
   ```python
   from llm_agent import GPTAgent
   agent = GPTAgent(name="gpt-agent")
   response = agent.ask("Qual é a capital do Brasil?")
   ```

## 📊 Exemplos de Resposta

### Resposta do Modo ASK
```
Pergunta: Qual é a capital do Brasil?

Resposta:
Resposta para: Qual é a capital do Brasil?

Este é um exemplo de resposta rápida e direta ao seu questionamento.
```

### Resposta do Modo STUDY
```
Tema: Explique como funciona machine learning

Análise:
1. CONTEXTO:
   - Este é um tópico importante para compreensão.

2. ANÁLISE DETALHADA:
   - Primeiro aspecto: Explicação detalhada.
   - Segundo aspecto: Insights relevantes.

3. EXEMPLOS:
   - Exemplo prático do conceito.

4. CONCLUSÕES:
   - Resumo das aprendizagens principais.
```

### Resposta do Modo PLAN
```
Objetivo: Aprender Python do zero

METAS ESPECÍFICAS:
   1. Dominar sintaxe básica
   2. Aprender POO
   3. Criar projetos reais

PASSOS DE EXECUÇÃO:
   1. Preparação e análise
   2. Planejamento detalhado
   3. Implementação
   4. Monitoramento
   5. Avaliação e ajustes

TIMELINE ESTIMADA:
   - Curto prazo: 1-2 semanas
   - Médio prazo: 1-3 meses
   - Longo prazo: 3-6 meses
```

## 🧪 Testando

Execute o arquivo de exemplo:

```bash
python example.py
```

Isso demonstrará todos os três modos em ação.

## 📝 Notas Importantes

- O `SimpleAgent` é ideal para testes e demonstrações rápidas
- O `GPTAgent` requer uma chave de API OpenAI válida
- Os agentes mantêm histórico automaticamente em memória
- Agentes são criados automaticamente se não existirem no primeiro acesso
- A API suporta múltiplos agentes simultâneos

## 🤝 Contribuições

Sinta-se livre para estender os agentes com suas próprias lógicas e integrações!

## 📄 Licença

MIT License

## ✨ Desenvolvido com ❤️

Criar agentes inteligentes e flexíveis para resolver diversos problemas!
