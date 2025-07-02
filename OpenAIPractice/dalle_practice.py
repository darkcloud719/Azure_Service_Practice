import os,requests,json,openai
from dotenv import load_dotenv
from PIL import Image

def main():
    
    assert os.getenv("DALLE_API_KEY"), "DALLE_API_KEY is not set."
    assert os.getenv("DALLE_ENDPOINT"), "DALLE_ENDPOINT is not set."
    assert os.getenv("OPENAI_API_VERSION"), "OPENAI_API_VERSION is not set."
    assert os.getenv("DALLE_ENDPOINT"), "AZURE_OPENAI_DEPLOYMENT_DALLE is not set."

    openai.api_key = os.getenv("DALLE_API_KEY")
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    openai.azure_endpoint = os.getenv("DALLE_ENDPOINT")
    openai.api_type = "azure"

    result = openai.images.generate(
        model = "dall-e-3",
        prompt = "一個人穿著西裝，在河邊裡跑步",
        n = 1
    )

    image_dir = os.path.join(os.pardir, "imgs")

    if not os.path.exists(image_dir):
        os.makedirs(image_dir)

    image_path = os.path.join(image_dir, "dalle3_result.png")

    image_url = result.data[0].url
    generated_image = requests.get(image_url).content
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)
    image= Image.open(image_path)
    image.show()

    # image_dir = os.path.join(os.curdir)

if __name__ == "__main__":
    load_dotenv()
    main()
    # print(os.curdir)