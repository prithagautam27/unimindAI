import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def get_gemini_response(message: str):

    if message.lower() in ["hi", "hello", "hey"]:
        return "Hi! I'm UniMind AI 👋 How can I help you today?"


    prompt = f"""
You are UniMind AI, a university support chatbot.

Rules:
- Keep answers under 80 words.
- Answer like a chat assistant.
- Use simple language.
- Do not write essays.
- Use bullet points only when necessary.
- If information is unknown, ask a follow-up question.

User Question:
{message}
"""

    response = model.generate_content(prompt)

    return response.text