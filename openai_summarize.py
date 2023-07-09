import openai
import os

MAX_TOKENS = 512

openai.api_key = os.environ.get("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("Environment variable OPENAI_API_KEY not set")

def generate_summary(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # will need to replace with newest model as OpenAI updates their versions 
        messages=[
            {
                "role": "system",
                "content": "You are a research assistant with expertise in conducting literature reviews."
            },
            {"role": "user", "content": prompt}
        ],
        max_tokens=MAX_TOKENS,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message_with_summary = response['choices'][0]['message']['content']
    return message_with_summary
