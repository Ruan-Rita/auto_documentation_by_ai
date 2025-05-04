#!/usr/bin/env python
import sys
import warnings
import os

from documentation_ai.crew import App

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    root_path = r'C:\Users\Ruan\developer_projects\crewai\documentation_ai'
    inputs = {
        'code_path': os.path.join(root_path, 'src', 'code_base', 'LogService.js'),
        'code_refactored_path': os.path.join(root_path, 'src', 'code_base', 'SuggestionImprovement.md'),
        'documentation_path': os.path.join(root_path, 'src', 'code_base', 'Documentation.md'),
    }
    
    try:
        App().crew().kickoff(inputs=inputs)
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
    }
    try:
        App().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        App().crew().replay(task_id=sys.argv[1])

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
    }
    
    try:
        App().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
