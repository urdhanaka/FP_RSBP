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

    def test(self):
        print(self.data, " ", self.sequence)
