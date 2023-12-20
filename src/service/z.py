import time
from typing import Any
from src.dto.regex_dto import SSRResultDTO, SsrDTO


class Interface:
    def search(self) -> Any:
        pass


class zService(Interface):
    def __init__(self, dto: SsrDTO) -> None:
        self.sequence = dto.sequence
        self.pattern = dto.pattern

    def search(self, timed=False):
        def compute_z_arr(sequence: str) -> list:
            sequence_length = len(sequence)
            z_arr = [0] * sequence_length
            left = 0
            right = 0

            for k in range(1, sequence_length):
                if k > right:
                    left = right = k

                    while (
                        right < sequence_length
                        and sequence[right] == sequence[right - left]
                    ):
                        right += 1

                    z_arr[k] = right - left
                    right -= 1
                else:
                    k1 = k - left

                    if z_arr[k1] < right - k + 1:
                        z_arr[k] = z_arr[k1]
                    else:
                        left = k

                        while (
                            right < sequence_length
                            and sequence[right] == sequence[right - left]
                        ):
                            right += 1

                        z_arr[k] = right - left
                        right -= 1

            return z_arr

        def matched_string(sequence: str, pattern: str) -> list:
            concatted_string = pattern + "$" + sequence
            concatted_length = len(concatted_string)
            z = compute_z_arr(concatted_string)
            final_matches = []

            for i in range(concatted_length):
                if z[i] == len(pattern):
                    final_matches.append(i - len(pattern))

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
