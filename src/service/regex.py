import re
from src.dto.regex_dto import RegexDto


class Interface:
    def PatternSearch(self, dto: RegexDto):
        pass

class regexService(Interface):
    def PatternSearch(self, dto: RegexDto):
        data = dto.data
        sequence = dto.sequence

        matches = [match.start() for match in re.finditer(sequence, data)]

        if matches:
            print(f"Motif '{sequence}' found at positions: {matches}")
        else:
            print(f"Motif '{sequence}' not found in the DNA sequence.")
