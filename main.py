from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import requests

app = FastAPI(title="Voice Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://vineeth1-voice+text-assistant.netlify.app",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Voice Assistant API is running!"}

@app.post("/ask")
def ask_ai(request: AskRequest):
    api_key = os.getenv("PERPLEXITY_API_KEY")

    if not api_key:
        return {"error": "PERPLEXITY_API_KEY not set"}

    try:
        response = requests.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "sonar-pro",
                "messages": [
                    {"role": "system", "content": "You are a helpful voice assistant."},
                    {"role": "user", "content": request.text}
                ]
            }
        )

        result = response.json()
        reply = result["choices"][0]["message"]["content"]

        return {"reply": reply}

    except Exception as e:
        return {"error": str(e)}
