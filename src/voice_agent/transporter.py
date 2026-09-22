from livekit.plugins import deepgram, elevenlabs

from livekit.agents import AgentSession


class Transporter():
    """Transporter is a class that selects the auxilary services that transport data 
    from and to the Agent"""
    
    session: AgentSession = None
    stt = None
    tts = None
    
    def __init__(self) ->None:
        pass
    
    def build_stt(self) ->None:
        self.stt= deepgram.STT(model="nova-3",language="es-419")        
    
    def build_tts(self) ->None:
        self.tts= elevenlabs.TTS(model="eleven_flash_v2_5")
    
    def build_transporter_session(self) -> None:
        self.session = AgentSession(
            stt=self.stt,
            tts=self.tts,            
        )
        
    async def start_transporter_session(self,ctx, agent) -> None:
        await self.session.start(
            agent=agent,
            room=ctx.room,            
        )
        await ctx.connect()