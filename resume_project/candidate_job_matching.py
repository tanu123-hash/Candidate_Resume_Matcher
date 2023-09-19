import torch
from transformers import DistilBertTokenizer, DistilBertModel
from sklearn.metrics.pairwise import cosine_similarity

# Load CV details and job descriptions (assuming you've already loaded them)
with open('cv_details.txt', 'r') as file:
    cv_details = file.read()

with open('job_descriptions.txt', 'r') as file:
    job_descriptions = file.read().splitlines()

# Preprocess CV details and job descriptions
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertModel.from_pretrained('distilbert-base-uncased')

cv_tokens = tokenizer(cv_details, return_tensors="pt", padding=True, truncation=True)
cv_embeddings = model(**cv_tokens).last_hidden_state.mean(dim=1)

job_description_tokens = [tokenizer(desc, return_tensors="pt", padding=True, truncation=True) for desc in job_descriptions]
job_description_embeddings = [model(**tokens).last_hidden_state.mean(dim=1) for tokens in job_description_tokens]

# Rest of your code remains the same...

print("CV Tokens:", cv_tokens)
print("CV Embeddings:", cv_embeddings)


# Calculate Cosine Similarity and Rank CVs
similarities = [cosine_similarity(job_description_embeddings[i], cv_embeddings) for i in range(len(job_descriptions))]
top_cvs_indices = [sim.argsort(axis=1)[:, -5:][:, ::-1] for sim in similarities]

print("Cosine Similarities:", similarities)
print("Top CVs Indices:", top_cvs_indices)


# Prepare the results
results = []

for i, desc in enumerate(job_descriptions):
    top_cvs = []
    for idx in top_cvs_indices[i]:
        top_cvs.append(f"CV {idx + 1} - Similarity Score: {similarities[i][0, idx]}")
    results.append(f"Top CVs for Job Description {i + 1}:\n" + "\n".join(top_cvs))

# Write results to a text file
with open('matching_results.txt', 'w') as file:
    file.write('\n\n'.join(results))
