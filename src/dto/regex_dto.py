class RegexDTO:
    def __init__(self, json) -> None:
        self.data = ""
        self.sequence = ""

        if "data" in json:
            self.data = json["data"]

        if "sequence" in json:
            self.sequence = json["sequence"]

    def is_valid(self) -> bool:
        if self.data == "" or self.sequence == "":
            return False

        return True


class SSRDTO:
    def __init__(self, json) -> None:
        self.sequence = ""

        if "sequence" in json:
            self.sequence = json["sequence"]

    def is_valid(self) -> bool:
        if self.sequence == "":
            return False

        return True


class ResponseSSRDTO:
    def __init__(self) -> None:
        self.result = {}

    def is_valid(self) -> bool:
        if self.result == {}:
            return False

        return True
