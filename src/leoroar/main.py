#!/usr/bin/env python
import sys
import warnings

from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from leoroar.crew import Leoroar
from leoroar.crew import SRS_Crew

# from leoroar.flows.flow import ResearchReportFlow

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "prompt": "I want to design the for a e-commerce website for selling shoes."
    }

    try:
        import os
        result = SRS_Crew().crew().kickoff(inputs=inputs)
        
        if hasattr(result, "pydantic") and result.pydantic:
            output_dir = "c:\\work\\Learn\\leoroar\\leoroar\\assets"
            os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, "SRS_Report_Output.md")
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result.pydantic.content_md)
            print(f"\\n✅ Đã lưu file báo cáo thành công tại: {output_path}")
            
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
