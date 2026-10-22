from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import agent
import os

app = FastAPI(title="Cloud Computer Agent API")

# Allow Vercel & All Frontends (CORS Fix)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskRequest(BaseModel):
    prompt: str
    api_secret: str = "default_secret"

@app.get("/")
def home():
    return {"status": "Computer Agent Server Running"}

@app.post("/run-agent")
async def run_agent_task(request: TaskRequest):
    try:
        result = await agent.execute_task(request.prompt)
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}
