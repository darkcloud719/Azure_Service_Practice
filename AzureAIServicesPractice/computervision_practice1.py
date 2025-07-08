import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

def main():

    assert os.getenv("AZURE_AISERVICES_KEY"), "AZURE_AISERVICES_KEY is not set."
    assert os.getenv("AZURE_AISERVICES_ENDPOINT"), "AZURE_AISERVICES_ENDPOINT is not set."

    try:
        endpoint = os.getenv("AZURE_AISERVICES_ENDPOINT")
        key = os.getenv("AZURE_AISERVICES_KEY")
    except KeyError as e:
        print(f"Missing environment variable 'AZURE_AISERVICES_KEY' or 'AZURE_AISERVICES_ENDPOINT'")
        print("Set them before running this sample")
        exit()

    image_analysis_client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    result = image_analysis_client.analyze_from_url(
        image_url="https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png",
        visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ]
    )

    print("Image analysis results:")

    print("Captions:")
    if result.caption is not None:
        print(f" '{result.caption.text}', Confidence: {result.caption.confidence:.4f}")

    print("Read:")

    if result.read is not None:
        for line in result.read.blocks[0].lines:
            print(f" Line: {line.text}, Bounding box: {line.bounding_polygon}")
            for word in line.words:
                print(f"Word: {word.text}, Bounding polygon {word.bounding_polygon}, Confidence: {word.confidence:.4f}")

if __name__ == "__main__":
    load_dotenv()
    main()