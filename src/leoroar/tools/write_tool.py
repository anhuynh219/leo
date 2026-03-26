from crewai_tools import FileWriterTool
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool


class WriteToolInput(BaseModel):
    filename: str = Field(description="The name of the file to write to")
    content: str = Field(description="The content to write to the file")
    # directory: str = Field(description="The directory to write the file to")
    directory: str = "c:\\work\\Learn\\leoroar\\leoroar\\assets"


class WriteTool(BaseTool):
    name: str = "Write Tool"
    description: str = "Write content to a file in a specified directory"
    args_schema: Type[BaseModel] = WriteToolInput

    def _run(self, filename: str, content: str, directory: str = "c:\\work\\Learn\\leoroar\\leoroar\\assets", overwrite: bool = True) -> str:
        file_writer_tool = FileWriterTool()
        return file_writer_tool._run(filename=filename, content=content, directory=directory, overwrite=overwrite)
