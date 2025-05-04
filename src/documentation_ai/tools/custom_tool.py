from crewai.tools import tool

@tool("Read JavaScript File")
def read_javascript_file(file_path: str) -> str:
    """Lê o conteúdo de um arquivo JavaScript (.js) e retorna como string. 
    Use essa ferramenta quando precisar analisar ou documentar o código de um arquivo JavaScript."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Arquivo não encontrado: {file_path}"
    except Exception as e:
        return f"Ocorreu um erro ao ler o arquivo: {str(e)}"