import os
from dotenv import load_dotenv
from groq import Groq

def get_company_name():
    with open("inputs/job_description.txt", encoding="utf-8") as desc:
        job_desc = desc.read()

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    prompt = f"{job_desc} What is the company name? Only output the company name. For example, if you think the company name is Amazon, only output Amazon"

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
    GROQ_API_TOKEN=os.getenv("GROQ_API_TOKEN")
    get_company_name()