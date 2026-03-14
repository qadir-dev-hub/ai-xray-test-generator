from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from testcrew_ai.tools.xray_tool import XrayCreateTestTool


@CrewBase
class testcrew_ai():
    """testcrew_ai crew"""


    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def test_case_writer(self)->Agent:
         return Agent(
            config=self.agents_config['test_case_writer'],
            verbose=True
        )

    @agent
    def test_case_reviewer(self)->Agent:
        return Agent(
            config=self.agents_config['test_case_reviewer'],
            verbose=True,
            tools=[XrayCreateTestTool()]
        )

    @task
    def write_test_cases(self)->Task:
         return Task(
            config=self.tasks_config['write_test_cases'],
        )

    @task
    def review_test_cases(self)->Task:
         return Task(
            config=self.tasks_config['review_test_cases'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the manual testing crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
