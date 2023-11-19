import re
from src.dto.regex_dto import RegexDto, SSRDto


class Interface:
    def PatternSearch(self, _: RegexDto):
        pass

    def SSRPatternSearch(self, _: SSRDto):
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

    def SSRPatternSearch(self, dto: SSRDto):
        ssr = []

        data = dto.data
        repeat_length = int(dto.repeat_length)

        pattern = f"({'A+'}|{'T+'}|{'C+'}|{'G+'}){{{repeat_length},}}"
        matches = re.finditer(pattern, data)

        for match in matches:
            ssr.append(match.group())
        
        return ssr
