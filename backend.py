# Step 1: Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Step 2: Setup AI Agent from Frontend Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES=["llama3-70b-8192","mixtral-8x7b-32768","llama-3.3-70b-versatile"]

app = FastAPI(title="Langchain AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with Chatbot using Langgraph and search tools.
    It dynamically selects the model specified in the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": f"Model '{request.model_name}' is not allowed. Kindly select a valid AI Model"}
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    # Create A1 Agent and get response from it.
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response
        
# Step 3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=9999)
    











