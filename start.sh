#!/bin/bash
# Script de inicialização rápida do Agent Backend
# Execute: bash start.sh

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║              🤖 AGENT BACKEND - INICIALIZAÇÃO RÁPIDA                      ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Cores
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}📦 Passo 1: Verificando Python...${NC}"
if ! command -v python3 &> /dev/null; then
    echo "Python3 não encontrado. Instale Python 3.8+ primeiro."
    exit 1
fi
python3 --version
echo -e "${GREEN}✅ Python verificado${NC}\n"

echo -e "${BLUE}📦 Passo 2: Criando ambiente virtual...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "${GREEN}✅ Ambiente virtual criado${NC}"
else
    echo -e "${GREEN}✅ Ambiente virtual já existe${NC}"
fi
echo ""

echo -e "${BLUE}📦 Passo 3: Ativando ambiente virtual...${NC}"
source venv/bin/activate
echo -e "${GREEN}✅ Ambiente ativado${NC}\n"

echo -e "${BLUE}📦 Passo 4: Instalando dependências...${NC}"
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
echo -e "${GREEN}✅ Dependências instaladas${NC}\n"

echo -e "${BLUE}🧪 Passo 5: Executando testes...${NC}"
python3 test_agents.py
echo ""

echo -e "${BLUE}📚 Passo 6: Exemplos de uso...${NC}"
read -p "Deseja ver os exemplos? (s/n) " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Ss]$ ]]; then
    python3 example.py
fi
echo ""

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║                    ✨ TUDO PRONTO! PRÓXIMOS PASSOS:                       ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "${YELLOW}1️⃣  Inicie o servidor:${NC}"
echo "   python3 app.py"
echo ""
echo -e "${YELLOW}2️⃣  Acesse a documentação:${NC}"
echo "   http://localhost:8000/docs"
echo ""
echo -e "${YELLOW}3️⃣  Teste com o cliente:${NC}"
echo "   # Em outro terminal:"
echo "   python3 client.py"
echo ""
echo -e "${YELLOW}4️⃣  Exemplos com cURL:${NC}"
echo "   curl -X POST http://localhost:8000/agent/create \\"
echo "     -H 'Content-Type: application/json' \\"
echo "     -d '{\"agent_name\": \"test\"}'"
echo ""
echo -e "${GREEN}Documentação adicional:${NC}"
echo "   📖 README.md - Documentação completa"
echo "   ⚡ QUICKSTART.md - Guia rápido"
echo "   📝 RESUMO.md - Resumo técnico"
echo "   🚀 PRODUCAO.md - Deploy em produção"
echo ""
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                                                                            ║"
echo "║                        🎉 PRONTO PARA COMEÇAR! 🎉                         ║"
echo "║                                                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
