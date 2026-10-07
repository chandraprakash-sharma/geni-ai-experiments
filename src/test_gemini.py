from llm.gemini_client import client

temperature = 1.0
prompt =  """What is AI? in two lines"""
for run in range(1,6):

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents= prompt,
        config = {
            "temperature": temperature,
            "max_output_tokens": 300
        }
    )

    print(f"\n{'=' * 50}")
    print(f"Run {run} | Temperature: {temperature}")
    print(f"{'=' * 50}")
    print(response.text)