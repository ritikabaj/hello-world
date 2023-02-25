from google.cloud.dialogflowcx_v3.services.agents.client import AgentsClient
from google.cloud.dialogflowcx_v3.types.agent import Agent


def create_agent(code_dojo2023, agent):

    parent = "projects/" + code_dojo2023 + "/locations/global"

    agents_client = AgentsClient()

    agent = Agent(
        agent=agent,
        default_language_code="en",
    )

    response = agents_client.create_agent(request={"agent": agent, "parent": parent})

    return response