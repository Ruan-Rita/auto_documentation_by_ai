#!/usr/bin/env python
import sys
import warnings
import os

from documentation_ai_agent.crew import CrewApp
from flask import Flask, request, jsonify

server = Flask(__name__)
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

@server.route('/check-health', methods=['GET'])
def checkServer():
    return jsonify({'status': 'HEALTHLY'}), 200


@server.route('/webhook/repository', methods=['POST'])
def webhookRepository():
    """
    Run the crew.
    """
    data = request.json

    # Extrai branch de origem, destino e PR number
    source_branch = data['pull_request']['head']['ref']
    target_branch = data['pull_request']['base']['ref']
    pr_number = data['pull_request']['number']

    inputs = {
        'source_branch': source_branch,
        'target_branch': target_branch,
        'pr_number': pr_number
    }

    try:
        result = CrewApp().crew().kickoff(task_name='pr_webhook_handler_task', inputs=inputs)
        return jsonify({'Output': result}), 200
    except Exception as e:
        return jsonify({'Error': f"An error occurred while running the crew: {e}"})
    
def run():
    """
    Run the crew.
    """
    root_path = r'C:\Users\Ruan\developer_projects\crewai\documentation_ai'

    inputs = {
        'code_path': os.path.join(root_path, 'public', 'TesteStress'),
        'business_documentation_path': os.path.join(root_path, 'public', 'Documentation.md'),
        'template_L1': os.path.join(root_path, 'public', 'templates', 'documentation_L1.md'),
        'diff_output_path': os.path.join(root_path, 'public', 'diff', 'diff.txt'),
        'classification_output_path': os.path.join(root_path, 'public', 'diff', 'classification.json'),
    }

    try:
        CrewApp().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    root_path = r'C:\Users\Ruan\developer_projects\crewai\documentation_ai'

    inputs = {
        'code_path': os.path.join(root_path, 'src', 'code_base', 'LogService.js'),
        'code_refactored_path': os.path.join(root_path, 'src', 'code_base', 'LogServiceRefctored.js'),
        'documentation_path': os.path.join(root_path, 'src', 'code_base', 'Documentation.md'),
        'diff_output_path': os.path.join(root_path, 'public', 'diff', 'diff.txt'),
        'classification_output_path': os.path.join(root_path, 'public', 'diff', 'classification.json'),
    }

    try:
        CrewApp().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewApp().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    root_path = r'C:\Users\Ruan\developer_projects\crewai\documentation_ai'

    inputs = {
        'code_path': os.path.join(root_path, 'src', 'code_base', 'LogService.js'),
        'code_refactored_path': os.path.join(root_path, 'src', 'code_base', 'LogServiceRefctored.js'),
        'documentation_path': os.path.join(root_path, 'src', 'code_base', 'Documentation.md'),
        'diff_output_path': os.path.join(root_path, 'public', 'diff', 'diff.txt'),
        'classification_output_path': os.path.join(root_path, 'public', 'diff', 'classification.json'),
    }

    try:
        CrewApp().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == '__main__':
    server.run(port=5000)
# # Execução direta (caso queira rodar por terminal)
# if __name__ == "__main__":
#     if len(sys.argv) < 2:
#         print("Uso: python main.py [run|train|replay|test] [params...]")
#         sys.exit(1)

#     command = sys.argv[1]

#     if command == "run":
#         run()
#     elif command == "train":
#         train()
#     elif command == "replay":
#         replay()
#     elif command == "test":
#         test()
#     else:
#         print(f"Comando '{command}' não reconhecido.")
#         sys.exit(1)
