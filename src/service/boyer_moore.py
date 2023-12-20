import time
from typing import Any
from src.dto.regex_dto import SSRResultDTO, SsrDTO


class Interface:
    def search(self) -> Any:
        pass


class boyerMooreService(Interface):
    def __init__(self, dto: SsrDTO) -> None:
        self.sequence = dto.sequence
        self.pattern = dto.pattern

    def search(self, timed=False):
        def bad_char(pattern: str):
            # ord() of all alphabet (a-zA-Z) is around 122-123
            # make the size fo the list to 128
            bar_char_list = [-1] * (128)

            for i in range(len(pattern)):
                bar_char_list[ord(pattern[i])] = i

            return bar_char_list

        def matched_string(sequence: str, pattern: str) -> list:
            sequence_length = len(sequence)
            pattern_length = len(pattern)

            bad_char_list = bad_char(pattern)
            final_matches = []

            i = 0
            while i <= sequence_length - pattern_length:
                j = pattern_length - 1

                while j >= 0 and pattern[j] == sequence[i + j]:
                    j -= 1

                if j < 0:
                    final_matches.append(i + 1)
                    i += (
                        pattern_length
                        - bad_char_list[ord(sequence[i + pattern_length])]
                        if i + pattern_length < sequence_length
                        else 1
                    )
                else:
                    i += max(1, j - bad_char_list[ord(sequence[i + j])])

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
