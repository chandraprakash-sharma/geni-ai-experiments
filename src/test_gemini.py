from llm.gemini_client import client

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explain what an LLM is in one sentence."
)

print(response.text)