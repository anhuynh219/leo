from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel
from leoroar.crew import SRS_Crew


class SRSState(BaseModel):
    meta_data: dict = Field(..., description="Metadata for the SRS")
    content_md: str = Field(..., description="Content of the SRS")
   

class SRS_FLOW(Flow[SRSState]):
    @start()
    def compose(self):
        print("Starting flow")

        input = {"prompt": "Create a SRS for a web application that allows users to upload files and share them with other users."}

        result = SRS_Crew().crew().kickoff(inputs=input)
        self.state.meta_data = result.meta_data
        self.state.content_md = result.content_md
        return result

    @listen(compose)
    def analyze_and_summarize_information(self):
        input = {"topic": self.state.topic}
        result = AnalysisCrew().crew().kickoff(inputs=input)
        self.state.research_content = result
        return result

    @listen(start_research)
    def create_google_docs_report(self):
        print("Creating Google Docs report")
        input = {"topic": self.state.topic, "id": self.state.id}
        result = ReportCrew().crew().kickoff(inputs=input)
        self.state.report_url = result
        return result