from flask import Blueprint, Response, request
from http import HTTPStatus

from src.dto.regex_dto import SsrDTO
from src.service.boyer_moore import boyerMooreService

import json

boyer_moore = Blueprint("boyer_moore", __name__)


@boyer_moore.route("", methods=["GET", "POST"])
def handle_search() -> Response:
    data = request.json
    dto = SsrDTO(data)

    if dto.is_valid() == False:
        return Response(
            response=json.dumps({"status": "request not satisfied"}),
            status=HTTPStatus.BAD_REQUEST,
            mimetype="application/json",
        )

    service = boyerMooreService(dto)
    response_data = service.boyer_moore_search()
    response_json = json.dumps(response_data, default=lambda o: o.encode(), indent=4)

    return Response(
        response=response_json,
        status=200,
        mimetype="application/json",
    )
