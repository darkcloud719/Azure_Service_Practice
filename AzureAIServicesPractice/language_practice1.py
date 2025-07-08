import os,json,sys
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def main():

    assert os.getenv("AZURE_AISERVICES_KEY"), "AZURE_AISERVICES_KEY is not set."
    assert os.getenv("AZURE_AISERVICES_ENDPOINT"), "AZURE_AISERVICES_ENDPOINT is not set."
    assert os.getenv("AZURE_AISERVICES_REGION"), "AZURE_AISERVICES_REGION is not set."

    key = os.getenv("AZURE_AISERVICES_KEY")
    endpoint = os.getenv("AZURE_AISERVICES_ENDPOINT")
    region = os.getenv("AZURE_AISERVICES_REGION")

    text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key), region=region)

    documents = ["My life is tough.", "我的生活像一坨屎"]

    result = text_analytics_client.analyze_sentiment(documents=documents, show_opinion_mining=True)

    docs = [doc for doc in result if not doc.is_error]

    print("Let's visualize the sentiment of each of these documents")

    for idx, doc in enumerate(docs):
        print(f"Document text: {documents[idx]}")
        print(f"Overall sentiment: {doc.sentiment}")
        print(f"Positive score: {doc.confidence_scores.positive}")
        print(f"Neutral score: {doc.confidence_scores.neutral}")
        print(f"Negative score: {doc.confidence_scores.negative}")

    print(result)

if __name__ == "__main__":
    load_dotenv()
    main()
