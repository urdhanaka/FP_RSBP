class RegexDto:
    def __init__(self, json) -> None:
        self.data = ""
        self.sequence = ""

        if "data" in json:
            self.data = json["data"]

        if "sequence" in json:
            self.sequence = json["sequence"]

    def is_valid(self) -> bool:
        if self.data == "":
            return False 
        elif self.sequence == "":
            return False
        else:
            return True

class SSRDto:
    def __init__(self, json) -> None:
        self.data = ""
        self.repeat_length = ""

        if "data" in json:
            self.data = json["data"]

        if "repeat_length" in json:
            self.repeat_length = json["repeat_length"]

    def is_valid(self) -> bool:
        if self.data == "":
            return False 
        if self.repeat_length == "":
            return False 
        else:
            return True
