import PyPDF2
import re

def extract_details(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        return text

def extract_category(text):
    pattern = r'(?:[Cc]ategory)[:\s]*(.+?)(?=\n|\r|\Z)'
    matches = re.findall(pattern, text)
    return matches[0].strip() if matches else None

def extract_skills(text):
    pattern = r'(?:[Ss]kills|[Qq]ualifications)[:\s]*(.+?)(?=\n|\r|\Z)'
    matches = re.findall(pattern, text)
    return [skill.strip() for skill in matches[0].split(',') if skill.strip()] if matches else None

def extract_education(text):
    pattern = r'(?:[Ee]ducation|[Qq]ualifications)[:\s]*(.+?)(?=\n|\r|\Z)'
    matches = re.findall(pattern, text)
    return [edu.strip() for edu in matches[0].split(',') if edu.strip()] if matches else None

# Example Usage:
pdf_path = 'C:/python projects/resume_p/archive/UpdatedResumeDataSet.pdf'
pdf_text = extract_details(pdf_path)

category = extract_category(pdf_text)
skills = extract_skills(pdf_text)
education = extract_education(pdf_text)

if category:
    print("Category:", category)
else:
    print("Category not found.")

if skills:
    print("Skills:", skills)
else:
    print("Skills not found.")

if education:
    print("Education:", education)
else:
    print("Education not found.")


# Save the results to a text file
with open('cv_details.txt', 'w') as file:
    file.write(f"Category: {category}\n")
    file.write(f"Skills: {', '.join(skills)}\n")
    file.write(f"Education: {', '.join(education)}\n")