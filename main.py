from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ✅ Allow your frontend domain
origins = [
    "charming-malasada-69ad7d.netlify.app",  # Replace with your Netlify URL
    "http://localhost:3000",              # For local testing
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allowed domains
    allow_credentials=True,
    allow_methods=["*"],    # GET, POST, etc.
    allow_headers=["*"],    # Any headers
)

# Example request model
class AskRequest(BaseModel):
    text: str

@app.post("/ask")
async def ask_ai(request: AskRequest):
    user_input = request.text
    # For now, just echo it or your Perplexity API call
    reply = f"Echo: {user_input}"
    return {"reply": reply}
