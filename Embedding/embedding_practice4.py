import numpy as np
import openai
import os
from rich import print as pprint
from openai import AzureOpenAI
from dotenv import load_dotenv

def cosine_similarity(a,b):
    a = np.array(a)
    b = np.array(b)

    dot_product = np.dot(a,b)

    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)

    if norm_a == 0 or norm_b == 0:
        return 0.0
    
    return dot_product / (norm_a * norm_b)

def main():

    assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY is not set."
    assert os.getenv("OPENAI_API_VERSION"), "OPENAI_API_VERSION is not set."
    assert os.getenv("AZURE_OPENAI_ENDPOINT"), "AZURE_OPENAI_ENDPOINT is not set."
    assert os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"), "AZURE_OPENAI_EMBEDDING_DEPLOYMENT is not set."

    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_type = "azure"

    response = openai.embeddings.create(
        model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        input = ["apple","bicycle","doctor","蘋果","ghost"]
    )

    apple_embedding = response.data[0].embedding
    bicycle_embedding = response.data[1].embedding
    doctor_embedding = response.data[2].embedding
    chinese_apple_embedding = response.data[3].embedding
    ghost_embedding = response.data[4].embedding

    print(f"Apple vs Bicycle: {cosine_similarity(apple_embedding, bicycle_embedding)}")
    print(f"Apple vs Doctor: {cosine_similarity(apple_embedding, doctor_embedding)}")
    print(f"Apple vs Chinese Apple: {cosine_similarity(apple_embedding, chinese_apple_embedding)}")
    print(f"Apple vs Ghost: {cosine_similarity(apple_embedding, ghost_embedding)}")

if __name__ == "__main__":
    load_dotenv()
    main()