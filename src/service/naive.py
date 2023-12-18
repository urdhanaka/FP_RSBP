from src.dto.regex_dto import SSRResultDTO, SsrDTO


class Interface:
    def PatternSSRSearch(self, dto: SsrDTO) -> list[SSRResultDTO]:
        _ = dto
        return []


class naiveService(Interface):
    def PatternSSRSearch(self, dto: SsrDTO):
        def ssrPatternSearch(sequence: str, pattern: str) -> list:
            sequence_length = len(sequence)
            pattern_length = len(pattern)

            final_matches = []

            for i in range(sequence_length-pattern_length+1):
                checked_string = sequence[i : i + pattern_length]

                if checked_string != pattern:
                    continue

                final_matches.append(i + 1)

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
