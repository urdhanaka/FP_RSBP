import time
from typing import Any
import regex as re
from src.dto.regex_dto import SsrDTO, SSRResultDTO


class Interface:
    def search(self) -> Any:
        pass


class regexService(Interface):
    def __init__(self, dto: SsrDTO) -> None:
        self.sequence = dto.sequence
        self.pattern = dto.pattern

    def search(self, timed=False):
        def matched_string(sequence: str, pattern: str) -> list:
            final_matches = []

            matches = re.finditer(pattern, sequence, overlapped=True)

            for position in matches:
                final_matches.append(position.start() + 1)

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
