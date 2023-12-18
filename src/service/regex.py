import regex as re
from src.dto.regex_dto import SsrDTO, SSRResultDTO


class Interface:
    def PatternSSRSearch(self, dto: SsrDTO) -> list[SSRResultDTO]:
        _ = dto
        return []


class regexService(Interface):
    def PatternSSRSearch(self, dto: SsrDTO):
        def ssrPatternSearch(sequence: str, pattern: str) -> list:
            final_matches = []

            matches = re.finditer(pattern, sequence, overlapped=True)

            for position in matches:
                final_matches.append(position.start()+1)

            return final_matches

        sequence = dto.sequence
        resultList = []

        for pattern in dto.pattern:
            matched = ssrPatternSearch(sequence, pattern)

            if matched:
                isFound = True
            else:
                isFound = False

            resultSSRDto = SSRResultDTO(pattern, isFound, len(matched), matched)

            resultList.append(resultSSRDto)

        return resultList
