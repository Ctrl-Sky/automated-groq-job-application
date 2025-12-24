import os
from dotenv import load_dotenv
from groq import Groq

def get_job_title():
    with open("inputs/job_description.txt", encoding="utf-8") as desc:
        job_desc = desc.read()

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = f"{job_desc} What is the job title? Only output the job title. For example, if you think the job title is Software Developer, only output Software Developer"

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content.strip())

if __name__=="__main__":
    load_dotenv()
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    get_job_title()