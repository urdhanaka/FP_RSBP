import regex as re
from typing import Any
from src.dto.regex_dto import SsrDTO, RegexDTO, ResponseSSRDTO, SSRResultDTO


class Interface:
    def PatternSearch(self, _: RegexDTO):
        pass

    def SSRSearch(self, _: SsrDTO):
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
    def SSRSearch(self, dto: SsrDTO):
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

    def PatternSSRSearch(self, dto: SsrDTO):
        def ssrPatternSearch(sequence: str) -> list:
            final_matches = []

            for i in range(1, len(sequence)):
                pattern = rf"(\w{{{i},{i}}})(?:\1)+"
                matches = re.findall(pattern, sequence, overlapped=True)

                for ssr in matches:
                    final_matches.append(ssr)

            return final_matches

        def isPatternFound(sequence: str, pattern: str) -> bool:
            matches = re.findall(pattern, sequence)

            if matches:
                return True

            return False

        sequence = dto.sequence
        resultList = []

        for pattern in dto.pattern:
            isFound = isPatternFound(sequence, pattern)
            ssr = ssrPatternSearch(pattern)

            resultSSRDto = SSRResultDTO(pattern, isFound, ssr)

            resultList.append(resultSSRDto)

        return resultList
