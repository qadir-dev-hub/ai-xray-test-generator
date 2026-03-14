#!/usr/bin/env python
import sys
import warnings
import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
from datetime import datetime
from testcrew_ai.crew import testcrew_ai

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



# Load .env variables
load_dotenv()

JIRA_BASE_URL = os.getenv("JIRA_BASE_URL")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")


def get_jira_issue(issue_key: str) -> dict:
    url = f"{JIRA_BASE_URL}/rest/api/3/issue/{issue_key}"
    response = requests.get(
        url,
        auth=HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN),
        headers={"Accept": "application/json"}
    )
    response.raise_for_status()
    return response.json()


def extract_story_for_ai(issue: dict) -> str:
    fields = issue["fields"]

    description_text = "No description provided"
    description = fields.get("description")

    if description and "content" in description:
        lines = []
        for block in description["content"]:
            if "content" in block:
                for item in block["content"]:
                    if item.get("type") == "text":
                        lines.append(item["text"])
        description_text = "\n".join(lines)

    return f"""
Title:
{fields.get("summary", "No title")}

Description:
{description_text}

Issue Type:
{fields["issuetype"]["name"]}

Priority:
{fields["priority"]["name"] if fields.get("priority") else "Not set"}
""".strip()

def run():
    """
    Run the research crew.
    """
    issue_key = "SCRUM-1"
    issue = get_jira_issue(issue_key)

    # 2️⃣ Extract story text for AI
    story_text = extract_story_for_ai(issue)


    inputs = {
        'story': story_text
    }

    # Create and run the crew
    result = testcrew_ai().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()