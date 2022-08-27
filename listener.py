from vosk import Model, KaldiRecognizer
import pyaudio
from speaker import Speaker
import sys


class Listener:
    """
        Parameters: path to voice model folder.. e.g listener = Listener("PathToModel")\n
        default model is "vosk-model-small-en-us-0.15" downloaded from vosk website\n
        Provides Offline speech recognition functionality.\n
        Returns speech from user as a string\n
    """

    def __init__(self, model):
        self.model_path = model
        self.model = Model(self.model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.speaker = Speaker()

    def get_audio(self):
        try:
            cap = pyaudio.PyAudio()
            stream = cap.open(
                format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=8192,
            )

            # Recognize from mic
            triggered = True
            print("\nListening...")
            stream.start_stream()
            while triggered:
                data = stream.read(8192)
                if self.recognizer.AcceptWaveform(data):
                    said = (
                        self.recognizer.Result()
                        .splitlines()[1]
                        .split(sep=":")[1]
                        .strip()
                        .strip('"')
                    )

                    said = str(said).lower()

                    if len(said) > 0:
                        triggered = False

            return said
        except OSError:
            self.speaker.speak(
                "Oops. An error ocuured. I'm leaving now"
            )
            sys.exit(0)
