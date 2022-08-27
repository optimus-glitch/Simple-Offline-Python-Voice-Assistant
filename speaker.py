import pyttsx3


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()

    def init_engine(self, gender="f"):
        """
        Intitialize an engine for audio output.
        params: gender: str - gender voice the engine will use to speak.
        default gender: female, options: "male","m" or "female", "f"
        """
        voices = self.engine.getProperty("voices")
        self.engine.setProperty("rate", 155)
        if gender.lower() == "f" or gender.lower() == "female":
            self.engine.setProperty("voice", voices[1].id)
        elif gender == "m" or gender == "male":
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, message: str, gender="f"):
        self.init_engine(gender)
        self.engine.say(message)
        self.engine.runAndWait()
