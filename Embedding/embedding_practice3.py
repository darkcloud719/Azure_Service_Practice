import os 
import openai
from dotenv import load_dotenv
from rich import print as pprint
from openai import AzureOpenAI

def main():

    assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY is not set."
    assert os.getenv("OPENAI_API_VERSION"), "OPENAI_API_VERSION is not set."
    assert os.getenv("AZURE_OPENAI_ENDPOINT"), "AZURE_OPENAI_ENDPOINT is not set."
    assert os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"), "AZURE_OPENAI_EMBEDDING_DEPLOYMENT is not set."

    client = AzureOpenAI(
        api_key = os.getenv("OPENAI_API_KEY"),
        api_version = os.getenv("OPENAI_API_VERSION"),
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    )

    response = client.embeddings.create(
        model = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT"),
        input = ["Apple"]
    )

    pprint(response.data[0].embedding)

if __name__ == "__main__":
    load_dotenv()
    main()