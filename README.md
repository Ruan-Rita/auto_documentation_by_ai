# 📑 Documentation AI Crew

Bem-vindo ao **Documentation AI Crew**, um projeto construído com [crewAI](https://crewai.com) para automatizar a leitura, análise e documentação de códigos JavaScript. Este projeto utiliza agentes multi-inteligentes alimentados pelo **Gemini API**, colaborando para gerar relatórios técnicos e documentação de forma automatizada e eficiente.

## 📦 Instalação

Certifique-se de ter **Python >=3.10 <3.13** instalado no seu sistema.  
Este projeto usa o [UV](https://docs.astral.sh/uv/) para gerenciamento de dependências.

### Instalar o `uv`:
```bash
pip install uv
Instalar as dependências do projeto:
bash
Copiar
Editar
crewai install
```

## ⚙️ Configuração
Adicione sua variável de ambiente **GOOGLE_APPLICATION_CREDENTIALS** apontando para seu arquivo de credenciais da API Gemini:

```bash
Copiar
Editar
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
Copiar
Editar
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

## 📖 Exemplo de Output
Gera um arquivo Documentation.md com a documentação baseada no código-fonte fornecido, e um SuggestionImprovement.md contendo as sugestão de melhorias gerados pelos agentes.

## Technical Documentation: LogService

## Overview

The `LogService` class provides a simple logging mechanism for a Node.js application. It allows writing log messages and error messages to separate files. The service creates a log directory if it doesn't exist and appends messages to the specified log files, including a timestamp for each entry.

## 1. Class: `LogService`

### Description

The `LogService` class encapsulates the functionality for writing log and error messages to files.

### Attributes

*   `directory`: (string) The directory where log files are stored (default: `'./src/logs/'`).
*   `loggFile`: (string) The name of the log file for general log messages (default: `'nodejs.log'`).
*   `errorFile`: (string) The name of the log file for error messages (default: `'error.log'`).

### Constructor

The constructor initializes the log directory. If the directory doesn't exist, it creates one.

## 2. Methods

### `logg(fileContent)`

Writes a log message to the `loggFile`.

*   `fileContent`: (any) The content to be logged (will be stringified).
*   It prepends the current date and time to the log message.
*   Uses `addContent` method to append the formatted log message to the log file.

### `error(fileContent)`

Writes an error message to the `errorFile`.

*   `fileContent`: (any) The content to be logged (will be stringified).
*   It prepends the current date and time to the error message.
*   Uses `addContent` method to append the formatted error message to the error file.

### `addContent(filePath, fileContent)`

Appends the given content to the specified file.

*   `filePath`: (string) The path to the file.
*   `fileContent`: (string) The content to append to the file.
*   It adds a newline character `\n` after the content.
*   Handles potential errors during file appending, logging any errors to the console.

## 3. Dependencies

*   `fs` (Node.js File System module): Used for file system operations like checking if a directory exists, creating a directory, and appending to a file.
*   `path` (Node.js Path module): Used for joining directory and file names to create file paths.
*    `formatDate` (from `../utils/date`): Used to format the current date and time for inclusion in the log messages.

## 4. File Structure

The service writes logs to files within a specified directory. The default directory is `./src/logs/`, and it contains two files:
*   `nodejs.log`: for standard logs
*   `error.log`: for errors

## 5. Usage

To use the `LogService`, you need to:

1.  Import the `LogService` class.
2.  Create an instance of the `LogService`.
3.  Call the `logg()` method to write log messages or the `error()` method to write error messages.

## 6. Error Handling

The `addContent` method includes basic error handling for file appending operations. If an error occurs during the `fs.appendFile` operation, it logs the error message to the console.

## 7. Date Formatting

The `formatDate` function (imported from `'../utils/date'`) is used to format the date and time for log entries.  The specific implementation of `formatDate` is assumed to be available in the specified utility file.

## 8. Initialization

The constructor ensures that the log directory exists. If the directory does not exist, it creates one using `fs.mkdirSync`.

## 9. Modularization

The class is exported as a module, allowing it to be easily imported and used in other parts of the application via `module.exports = LogService;`.

## 10. Potential Improvements

*   Implement more robust error handling, including logging errors to a separate error stream or file.
*   Add support for different log levels (e.g., DEBUG, INFO, WARN, ERROR).
*   Implement log rotation to prevent log files from growing too large.
*   Add configuration options for the log directory and file names.