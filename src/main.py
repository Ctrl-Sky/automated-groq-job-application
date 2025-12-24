import format_prompts
import helpers
import os

from dotenv import load_dotenv
from groq import Groq

def generate_resume_and_cl():
    # Get resume and cover letter prompt
    resume_prompt = format_prompts.get_resume_prompt()
    cl_prompt = format_prompts.get_cl_prompt()

    # Create conversation with gemini model
    client = Groq(api_key=GROQ_API_KEY)
    chat = client.chats.create(model="gemini-2.0-flash")

    # Get resume and write to docx
    print("Generating Resume...")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": resume_prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    print("Successfully Created Resume\n")
    helpers.formatted_text_to_docx(chat_completion.choices[0].message.content, "resume.docx")

    # Get cover letter and write to docx
    print("Generating Cover Letter...")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": cl_prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    print("Successfully Created Cover Letter\n")
    helpers.formatted_text_to_docx(chat_completion.choices[0].message.content, "cover_letter.docx")


if __name__=="__main__":
    # Load and get environment variables from .env
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    generate_resume_and_cl()

