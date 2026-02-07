from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

from config import API_PORT, API_HOST
from agent import SimpleAgent, AgentMode


# ==================== MODELOS PYDANTIC ====================

class AskRequest(BaseModel):
    prompt: str
    use_gpt: bool = False


class StudyRequest(BaseModel):
    prompt: str
    context: Optional[str] = None
    use_gpt: bool = False


class PlanRequest(BaseModel):
    prompt: str
    goals: Optional[List[str]] = None
    use_gpt: bool = False


class AgentInfoRequest(BaseModel):
    agent_name: str = "Agent1"


# ==================== INSTÂNCIA DA APLICAÇÃO ====================

app = FastAPI(
    title="Agent API",
    description="API com Agentes que operam em três modos: Ask, Study e Plan",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Armazenamento de agentes
agents = {}


# ==================== ENDPOINTS ====================

@app.get("/")
def root():
    """Endpoint raiz com informações da API"""
    return {
        "name": "Agent API",
        "version": "1.0.0",
        "description": "Backend com agentes em três modos: ask, study, plan",
        "modes": ["ask", "study", "plan"],
        "docs": "/docs"
    }


@app.post("/agent/create")
def create_agent(request: AgentInfoRequest):
    """Cria um novo agente"""
    if request.agent_name in agents:
        raise HTTPException(status_code=400, detail="Agente já existe")
    
    # Criar agente simples por padrão
    agents[request.agent_name] = SimpleAgent(name=request.agent_name)
    
    return {
        "message": "Agente criado com sucesso",
        "agent_name": request.agent_name,
        "type": "SimpleAgent"
    }


@app.get("/agent/list")
def list_agents():
    """Lista todos os agentes criados"""
    return {
        "agents": list(agents.keys()),
        "total": len(agents)
    }


@app.get("/agent/{agent_name}")
def get_agent_info(agent_name: str):
    """Retorna informações de um agente"""
    if agent_name not in agents:
        raise HTTPException(status_code=404, detail="Agente não encontrado")
    
    agent = agents[agent_name]
    return {
        "name": agent.name,
        "description": agent.description,
        "history_size": len(agent.get_history())
    }


@app.post("/agent/{agent_name}/ask")
def agent_ask(agent_name: str, request: AskRequest):
    """
    Modo ASK: Pergunta ao agente para uma resposta direta
    """
    if agent_name not in agents:
        # Criar agente se não existir
        agents[agent_name] = SimpleAgent(name=agent_name)
    
    agent = agents[agent_name]
    response = agent.ask(request.prompt)
    
    return response.to_dict()


@app.post("/agent/{agent_name}/study")
def agent_study(agent_name: str, request: StudyRequest):
    """
    Modo STUDY: Pede ao agente uma análise profunda
    """
    if agent_name not in agents:
        agents[agent_name] = SimpleAgent(name=agent_name)
    
    agent = agents[agent_name]
    response = agent.study(request.prompt, request.context)
    
    return response.to_dict()


@app.post("/agent/{agent_name}/plan")
def agent_plan(agent_name: str, request: PlanRequest):
    """
    Modo PLAN: Pede ao agente para criar um plano de ação
    """
    if agent_name not in agents:
        agents[agent_name] = SimpleAgent(name=agent_name)
    
    agent = agents[agent_name]
    response = agent.plan(request.prompt, request.goals)
    
    return response.to_dict()


@app.get("/agent/{agent_name}/history")
def get_agent_history(agent_name: str):
    """Retorna o histórico de conversações do agente"""
    if agent_name not in agents:
        raise HTTPException(status_code=404, detail="Agente não encontrado")
    
    agent = agents[agent_name]
    return {
        "agent_name": agent_name,
        "history": agent.get_history()
    }


@app.delete("/agent/{agent_name}/history")
def clear_agent_history(agent_name: str):
    """Limpa o histórico do agente"""
    if agent_name not in agents:
        raise HTTPException(status_code=404, detail="Agente não encontrado")
    
    agent = agents[agent_name]
    agent.clear_history()
    
    return {
        "message": "Histórico limpo com sucesso",
        "agent_name": agent_name
    }


@app.delete("/agent/{agent_name}")
def delete_agent(agent_name: str):
    """Deleta um agente"""
    if agent_name not in agents:
        raise HTTPException(status_code=404, detail="Agente não encontrado")
    
    del agents[agent_name]
    
    return {
        "message": "Agente deletado com sucesso",
        "agent_name": agent_name
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "ok",
        "agents_count": len(agents)
    }


# ==================== MAIN ====================

if __name__ == "__main__":
    print(f"🚀 Iniciando Agent API em {API_HOST}:{API_PORT}")
    print(f"📚 Documentação disponível em http://{API_HOST}:{API_PORT}/docs")
    
    uvicorn.run(
        app,
        host=API_HOST,
        port=API_PORT,
        log_level="info"
    )
