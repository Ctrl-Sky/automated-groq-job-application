# Gemini-Job-Application-Generator

## Overview
This project automates the job application process using Google’s Gemini-2.0 and GitHub Actions. Taking a job description and your resume, the model provides suggestions for your resume, suggesting relevant points that best match the job.

With these suggestions, the model then helps in generating ideas and key content for a cover letter. The resulting resume and cover letter drafts are then saved as a .docx file for editing and personalization.

All generated content is stored in the hidden `outputs` directory, so you can revisit and track your job applications over time. Additionally, the system logs each interaction in a CSV file, providing a record of the jobs you've applied to with this automation.

## How to use
This project takes 3 parameters within the inputs directory.
- `job_description.txt` contains the job opening's description
- `resume_template.txt` this is the template the model will follow when generating the resume
- `skillset.txt` contains key=value pairs matching the resume template representing all the possible skills the model will choose from to include in the resume

If you're on linux, to run locally:
`bash execute_application.sh`

If you're on windows, to run locally:
`.\execute_application.ps1`

The .docx files will be written to `outputs/<day_applied>/<company_name>-<job_title>` and the csv file will be updated at `outputs`

## Technologies Used
- Google's Gemini 2.0 Flash model
- Python
- Shell
- Powershell
- GitHub Actions
