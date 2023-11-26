import re
from typing import Any
from src.dto.regex_dto import SSRDTO, RegexDTO, ResponseSSRDTO


class Interface:
    def PatternSearch(self, _: RegexDTO):
        pass

    def SSRSearch(self, _: SSRDTO):
        pass


class regexService(Interface):
    def PatternSearch(self, dto: RegexDTO):
        data = dto.data
        sequence = dto.sequence

        matches = [match.start() for match in re.finditer(sequence, data)]

        if matches:
            print(f"Motif '{sequence}' found at positions: {matches}")
        else:
            print(f"Motif '{sequence}' not found in the DNA sequence.")

    # temp, might delete soon
    def SSRSearch(self, dto: SSRDTO):
        def ssrPatternSearch(sequence: str, length: int) -> list[Any]:
            pattern = rf"(\w{{{length},{length}}})(?:\1)+"
            matches = re.findall(pattern, sequence)

            return matches

        resp = ResponseSSRDTO()
        sequence = dto.sequence
        resultDict = {}

        # Make SSR search length max to 6
        for i in range(2, 7):
            res = ssrPatternSearch(sequence, i)
            resultDict[str(i)] = res

        resp.result = resultDict

        return resp

    def PatternSSRSearch(self, dto: SSRDTO):
        def ssrPatternSearch(sequence: str, pattern: str):
            matches = re.findall(pattern, sequence)

            return matches

        sequence = dto.sequence
        resultList = []

        for pattern in dto.pattern:
            res = ssrPatternSearch(sequence, pattern)
            resultList.append(res)

        return resultList
