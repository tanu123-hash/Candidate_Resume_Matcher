import requests
from bs4 import BeautifulSoup

# Define the URL
url = "https://huggingface.co/datasets/jacob-hugging-face/job-descriptions"

# Send a request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table containing job descriptions
    table = soup.find('table')
    
    # Loop through the rows of the table and extract job descriptions
    descriptions = []
    for row in table.find_all('tr'):
        cells = row.find_all('td')
        if len(cells) > 1:
            descriptions.append(cells[1].text.strip())
    
    # Print the job descriptions
    for idx, description in enumerate(descriptions):
        print(f"Job Description {idx + 1}:\n{description}\n")
else:
    print("Error: Unable to retrieve the webpage.")



# Save the job descriptions to a text file with UTF-8 encoding
with open('job_descriptions.txt', 'w', encoding='utf-8') as file:
    for description in descriptions:
        file.write(f"{description}\n")
