import os,json,sys
from dotenv import load_dotenv
from azure.ai.translation.text import TextTranslationClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.text.models import InputTextItem
from azure.core.exceptions import HttpResponseError

def main():

    assert os.getenv("AZURE_AISERVICES_KEY"), "AZURE_AISERVICES_KEY is not set."
    assert os.getenv("AZURE_AISERVICES_ENDPOINT"), "AZURE_AISERVICES_ENDPOINT is not set."
    assert os.getenv("AZURE_AISERVICES_REGION"), "AZURE_AISERVICES_REGION is not set."

    key = os.getenv("AZURE_AISERVICES_KEY")
    endpoint = os.getenv("AZURE_AISERVICES_ENDPOINT")
    region = os.getenv("AZURE_AISERVICES_REGION")
    credential = AzureKeyCredential(key)

    text_translation_client = TextTranslationClient(endpoint=endpoint, credential=credential, region=region)

    try:
        source_language = "en"
        target_language = ["zh-Hans", "ja"]
        input_text_elements = [InputTextItem(text="I am a software engineer")]

        response = text_translation_client.translate(body=input_text_elements, to_language=target_language, from_language=source_language)
        translation = response[0] if response else None
        if translation:
            for translated_text in translation.translations:
                print(f"Text was translated to {translated_text.to} and the result is: {translated_text.text}")
    except HttpResponseError as exception:
        print(f"Error Code: {exception.error.code}")
        print(f"Error Message: {exception.error.message}")

if __name__ == "__main__":
    load_dotenv()
    main()