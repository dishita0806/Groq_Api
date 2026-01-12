from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ["GROQ_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    model="openai/gpt-oss-20b",
    input="Explain the importance of fast language models",
)

print(response.output_text)
