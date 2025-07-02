import os,openai,base64
from rich import print as pprint
from dotenv import load_dotenv

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def main():
     
    assert os.getenv("OPENAI_API_KEY"), "OPENAI_API_KEY is not set."
    assert os.getenv("OPENAI_API_VERSION"), "OPENAI_API_VERSION is not set."
    assert os.getenv("AZURE_OPENAI_ENDPOINT"), "AZURE_OPENAI_ENDPOINT is not set."
    assert os.getenv("AZURE_OPENAI_DEPLOYMENT_4O"), "AZURE_OPENAI_DEPLOYMENT_4O is not set."

    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    openai.api_type = "azure"

    img = encode_image("../imgs/cat1.jpg")

    response = openai.chat.completions.create(
        model = os.getenv("AZURE_OPENAI_DEPLOYMENT_4O"),
        messages = [
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":[
                {"type":"text","text":"Please describe this image"},
                {"type":"image_url","image_url":{"url":f"data:image/jpeg;base64,{img}",}}
            ]}
        ],
        max_tokens=100
    )

    pprint(response.choices[0].message.content)

if __name__ == "__main__":
    load_dotenv()
    main()