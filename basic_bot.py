from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

SYSTEM_PROMPT = "You are a helpful chatbot."

messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    response = client.responses.create(
        model="openai/gpt-oss-20b",
        input=messages
    )

    # ✅ CORRECT extraction
    bot_reply = response.output[0].content[0].text

    print("Bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})
