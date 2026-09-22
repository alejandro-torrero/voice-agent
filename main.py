import os
from dotenv import load_dotenv
from livekit.agents import cli, WorkerOptions, AgentServer

load_dotenv()

from livekit.agents import JobContext, JobProcess

server=AgentServer(
    ws_url=os.getenv("LIVEKIT_URL"),
    api_key=os.getenv("LIVEKIT_API_KEY"),
    api_secret=os.getenv("LIVEKIT_API_SECRET"),        
)   

@server.rtc_session(agent_name="general-agent")
def entrypoint(ctx: JobContext):
    pass


if __name__ == "__main__":
    print("Starting livekit hybrid service")
        
    cli.run_app(
        server
    )