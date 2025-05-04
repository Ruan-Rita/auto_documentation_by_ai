from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from documentation_ai.tools.custom_tool import read_javascript_file
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
    # llm = LLM(
    #     model=os.getenv("GOOGLE_MODEL"),
    #     api_key=os.getenv("GOOGLE_API_KEY"),
    #     # base_url=os.getenv("GOOGLE_API_URL")
    # )
    llm = 'gemini-2.0-flash'

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def code_documentator(self) -> Agent:
        return Agent(
            config=self.agents_config['code_documentator'], # type: ignore[index]
            verbose=True,
            tools=[read_javascript_file],
            llm=self.llm
        )

    @agent
    def code_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['code_analyst'], # type: ignore[index]
            verbose=True,
            tools=[read_javascript_file],
            llm=self.llm
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def documentar_task(self) -> Task:
        return Task(
            config=self.tasks_config['documentar_task'], # type: ignore[index]
        )

    @task
    def analyse_code_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyse_code_task'], # type: ignore[index]
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
