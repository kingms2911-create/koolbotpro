from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
import agent
import os

app = FastAPI(title="Cloud Computer Agent API")

class TaskRequest(BaseModel):
    prompt: str
    api_secret: str

@app.get("/")
def home():
    return {"status": "Computer Agent Server Running"}

@app.post("/run-agent")
async def run_agent_task(request: TaskRequest):
    if request.api_secret != os.getenv("API_SECRET", "default_secret"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    result = await agent.execute_task(request.prompt)
    return result
