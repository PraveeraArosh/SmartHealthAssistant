from openai import OpenAI
import os

from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_chatbot_response(symptoms):
    if not symptoms:
        return "Please describe your symptoms."
    prompt = f"You are a health assistant. Based on the following symptoms: {symptoms}, suggest possible causes, preliminary evaluations, and diagnostic tests. Note: This is not a substitute for professional medical advice."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    return response.choices[0].message.content