from pathlib import Path
import random
import subprocess
from speaker import Speaker
from checker import CheckCommand
from actions import Methods
from listener import Listener

model_path = f"{Path()}\\voice-model\\"
listener = Listener(model=model_path)
speaker = Speaker()
do_this = Methods()


# Mapping of tag from intents to a function in Methods class (actions.py)
mappings = {
    "add_todo": do_this.add_todo,
    "create_note": do_this.create_note,
    "show_todos": do_this.show_todos,
    "time": do_this.query_time,
    "query_day": do_this.day,
    "joke": do_this.joke,
    "exit": do_this.quit,
}


intents_file = Path("intents.json")

done = False
subprocess.call("cls", shell=True)

while not done:
    # Listen for commands
    data = listener.get_audio()  # Returns the word said by user
    data = data.lower().strip()

    print(f"You said: {data}")

    # Check if command exists in intents.json file patterns
    command_check = CheckCommand(filename=intents_file, user_command=data)

    command_tag = command_check.command_in_intent()[0]
    command_responses = command_check.command_in_intent()[1]

    if mappings.get(command_tag):
        mappings[command_tag]()

    elif command_tag != "misunderstood":
        if len(command_responses) > 0:
            random_response = random.randrange(
                start=0, stop=len(command_responses))
            command_response = command_responses[random_response]

        speaker.speak(command_response)

    else:
        continue
