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


class SsrDTO:
    def __init__(self, json) -> None:
        self.sequence = ""
        self.pattern = []

        if "sequence" in json:
            self.sequence = json["sequence"]

        if "pattern" in json:
            if isinstance(json["pattern"], list):
                for pattern in json["pattern"]:
                    self.pattern.append(pattern)
            else:
                self.pattern.append(json["pattern"])

    def is_valid(self) -> bool:
        if self.sequence == "" or self.pattern == []:
            return False

        return True


class ResponseSSRDTO:
    def __init__(self) -> None:
        self.result = {}

    def is_valid(self) -> bool:
        if self.result == {}:
            return False

        return True


class SSRResultDTO:
    def __init__(self, pattern: str, is_found: bool, count: int, ssr: list) -> None:
        self.pattern = pattern
        if is_found == True:
            self.is_found = f"Pattern {self.pattern} ditemukan"
            self.count = count
            self.ssr = ssr
        else:
            self.is_found = f"Pattern {self.pattern} tidak ditemukan"
            self.count = count
            self.ssr = []

    def encode(self):
        return self.__dict__
