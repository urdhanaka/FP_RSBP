import time
from typing import Any
from src.dto.regex_dto import SSRResultDTO, SsrDTO


class Interface:
    def search(self) -> Any:
        pass


class kmpService(Interface):
    def __init__(self, dto: SsrDTO) -> None:
        self.sequence = dto.sequence
        self.pattern = dto.pattern

    def search(self, timed=False):
        def compute_lps(pattern: str) -> list:
            pattern_length = len(pattern)
            prev_longest = 0
            lps = [0] * pattern_length
            i = 1

            while i < pattern_length:
                if pattern[i] == pattern[prev_longest]:
                    prev_longest += 1
                    lps[i] = prev_longest
                    i += 1
                else:
                    if prev_longest != 0:
                        prev_longest = lps[prev_longest - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        def matched_string(sequence: str, pattern: str) -> list:
            sequence_length = len(sequence)
            pattern_length = len(pattern)

            final_matches = []
            lps = compute_lps(pattern)

            i = 0
            j = 0
            while (sequence_length - i) >= (pattern_length - j):
                if pattern[j] == sequence[i]:
                    i += 1
                    j += 1

                if j == pattern_length:
                    final_matches.append(i - j + 1)
                    j = lps[j - 1]
                elif (i < sequence_length) and (pattern[j] != sequence[i]):
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return final_matches

        resultList = []

        for pattern in self.pattern:
            if timed:
                start = time.perf_counter()
                matched = matched_string(self.sequence, pattern)
                end = time.perf_counter()

                elapsed_time = f"{end - start:0.4f} seconds"

                if matched:
                    isFound = True
                else:
                    isFound = False

                resultDTO = SSRResultDTO(
                    pattern, isFound, len(matched), matched, elapsed_time
                )
                resultList.append(resultDTO)
            else:
                matched = matched_string(self.sequence, pattern)

                if matched:
                    isFound = True
                else:
                    isFound = False

                resultSSRDto = SSRResultDTO(pattern, isFound, len(matched), matched)
                resultList.append(resultSSRDto)

        return resultList
