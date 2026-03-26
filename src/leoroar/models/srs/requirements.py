from pydantic import BaseModel, Field
from typing import List


class RequirementMetadata(BaseModel):
    actors: List[str] = Field(..., description="List of system actors (users or external systems) that interact with the system.")
    actions: List[str] = Field(..., description="Primary actions or operations the system must support.")
    constraints: List[str] = Field(..., description="Technical, business, or operational constraints that limit the system design or behavior.")


class SRSReport(BaseModel):
    content_md: str = Field(..., description="Complete Software Requirements Specification (SRS) document formatted in Markdown.")
    metadata: RequirementMetadata = Field(..., description="Structured requirement metadata used by downstream agents for further processing.")