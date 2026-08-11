from fastapi import FastAPI
from pydantic import BaseModel
from agent import generate_agent_response

app = FastAPI()


class AgentRequest(BaseModel):
    request: str


@app.get("/")
def home():
    return {"message": "AI Agent API is running"}


@app.post("/generate")
def generate_document(data: AgentRequest):
    result = generate_agent_response(data.request)
    return result