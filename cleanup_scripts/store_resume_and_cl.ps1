# PowerShell equivalent of store_resume_and_cl.sh

param(
    [string]$COMPANY_NAME,
    [string]$JOB_TITLE
)

# Get the current month and year in format %b-%Y
$MONTH_DATE = Get-Date -Format "MMM-dd-yyyy"
$DIR_PATH = "outputs\$MONTH_DATE\$COMPANY_NAME-$JOB_TITLE"
$INITIALS = "$($COMPANY_NAME.Substring(0,1))$($JOB_TITLE.Substring(0,1))"

# If the directory does not exist, create it
if (-not (Test-Path -Path $DIR_PATH)) {
    Write-Host "Creating Directory"
    New-Item -ItemType Directory -Path $DIR_PATH
}

# Copy Job Description to path outputs\Feb-2025\Qualcomm Canada ULC -Interim Engineering Intern - SW
Write-Host "Moving job description"
Copy-Item -Path "inputs\job_description.txt" -Destination $DIR_PATH

# Rename and move cover letter
Write-Host "Moving cover letter"
Rename-Item -Path "cover_letter.docx" -NewName "Sky_Quan_Cover_Letter_$INITIALS.docx"
Move-Item -Path "Sky_Quan_Cover_Letter_$INITIALS.docx" -Destination $DIR_PATH

# Rename and move resume
Write-Host "Moving resume"
Rename-Item -Path "resume.docx" -NewName "Sky_Quan_Resume_$INITIALS.docx"
Move-Item -Path "Sky_Quan_Resume_$INITIALS.docx" -Destination $DIR_PATH

# Copy Original Resume
Copy-Item -Path "resumes/Sky_Quan_Resume.docx" -Destination $DIR_PATH

Write-Host "Script completed successfully"