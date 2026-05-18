import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")


def get_ai_response(user_input):

    try:
        response = model.generate_content(user_input)
        return response.text

    except Exception as e:
        return f"AI Error: {str(e)}"
