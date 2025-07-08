import os
import time
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

def recognize_from_microphone_continuous():

    assert os.getenv("AZURE_AISERVICES_KEY"), "AZURE_AISERVICES_KEY is not set."
    assert os.getenv("AZURE_AISERVICES_ENDPOINT"), "AZURE_AISERVICES_ENDPOINT is not set."

    speech_key = os.getenv("AZURE_AISERVICES_KEY")
    service_endpoint = os.getenv("AZURE_AISERVICES_ENDPOINT")

    speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=service_endpoint)
    speech_config.speech_recognition_language = "en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    def recognized_handler(evt):
        if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print(f"[Recognized] {evt.result.text}")
        elif evt.result.reason == speechsdk.ResultReason.NoMatch:
            print("[NoMatch] Speech could not be recognized.")

    def canceled_handler(evt):
        print(f"[Canceled] REason: {evt.reason}")
        if evt.reason == speechsdk.CancellationReason.Error:
            print(f"[Error] {evt.error_details}")

    speech_recognizer.recognized.connect(recognized_handler)
    speech_recognizer.canceled.connect(canceled_handler)

    print("Start speaking...(press Ctrl+C to stop)")
    speech_recognizer.start_continuous_recognition()

    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Stopping recognition...")
        speech_recognizer.stop_continuous_recognition()
        print("stopped.")

def main():
    recognize_from_microphone_continuous()

if __name__ == "__main__":
    load_dotenv()
    main()