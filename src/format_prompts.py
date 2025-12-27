from datetime import datetime
from textwrap import dedent

def get_resume_prompt():
    with open("inputs/job_description.txt", encoding="utf-8") as desc:
        job_desc = desc.read()
    with open("inputs/skillset.txt", encoding="utf-8") as skills:
        skillset = skills.read()
    with open("inputs/resume_template.txt", encoding="utf-8") as resume:
        resume_format = resume.read()
    
    resume_prompt = dedent(f"""\
        I will provide you with a job description, my skillset, and a resume template. Your task is to to map key-value pairs in my skillset to the resume template to best fit the job description.
        
        Do these when filling in the template:
        Generate the unqiue highlight of qualifications based on what you included in the resume. Do not copy exactly what is on the resume, include unqiue highlights based off of the info.
        Here is a good example. It highlights the skills I have based off of the information on my resume but does not list the exact job I did.
        Highlights of Qualifications
        - Expertise in developing and implementing CI/CD pipelines using Jenkins, GitHub Actions, Ansible, and SonarQube.
        - Proficient in database technologies including Snowflake, MSSQL, and Oracle
        - Hands-on experience with cloud infrastructure (AWS, Azure), Docker containerization, and scripting languages (Python), coupled with skills in data analysis using Pandas and NumPy.
        Under experience, there will be more than 3 points listed. Take the best 3 points that match the job description
        Do not shorten any of the points. Only include the full point and do not cut it off and summarise it. For example do not shorten:
        Developed an application integrating Google's Gemini 2.0 model with Python to optimize resumes based on job descriptions. The project then automatically generates a tailored cover letter based on the previous results, then stores the optimized resume and cover letter in a directory. All executed within a GitHub Actions workflow for scalability.
        to: Developed an application integrating Google's Gemini 2.0 model with Python to optimize resumes based on job descriptions.
        Follow the template exactly, do not add more points than needed. For example, the format list one course name and one course description. Only add one course from the skillset and not more.
        Finally, only output the resume. For example, do not output: “Ok here is the resume: [resume]”, only output “[resume]” Another example, do not include highlight of qualifications
        
        Here is the job description:
        {job_desc}

        Here is my skillset:
        {skillset}

        Here is the resume template:
        {resume_format}\
    """)
    return resume_prompt

def get_cl_prompt():
    with open("inputs/skillset.txt", encoding="utf-8") as skills:
        skillset = skills.read()
    today = datetime.today()
    cl_prompt = dedent(f"""\
        For the same job description, I want you to write a cover letter that is 225 words long using my skills
        {skillset}
        When writing the cover letter follow this format:
        {today:%B %d, %Y}
        Sky Quan
        Toronto, Ontario, Canada
        skyquan23@gmail.com
        647-613-7546

        Dear Hiring Team,
        [Opening Paragraph]
        [Body Paragraph]
        [Closing Paragraph]

        Sincerely,
        Sky Quan

        Here are the constraints when writing this cover letter.
        Do not include any information that you do not already have. For example, do not include a line like this: “I found this opening at [Platform where you saw the job posting].” 
        When writing the cover letter, always ensure that it would be able to fit into a single A4 piece of paper.
        Finally, only output the cover letter. For example, do not output: “Ok here is the cover letter: [cover letter]”, only output “[cover letter]”
    """)
    return cl_prompt