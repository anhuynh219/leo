from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class ResearchCrew:
    """Research Crew"""

    agents_config = "config/research_crew/agents.yaml"
    tasks_config = "config/research_crew/tasks.yaml"

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def research_specialist_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["research_specialist_agent"],  # type: ignore[index]
            verbose=True,
            apps=["google_docs/create_document"],
        )

    @task
    def research_topic_task(self) -> Task:
        return Task(
            config=self.tasks_config["research_topic_task"],  # type: ignore[index]
            agent=self.research_specialist_agent(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

@CrewBase
class AnalysisCrew:
    """Analysis Crew"""

    agents_config = "config/analysis_crew/agents.yaml"
    tasks_config = "config/analysis_crew/tasks.yaml"

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def content_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["content_analyst_agent"],  # type: ignore[index]
            verbose=True,
        )

    @task
    def analyze_and_summarize_information_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_and_summarize_information_task"],  # type: ignore[index]
            agent=self.content_analyst_agent(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


@CrewBase
class ReportCrew:
    """Report Crew"""

    agents_config = "config/report_crew/agents.yaml"
    tasks_config = "config/report_crew/tasks.yaml"

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent  
    def report_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer_agent"],  # type: ignore[index]
            verbose=True,
            apps=["google_docs/insert_text"],
        )

    @task
    def create_google_docs_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_google_docs_report_task"],  # type: ignore[index]
            agent=self.report_writer_agent(),
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


@CrewBase
class Leoroar:
    """Leoroar crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    @agent
    def report_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer_agent"],  # type: ignore[index]
            verbose=True,
            apps=["google_docs/create_document"],
        )

    # @agent
    # def summary_agent(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['summary_agent'], # type: ignore[index]
    #         verbose=True,
    #         apps=['google_docs/get_document']
    # )

    # @task
    # def summary_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['summary_task'], # type: ignore[index]
    #         agent=self.summary_agent(),
    #     )

    @task
    def create_google_docs_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["create_google_docs_report_task"],  # type: ignore[index]
            agent=self.report_writer_agent(),
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @crew
    def crew(self) -> Crew:
        """Creates the Leoroar crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
