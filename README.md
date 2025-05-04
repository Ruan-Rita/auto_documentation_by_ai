# 📑 Documentation AI Crew

Bem-vindo ao **Documentation AI Crew**, um projeto construído com [crewAI](https://crewai.com) para automatizar a leitura, análise e documentação de códigos JavaScript. Este projeto utiliza agentes multi-inteligentes alimentados pelo **Gemini API**, colaborando para gerar relatórios técnicos e documentação de forma automatizada e eficiente.

## 📦 Instalação

Certifique-se de ter **Python >=3.10 <3.13** instalado no seu sistema.  
Este projeto usa o [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências.

### Instalar o `uv`:
```bash
#Instalar o gerenciador de pacote:
pip install uv

#Instalar as dependências do projeto:
crewai install
```

## ⚙️ Configuração
Adicione sua variável de ambiente **GOOGLE_APPLICATION_CREDENTIALS** apontando para seu arquivo de credenciais da API Gemini:

```bash
$env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\Ruan\developer_projects\crewai\documentation_ai\credentials\meu-credentials.json"
```

### Edite as seguintes configurações conforme necessário:

- src/documentation_ai/config/agents.yaml → Definição dos agentes

- src/documentation_ai/config/tasks.yaml → Definição das tarefas

- src/documentation_ai/crew.py → Lógica, ferramentas e argumentos customizados

- src/documentation_ai/main.py → Definição dos inputs personalizados

### 🚀 Executando o Projeto
Para iniciar sua equipe de agentes AI e executar as tarefas definidas:

```bash
crewai run
```
Isso inicializa a Documentation AI Crew, organiza os agentes e distribui as tarefas.
O exemplo atual realiza a leitura de um arquivo .js, gera um relatório técnico e cria uma documentação Markdown no diretório do código.

## 📚 Entendendo a Crew
A Documentation AI Crew é composta por múltiplos agentes, cada um com objetivos e ferramentas:

**code_documentator**: pesquisa e coleta informações contextuais e relevantes

**code_analyst**: organiza e transforma essas informações em relatórios e documentações formatadas

As definições de agentes e tarefas estão em:

- src/documentation_ai/config/agents.yaml

- src/documentation_ai/config/tasks.yaml

## 📊 Resultado da Magia dos Agentes
Gera um arquivo Documentation.md com a documentação baseada no código-fonte fornecido, e um SuggestionImprovement.md contendo as sugestão de melhorias gerados pelos agentes.

[Technical Documentation: LogService](https://github.com/Ruan-Rita/auto_documentation_by_ai/blob/main/src/code_base/Documentation.md)

[Code Improvement Report: LogService](https://github.com/Ruan-Rita/auto_documentation_by_ai/blob/main/src/code_base/SuggestionImprovement.md)
