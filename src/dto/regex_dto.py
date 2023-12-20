from typing import Any


class SsrDTO:
    def __init__(self, json: Any) -> None:
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


class SSRResultDTO:
    def __init__(self, pattern: str, is_found: bool, count: int, position: list, timed: str = "") -> None:
        self.pattern = pattern
        if is_found == True:
            self.is_found = f"Pattern {self.pattern} ditemukan"
            self.count = count
            self.position = position
            self.timed = timed
        else:
            self.is_found = f"Pattern {self.pattern} tidak ditemukan"
            self.count = count
            self.position = []
            self.timed = timed

    def encode(self):
        return self.__dict__
