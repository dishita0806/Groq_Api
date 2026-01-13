from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

# -----------------------
# Setup
# -----------------------

app = FastAPI()

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = """
You are StudyBot.
You explain AI concepts clearly and step by step.
You use simple language and examples.
You are friendly and patient.
"""

# -----------------------
# Request / Response Models
# -----------------------

class ChatRequest(BaseModel):
    messages: list[dict]

class ChatResponse(BaseModel):
    reply: str

# -----------------------
# Routes
# -----------------------

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    # 1️⃣ Start with system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # 2️⃣ Add conversation history from client
    messages.extend(req.messages)

    # 3️⃣ Call the model
    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=messages
    )

    # 4️⃣ Extract reply
    bot_reply = response.output_text

    # 5️⃣ Return JSON
    return {"reply": bot_reply}
