from src.dto.regex_dto import SSRResultDTO, SsrDTO


class Interface:
    def PatternSSRSearch(self, dto: SsrDTO) -> list[SSRResultDTO]:
        _ = dto
        return []


class naiveService(Interface):
    def PatternSSRSearch(self, dto: SsrDTO):
        def ssrPatternSearch(sequence: str) -> list:
            sequence_length = len(sequence)

            final_matches = []

            for i in range(2, sequence_length // 2 + 1):
                temp_string = sequence[:i] + sequence[:i]

                if temp_string in sequence:
                    final_matches.append(sequence[:i])

            return final_matches

        def isPatternFound(sequence: str, pattern: str) -> list:
            sequence_length = len(sequence)
            pattern_length = len(pattern)

            matches = []

            for i in range(sequence_length - pattern_length + 1):
                j = 0

                while j < pattern_length:
                    if sequence[i + j] != pattern[j]:
                        break
                    j += 1

                if j == pattern_length:
                    matches.append(pattern)

            return matches

        sequence = dto.sequence
        resultList = []

        for pattern in dto.pattern:
            foundPattern = isPatternFound(sequence, pattern)
            ssr = ssrPatternSearch(pattern)
            isFound = False

            if foundPattern:
                isFound = True

            resultSSRDto = SSRResultDTO(pattern, isFound, len(foundPattern), ssr)

            resultList.append(resultSSRDto)

        return resultList
