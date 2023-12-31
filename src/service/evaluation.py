from typing import Any

from flask import json
from src.dto.regex_dto import SsrDTO
from src.service.naive import naiveService
from src.service.regex import regexService
from src.service.z import zService
from src.service.boyer_moore import boyerMooreService
from src.service.kmp import kmpService


class Interface:
    def evaluation(self) -> Any:
        pass


class evaluationService(Interface):
    def __init__(self, dto: SsrDTO) -> None:
        self.dto = dto
        self.algorithm = {
            "naive": naiveService,
            "regex": regexService,
            "z": zService,
            "boyer-moore": boyerMooreService,
            "kmp": kmpService,
        }

    def evaluation(self) -> Any:
        result = {}

        result["sequence"] = self.dto.sequence
        result["result"] = []

        for algorithm_name, _ in self.algorithm.items():
            service = self.algorithm[algorithm_name](self.dto)

            temp = service.search(timed=True)

            resDict = {}
            resDict[algorithm_name] = temp

            result["result"].append(resDict)

        return result

