import json
import os
from google import genai
from google.genai import types
import prompts

# get GEMINI_API_KEY from environment variable
DEMO_MODE = False
# if GEMINI_API_KEY is not set, set demo mode to True
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", None)
if not GEMINI_API_KEY:
    print("GEMINI_API_KEY not found in environment variables. Running in demo mode.")
    DEMO_MODE = True
    # Set a dummy API key for demo purposes
    GEMINI_API_KEY = "dummy_key_for_demo"

client = genai.Client(api_key=GEMINI_API_KEY)
ACTIVE_PROMPTS = ['combined', 'short']

def generate_summaries(uuid, bio, actives=ACTIVE_PROMPTS):
    if DEMO_MODE:
        print("Running in demo mode. No API calls will be made.")
        # read response.json file content and return it
        with open('response.json', 'r') as f:
            return json.load(f)

    prompts.load_prompts()
    responses = {}
    for prompt in prompts.prompts_db:
        if prompt['name'] not in actives:
            continue
        responses[prompt['name']] = generate_summary(uuid, bio, prompt['text'])
    return responses

def generate_summary(uuid, bio, prompt):
    config=types.GenerateContentConfig(
        max_output_tokens=5000,
        temperature=0.1,
        response_mime_type="application/json",
    )
    contents = f'{prompt}: \n {bio}'
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=config,
        contents=contents,
    )

    return response.text
