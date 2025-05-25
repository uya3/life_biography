from google import genai
from google.genai import types
from prompts import prompts_db

client = genai.Client(api_key="GEMINI_API_KEY")


def generate_summaries(uuid, bio):
    for prompt in prompts_db:
        if prompt['name'] == uuid:
            text = prompt['text']
            break

def generate_summary(uuid, bio, prompt):
    config=types.GenerateContentConfig(
        max_output_tokens=5000,
        temperature=0.1
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=config,
        contents=text,
    )
    return response.text


