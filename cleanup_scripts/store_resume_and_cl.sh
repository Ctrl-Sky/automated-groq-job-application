#!/bin/bash

COMPANY_NAME="$1"
JOB_TITLE="$2"

MONTH_DATE=$(date +"%b-%d-%Y")
DIR_PATH="outputs/$MONTH_DATE/$COMPANY_NAME-$JOB_TITLE"
INITIALS="${COMPANY_NAME:0:1}${JOB_TITLE:0:1}"

# If dir does not exist, create it
if [ ! -d "$DIR_PATH" ]; then
    echo "Creating Directory"
    mkdir -p "$DIR_PATH"
fi

# Copy Job Description to path
echo "Moving job description"
cp inputs/job_description.txt "$DIR_PATH"

# Rename and move cover letter
echo "Moving Cover Letter"
mv cover_letter.docx "Sky_Quan_Cover_Letter_$INITIALS.docx"
mv "Sky_Quan_Cover_Letter_$INITIALS.docx" "$DIR_PATH"

# Rename and move resume
echo "Moving Resume"
mv resume.docx "Sky_Quan_Resume_$INITIALS.docx"
mv "Sky_Quan_Resume_$INITIALS.docx" "$DIR_PATH"

# Copy original resume
cp "resumes/Sky_Quan_Resume.docx" "$DIR_PATH"

echo "Script completed Successfully"