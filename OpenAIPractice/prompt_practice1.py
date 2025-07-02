import openai
import os
from dotenv import load_dotenv
from rich import print as pprint

def main():

    assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY is not set."
    assert os.getenv("OPENAI_API_VERSION"), "OPENAI_API_VERSION is not set."
    assert os.getenv("AZURE_OPENAI_ENDPOINT"), "AZURE_OPENAI_ENDPOINT is not set."
    assert os.getenv("AZURE_OPENAI_DEPLOYMENT_4O"), "AZURE_OPENAI_DEPLOYMENT_4O is not set."

    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_type = "azure"

    response = openai.chat.completions.create(
        model = os.getenv("AZURE_OPENAI_DEPLOYMENT_4O"),
        messages = [
            {"role":"system","content":"You are a professional translator. Your task is to translate any English text accurate and natural Mandariin Chinese."},
            {"role":"user","content":"What is the highest mountain in the world?"}
        ]
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    load_dotenv()
    main()