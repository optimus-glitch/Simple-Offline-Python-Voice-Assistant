import json


class CheckCommand:
    """
        Checks if speech from speaker matches any pattern in the intents.json file.\n
        Parameters: \tfilename --> Give path to intents.json file , user_command --> Speech/word from user
        Returns: list with [commmand-tag, responses-to-that-command]
    """

    def __init__(self, filename: str, user_command: str):
        self.filename = filename
        self.user_command = user_command

    def command_in_intent(self):
        with open(file=self.filename) as f:
            data = json.load(f)

        ls = data["intents"]
        word = self.user_command.lower().strip()
        done = False

        while not done:
            for item in range(len(ls)):
                pattern_list = ls[item]["patterns"]
                for i in range(len(pattern_list)):
                    wrd = pattern_list[i].lower()

                    if word in wrd:
                        command_tag = ls[item]["tag"]
                        command_response = ls[item]["responses"]
                        command_tag_response = []
                        command_tag_response.append(command_tag)
                        command_tag_response.append(command_response)

                        return command_tag_response

            command_tag = "misunderstood"
            command_response = ["I did not understand"]
            command_tag_response = []
            command_tag_response.append(command_tag)
            command_tag_response.append(command_response)
            done = True

        return command_tag_response
