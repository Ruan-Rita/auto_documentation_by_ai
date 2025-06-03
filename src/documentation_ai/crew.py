from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from documentation_ai.tools.custom_tool import list_project_files
from documentation_ai.tools.custom_tool import read_file
from typing import List
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

print('GOOGLE_APPLICATION_CREDENTIALS')
print(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class App():
    """App crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    llm = 'gemini-2.0-flash'

    @agent
    def business_documentator(self) -> Agent:
        return Agent(
            config=self.agents_config['business_documentator'], # type: ignore[index]
            verbose=True,
            tools=[read_file, list_project_files],
            llm=self.llm
        )

    @task
    def documentar_negocio_task(self) -> Task:
        return Task(
            config=self.tasks_config['documentar_negocio_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Documentation crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
