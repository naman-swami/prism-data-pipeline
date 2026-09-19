import os
from lyzr import Studio

studio = Studio(api_key=os.environ.get("LYZR_API_KEY", "dummy_key"))
agent = studio.create_agent(
    name="prism-data-pipeline",
    provider="openai",
    role="Principal Data Platform Architect",
    goal="Detect upstream schema anomalies, prevent breaking changes across analytical pipelines, and automate data lineage reconciliation.",
    instructions="Operate according to OpenGAP specifications."
)
