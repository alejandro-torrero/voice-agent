import os
from dotenv import load_dotenv
from livekit.agents import cli, WorkerOptions, AgentServer
from voice_agent import Assistant, Transporter

load_dotenv()

from livekit.agents import JobContext, JobProcess

server=AgentServer(
    ws_url=os.getenv("LIVEKIT_URL"),
    api_key=os.getenv("LIVEKIT_API_KEY"),
    api_secret=os.getenv("LIVEKIT_API_SECRET"),        
)   

@server.rtc_session(agent_name="general-agent")
async def entrypoint(ctx: JobContext):
    """Entrypoint function for the general-agent"""
    
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }
    
    prompt = "Interactùa como un amigo de toda la vida"
    
    assistant = Assistant(prompt)
    
    transporter = Transporter()
    
    transporter.build_stt()
    
    transporter.build_tts()
    
    transporter.build_transporter_session()
    
    await transporter.start_transporter_session(ctx,assistant)


if __name__ == "__main__":
    print("Starting livekit hybrid service")
        
    cli.run_app(
        server
    )