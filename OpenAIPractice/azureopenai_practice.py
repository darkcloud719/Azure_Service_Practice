import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from rich import print as pprint

def main():

    assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY is not set."
    assert os.getenv("OPENAI_API_VERSION"), "OPENAI_API_VERSION is not set."
    assert os.getenv("AZURE_OPENAI_ENDPOINT"), "AZURE_OPENAI_ENDPOINT is not set."
    assert os.getenv("AZURE_OPENAI_DEPLOYMENT_4O"), "AZURE_OPENAI_DEPLOYMENT_4O is not set."

    client = AzureOpenAI(
        api_version = os.getenv("OPENAI_API_VERSION"),
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key = os.getenv("OPENAI_API_KEY")
    )

    response = client.chat.completions.create(
        messages = [
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":"I am going to Paris, what should I see?"}
        ],
        # Set the maximum number of tokens for the response
        max_tokens=4096,
        # Set the temperature for randomness in the response
        temperature=1.0,
        # Set the top_p for nucleus sampling
        top_p=1.0,
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_4O"),
    )

    pprint(response.choices[0].message.content)

if __name__ == "__main__":
    load_dotenv()
    main()