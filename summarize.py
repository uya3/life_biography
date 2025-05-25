import os
from google import genai
from google.genai import types
import prompts

# get GEMINI_API_KEY from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

ACTIVE_PROMPTS = ['activity', 'short']

def generate_summaries(uuid, bio):
    prompts.load_prompts()
    responses = {}
    for prompt in prompts.prompts_db:
        if prompt['name'] not in ACTIVE_PROMPTS:
            continue
        responses[prompt['name']] = generate_summary(uuid, bio, prompt['text'])
    return responses

def generate_summary(uuid, bio, prompt):
    config=types.GenerateContentConfig(
        max_output_tokens=5000,
        temperature=0.1
    )
    contents = f'{prompt}: \n {bio}'
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=config,
        contents=contents,
    )
    return response.text
