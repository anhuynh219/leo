from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel
from leoroar.crew import AnalysisCrew, ReportCrew, ResearchCrew


class ResearchState(BaseModel):
    id: str = "1QgK4qruO1Ue5okNRv8B9fzKSVGAFRqx5IXXFROjBF14"
    topic: str = ""
    title: str = ""
    research_content: str = ""
    report_url: str = ""
    status: str = "New"


class ResearchReportFlow(Flow[ResearchState]):
    @start()
    def start_research(self):
        print("Starting flow")
        # Mỗi flow state lúc này tự động có thêm id, nhưng ResearchState (kiểu Pydantic)
        # không có trường `id` theo mặc định. Nếu bạn cần truy cập flow id,
        # hãy dùng getattr(self.state, "id", None) nếu nó nằm ngầm,
        # Hoặc dùng self.id cho đơn giản.
        # print(f"Flow ID: {self.id}")

        self.state.topic = "Singing Voice Synthesis"
        self.state.title = "Singing Voice Synthesis Report"
        self.state.status = "In Progress"

        input = {"topic": self.state.topic}

        result = ResearchCrew().crew().kickoff(inputs=input)
        self.state.research_content = result
        return result

    @listen(start_research)
    def analyze_and_summarize_information(self):
        input = {"topic": self.state.topic}
        result = AnalysisCrew().crew().kickoff(inputs=input)
        self.state.research_content = result
        return result

    @listen(analyze_and_summarize_information)
    def create_google_docs_report(self):
        print("Creating Google Docs report")
        input = {"topic": self.state.topic, "id": self.state.id}
        result = ReportCrew().crew().kickoff(inputs=input)
        self.state.report_url = result
        return result

    @listen(create_google_docs_report)
    def end_flow(self):
        self.state.status = "Completed"
        return self.state


# flow = ResearchReportFlow()
# flow.plot()
# result = flow.kickoff()

# print(f"Generated fun fact: {result}")
