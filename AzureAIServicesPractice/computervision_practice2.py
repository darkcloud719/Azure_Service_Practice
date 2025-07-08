import os
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv

def main():

    assert os.getenv("AZURE_AISERVICES_KEY"), "AZURE_AISERVICES_KEY is not set."
    assert os.getenv("AZURE_AISERVICES_ENDPOINT"), "AZURE_AISERVICES_ENDPOINT is not set."

    key = os.getenv("AZURE_AISERVICES_KEY")
    endpoint = os.getenv("AZURE_AISERVICES_ENDPOINT")

    image_analysis_client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    parent_dir = os.pardir
    target_file = os.path.join(parent_dir, "imgs","cat1.jpg")


    with open(target_file, "rb") as f:
        image_data = f.read()

    result = image_analysis_client.analyze(image_data=image_data, visual_features=[VisualFeatures.CAPTION])

    print("Image analysis results:")
    print("Captions:")
    if result.caption is not None:
        print(f" '{result.caption.text}', Confidence: {result.caption.confidence:.4f}")
        print(f"Image height: {result.metadata.height}")
        print(f"Image width: {result.metadata.width}")
        print(f"Model version: {result.model_version}")
    
if __name__ == "__main__":
    load_dotenv()
    main()

    
