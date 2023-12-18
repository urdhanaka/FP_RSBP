from flask import Blueprint, Response, request
from http import HTTPStatus

from src.dto.regex_dto import SsrDTO
from src.service.regex import regexService

import json

regex = Blueprint("regex", __name__)


@regex.route("/", methods=["POST"])
def handle_ssr() -> Response:
    data = request.json
    dto = SsrDTO(data)

    if dto.is_valid() == False:
        return Response(
            response=json.dumps({"status": "request not satisfied"}),
            status=HTTPStatus.BAD_REQUEST,
            mimetype="application/json",
        )

    service = regexService()
    response_data = service.PatternSSRSearch(dto)

    response_json = json.dumps(response_data, default=lambda o: o.encode(), indent=1)

    return Response(
        response=response_json,
        status=200,
        mimetype="application/json",
    )
