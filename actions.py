import datetime
from pathlib import Path
from speaker import Speaker
import sys
import pyjokes
import subprocess
from listener import Listener


model_path = f"{Path()}\\voice-model\\"
speaker = Speaker()
listener = Listener(model=model_path)


class Methods:
    def __init__(self):
        self.todo_list = ["Do some coding"]

    def create_note(self):
        done = False

        while not done:
            try:
                speaker.speak("What do you want to write on your note?")
                note = listener.get_audio()
                note = note.lower()

                speaker.speak("Choose a file name")
                filename = listener.get_audio()
                filename = filename.lower()

                with open(f"{filename}.txt", "w") as f:
                    f.write(note)
                    done = True
                    speaker.speak(
                        f"I Successfully created the note {filename}")
            except:
                speaker.speak("I did not understand you. Try again")

    def add_todo(self):
        speaker.speak("What do you want to add?")
        done = False
        while not done:
            try:
                speaker.speak("What do you want to write on your note?")
                item = listener.get_audio()
                item = item.lower()

                self.todo_list.append(item)
                done = True
                speaker.speak(f"I added {item} to the to do list")

            except:
                speaker.speak("I did not understand. Please try again")

    def show_todos(self):
        speaker.speak(f"Your todo list has the following")
        for item in self.todo_list:
            speaker.speak(item)

    def know_me():
        pass

    def day(self):
        tday = datetime.date.today()
        weekday = tday.weekday()
        mapping = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        day = mapping[weekday]

        speaker.speak(f"Today is {day}")

    def query_time(self):
        tnow = datetime.datetime.now()
        hour = tnow.hour
        mins = tnow.minute
        pm = False

        if hour > 12:
            hour = round(hour - 12)
            pm = True
        if pm:
            if mins < 10:
                speaker.speak(f"It is now {str(hour)} o{str(mins)} pm")
            else:
                speaker.speak(f"It is now {str(hour)} {str(mins)} pm")
        else:
            if mins < 10:
                speaker.speak(f"It is now {str(hour)} o{str(mins)} am")
            else:
                speaker.speak(f"It is now {str(hour)} {str(mins)} am")

    def joke(self):
        jk = pyjokes.get_joke()
        print(jk)
        speaker.speak(jk)

    def quit(self):
        speaker.speak("Nice Talk.")
        subprocess.call("cls", shell=True)
        sys.exit(0)


if __name__ == "__main__":
    speaker.speak("Hey There.")
