import os
import httpx
import subprocess
from crewai.tools import tool

@tool("Read File")
def read_file(file_path: str) -> str:
    """Lê o conteúdo de um arquivo de texto (como .js, .ts, .py, .json, .html, etc) e retorna como string.
    Use essa ferramenta quando precisar analisar ou documentar o código ou conteúdo de qualquer arquivo."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Arquivo não encontrado: {file_path}"
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo: {str(e)}"
    
@tool("List Project Files")
def list_project_files(directory_path: str) -> str:
    """Lista todos os arquivos e diretórios dentro de um diretório,
    ignorando pastas como node_modules, .git e dist.
    Use essa ferramenta para explorar a estrutura de um projeto."""
    try:
        ignored_dirs = {'node_modules', '.git', 'dist', '__pycache__'}

        files = []
        for root, dirs, filenames in os.walk(directory_path):
            # Remove as pastas indesejadas da lista de diretórios a serem percorridos
            dirs[:] = [d for d in dirs if d not in ignored_dirs]
            for name in filenames:
                files.append(os.path.join(root, name))
                
        return "\n".join(files) if files else "Nenhum arquivo encontrado."
    except Exception as e:
        return f"Ocorreu um erro ao listar os arquivos: {str(e)}"
    
@tool("Async HTTP Request and Response Reader")
async def fetch_and_read_response(method: str, url: str, data: dict = None, headers: dict = None) -> str:
    """Faz uma requisição HTTP assíncrona e retorna o conteúdo da resposta para o agente analisar."""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.request(method=method.upper(), url=url, json=data, headers=headers)

            # Se for JSON tenta formatar
            try:
                content = response.json()
                return f"Status: {response.status_code}\n\nResponse JSON:\n{content}"
            except Exception:
                return f"Status: {response.status_code}\n\nResponse Text:\n{response.text}"

    except Exception as e:
        return f"Ocorreu um erro ao fazer a requisição: {str(e)}"
    
# @tool("Run NPM Command")
# def run_npm_command(command: str) -> str:
#     """Executa um comando npm no terminal e retorna a saída. Use apenas para comandos npm seguros."""
#     try:
#         # Só permite comandos npm para segurança
#         if not command.startswith("npm "):
#             return "Comando não permitido. Apenas comandos npm são aceitos."

#         result = subprocess.run(command, shell=True, capture_output=True, text=True)
#         output = result.stdout
#         error = result.stderr

#         if result.returncode == 0:
#             return f"Comando executado com sucesso:\n\n{output}"
#         else:
#             return f"Ocorreu um erro ao executar o comando:\n\n{error}"

#     except Exception as e:
#         return f"Ocorreu um erro inesperado: {str(e)}"
    
@tool("Generate Git Diff")
def generate_git_diff(diff_target: str, output_path: str) -> str:
    """Gera um diff entre o HEAD atual e o target especificado, salvando no output_path."""
    try:
        command = f"git diff {diff_target} > {output_path}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            return f"Diff salvo em {output_path}"
        else:
            return f"Erro ao gerar diff:\n\n{result.stderr}"

    except Exception as e:
        return f"Ocorreu um erro ao gerar o diff: {str(e)}"
    
@tool("Write File")
def write_file(file_path: str, content: str) -> str:
    """Salva o conteúdo recebido no arquivo especificado."""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f"Conteúdo salvo em {file_path}"
    except Exception as e:
        return f"Ocorreu um erro ao salvar o arquivo: {str(e)}"
    
@tool("Classify Code Changes")
def classify_code_changes(diff_content: str) -> str:
    """Classifica alterações no diff por categoria (endpoint, regra de negócio, etc)."""
    try:
        lines = diff_content.splitlines()
        classifications = []

        for line in lines:
            if line.startswith('+') and 'app.post' in line:
                classifications.append(f"Novo endpoint detectado: {line}")
            elif 'if ' in line or 'else' in line:
                classifications.append(f"Regra de negócio modificada: {line}")
            # adicionar mais heurísticas aqui

        return "\n".join(classifications) if classifications else "Nenhuma alteração relevante detectada."
    except Exception as e:
        return f"Erro ao classificar alterações: {str(e)}"

@tool("Update Business Documentation")
def update_business_documentation(report_content: str, doc_path: str) -> str:
    """Atualiza o arquivo de documentação com base no conteúdo do report."""
    try:
        with open(doc_path, 'a', encoding='utf-8') as file:
            file.write("\n\n## Atualização automática:\n")
            file.write(report_content)
        return f"Documentação atualizada em {doc_path}"
    except Exception as e:
        return f"Erro ao atualizar documentação: {str(e)}"