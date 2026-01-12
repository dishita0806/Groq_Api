from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = """
You are StudyBot.
You explain AI concepts clearly and step by step.
"""

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # 1️⃣ Add user message to conversation
    messages.append({"role": "user", "content": user_input})

    # 2️⃣ Send FULL conversation to model
    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=messages
    )

    # 3️⃣ Extract model reply
    bot_reply = response.output_text

    # 4️⃣ Print reply
    print("Bot:", bot_reply)

    # 5️⃣ Save assistant reply (memory)
    messages.append({"role": "assistant", "content": bot_reply})
