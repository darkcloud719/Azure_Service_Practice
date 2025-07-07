import os,json,openai,pyaudio,wave
from dotenv import load_dotenv
from rich import print as pprint
from rich.console import Console
from rich.table import Table

console = Console()


# def record_audio(duration=5, rate=44100, channels=2, chunk=1024):
def record_audio(duration=5, rate=16000, channels=1, chunk=1024, device_index=18):

    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=pyaudio.paInt16,
                        channels=channels,
                        rate=rate,
                        input=True,
                        input_device_index=device_index,
                        frames_per_buffer=chunk
                        )
        
        print("Recording...")
        frames = []
        for i in range(0, int(rate / chunk * duration)):
            data = stream.read(chunk)
            frames.append(data)

        print("Finished recording...")
    except Exception as e:
        print(f"Error occurred while setting up the audio stream: {e}")
    finally:
        if 'stream' in locals():
            stream.stop_stream()
            stream.close()
        p.terminate()
    
    audio_data = b''.join(frames)
    return audio_data

def save_as_wav(audio_data, filename="recorded_audio.wav", rate=16000, channels=1):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(audio_data)
    print(f"Audio saved as '{filename}'")

# def list_audio_devices():

#     table = Table(title="Audio Devices")
#     table.add_column("Index", style="cyan", justify="right")
#     table.add_column("Content", style="magenta")

#     p = pyaudio.PyAudio()
#     device_count = p.get_device_count()
#     for i in range(device_count):
#         # table.add_row(str(i), p.get_device_info_by_index(i).get('name', 'Unkown Device'))
#         # table.add_row(str(i), p.get_device_info_by_index(i))
#         print(p.get_device_info_by_index(i))
#     p.terminate()

#     console.print(table)

def list_audio_devices():

    table = Table(title="Audio Devices")
    table.add_column("Index", style="cyan", justify="right")
    table.add_column("Name", style="magenta")
    table.add_column("Input Channels", style="green", justify="right")
    table.add_column("Output Channels", style="green", justify="right")
    table.add_column("Default Sample Rate", style="blue", justify="right")

    p = pyaudio.PyAudio()
    device_count = p.get_device_count()
    for i in range(device_count):
        info = p.get_device_info_by_index(i)
        table.add_row(
            str(i),
            info.get("name","Unknown Device"),
            str(info.get("maxInputChannels", 0)),
            str(info.get("maxOutputChannels", 0)),
            str(int(info.get("defaultSampleRate", 0)))
        )
    p.terminate()
    console.print(table)

def recognize_audio_by_whisper(filename):
    with open(filename, "rb") as audio_file:
        result = openai.audio.transcriptions.create(
            model = "whisper",
            file = audio_file
        )

    pprint(result)

def main():

    assert os.getenv("WHISPER_API_KEY"), "WHISPER_API_KEY is not set."
    assert os.getenv("WHISPER_ENDPOINT"), "WHISPER_ENDPOINT is not set."
    assert os.getenv("OPENAI_API_VERSION"), "OPENAI_API_VERSION is not set."
    assert os.getenv("WHISPER_MODEL_NAME"), "WHISPER_MODEL_NAME is not set."

    openai.api_key = os.getenv("WHISPER_API_KEY")
    openai.api_version = os.getenv("OPENAI_API_VERSION")
    openai.azure_endpoint = os.getenv("WHISPER_ENDPOINT")
    openai.api_type = "azure"

    audio_data = record_audio(duration=5)
    print(f"Auto data length: {len(audio_data)} bytes")

    save_as_wav(audio_data)

    recognize_audio_by_whisper("recorded_audio.wav")

    # list_audio_devices()

if __name__ == "__main__":
    load_dotenv()
    main()



