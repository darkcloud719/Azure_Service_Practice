import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

def recognize_from_microphone():

    assert os.getenv("AZURE_AISERVICES_KEY"), "AZURE_AISERVICES_KEY is not set."
    assert os.getenv("AZURE_AISERVICES_ENDPOINT"), "AZURE_AISERVICES_ENDPOINT is not set."

    speech_key = os.getenv("AZURE_AISERVICES_KEY")
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=os.getenv("AZURE_AISERVICES_ENDPOINT"))

    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Please speak into the microphone.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print(f"Recognized: {speech_recognition_result.text}")
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print(f"No speech could be recognized:{speech_recognition_result.no_match_details}")
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print(f"Speech Recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error detials: {cancellation_details.error_details}")
            print("Did you set the speech resource key and region values?")

def main():
    recognize_from_microphone()

if __name__ == "__main__":
    load_dotenv()
    main()
