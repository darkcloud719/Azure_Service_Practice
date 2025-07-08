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
        input_text_elements = [InputTextItem(text="I am a software engineer.")]
        target_languages = ["zh-Hans","ja","fr"]

        for lang in target_languages:
            response = text_translation_client.translate(body=input_text_elements, to_language=[lang])

            translation = response[0] if response else None
            if translation:
                print(f"[{lang}] Detected Language: {translation.detected_language.language}")
                for t in translation.translations:
                    print(f" -> {t.text}")
    except HttpResponseError as exception:
        print(f"Error Code:{exception.error.code}")
        print(f"Error Message:{exception.error.message}")

if __name__ == "__main__":
    load_dotenv()
    main()
