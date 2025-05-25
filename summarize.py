from google import genai
from prompts import prompts_db

client = genai.Client(api_key="GEMINI_API_KEY")

def generate_summary(uuid, text):
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text,
    )
    return response.text


