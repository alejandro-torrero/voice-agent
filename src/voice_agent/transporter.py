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
    
    def build_stt(self,provider:str, config) ->None:
        stt= deepgram.STT()
        pass
    
    def build_tts(sefl,provider:str, config) ->None:
        stt= elevenlabs()
        pass
    
    def build_transporter_session(self) -> None:
        self.session = AgentSession(
            stt=self.stt,
            tts=self.tts,            
        )
        
    async def start_transporter_session(self,ctx, agent) -> None:
        await self.session.start(
            agent=agent(),
            room=ctx.room,            
        )
        await ctx.connect()