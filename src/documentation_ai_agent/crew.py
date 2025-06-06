from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from documentation_ai_agent.tools.custom_tool import (
    read_file,
    generate_git_diff,
    classify_code_changes,
    update_business_documentation,
    list_project_files,
    write_file,
    fetch_and_read_response,
)
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print('GOOGLE_APPLICATION_CREDENTIALS')
print(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

@CrewBase
class App():
    """App crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    llm = 'gemini-2.0-flash'

    # 1️⃣ Agent: gerar diff
    @agent
    def business_documentator(self) -> Agent:
        return Agent(
            config=self.agents_config['business_documentator'],
            verbose=True,
            tools=[read_file, list_project_files, update_business_documentation],
            llm=self.llm
        )

    # 2️⃣ Agent: classificar mudanças
    @agent
    def code_diff_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_diff_analyzer'],
            verbose=True,
            tools=[generate_git_diff, classify_code_changes, write_file],
            llm=self.llm
        )

    # 3️⃣ Agent: atualizar documentação
    @agent
    def pr_webhook_listener(self) -> Agent:
        return Agent(
            config=self.agents_config['pr_webhook_listener'],
            verbose=True,
            tools=[fetch_and_read_response],
            llm=self.llm
        )

    # 📑 Tasks
    @task
    def pr_webhook_handler_task(self) -> Task:
        return Task(
            config=self.tasks_config['pr_webhook_handler_task'],
        )

    @task
    def process_code_changes_task(self) -> Task:
        return Task(
            config=self.tasks_config['process_code_changes_task'],
        )

    @task
    def documentar_negocio_task(self) -> Task:
        return Task(
            config=self.tasks_config['documentar_negocio_task'],
        )

    # 🧑‍🚀 Crew
    @crew
    def crew(self) -> Crew:
        """Creates the Documentation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
