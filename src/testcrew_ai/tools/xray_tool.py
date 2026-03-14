import os
import requests
from dotenv import load_dotenv
from pathlib import Path
from crewai.tools import BaseTool

# Load .env
# env_path = Path(__file__).parent.parent / ".env"
# load_dotenv(dotenv_path=env_path)
load_dotenv()

XRAY_CLIENT_ID = os.getenv("XRAY_CLIENT_ID")
XRAY_CLIENT_SECRET = os.getenv("XRAY_CLIENT_SECRET")


def get_xray_token():
    response = requests.post(
        "https://xray.cloud.getxray.app/api/v2/authenticate",
        json={
            "client_id": XRAY_CLIENT_ID,
            "client_secret": XRAY_CLIENT_SECRET
        }
    )
    response.raise_for_status()
    return response.text.strip('"')


class XrayCreateTestTool(BaseTool):
    name: str = "Create Xray Test"
    description: str = "Creates a Manual Test in Xray Jira project"

    def _run(self, summary: str, description: str, project_key: str = "SCRUM"):

        token = get_xray_token()

        payload = [
            {
                "xray_testtype": "Manual",
                "fields": {
                    "project": {"key": project_key},
                    "summary": summary,
                    "description": description,
                    "issuetype": {"name": "Test"},
                    # Replace with your actual Test Type field ID if needed
                }
            }
        ]

        response = requests.post(
            "https://xray.cloud.getxray.app/api/v2/import/test/bulk",
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            json=payload
        )

        response.raise_for_status()
        return response.json()
