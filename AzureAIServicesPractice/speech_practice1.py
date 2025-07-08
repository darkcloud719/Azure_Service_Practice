import os
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv

def text_to_speech():

    assert os.getenv("AZURE_AISERVICES_KEY"), "AZURE_AISERVICES_KEY is not set in the environment variables"
    assert os.getenv("AZURE_AISERVICES_ENDPOINT"), "AZURE_AISERVICES_ENDPOINT is not set in the environment variables"
    assert os.getenv("AZURE_AISERVICES_REGION"), "AZURE_AISERVICES_REGION is not set in the environment variables"

    speech_key = os.getenv("AZURE_AISERVICES_KEY")
    speech_region = os.getenv("AZURE_AISERVICES_REGION")
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, endpoint=os.getenv("AZURE_AISERVICES_ENDPOINT"))

    speech_config.speech_synthesis_voice_name = "zh-TW-YunJheNeural"
    # speech_config.speech_synthesis_voice_name = "zh-TW-HsiaoChenNeural"
    # speech_config.speech_synthesis_voice_name = "en-US-AriaNeural"

    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    result = synthesizer.speak_text_async("今天你好嗎?").get()
    # result = synthesizer.speak_text_async("How are you today?").get()
    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesis completed.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.error_details:
            print(f"Error details: {cancellation_details.error_details}")

def main():
    text_to_speech()

if __name__ == "__main__":
    load_dotenv()
    main()