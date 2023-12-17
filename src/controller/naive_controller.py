from flask import Blueprint, Response, request
from http import HTTPStatus

from src.dto.regex_dto import SsrDTO
from src.service.naive import naiveService

import json

naive = Blueprint("naive", __name__)


@naive.route("/", methods=["GET", "POST"])
def handle_search() -> Response:
    data = request.json
    dto = SsrDTO(data)

    if dto.is_valid() == False:
        return Response(
            response=json.dumps({"status": "request not satisfied"}),
            status=HTTPStatus.BAD_REQUEST,
            mimetype="application/json",
        )

    service = naiveService()
    response_data = service.PatternSSRSearch(dto)

    response_json = json.dumps(response_data, default=lambda o: o.encode(), indent=4)

    return Response(
        response=response_json,
        status=200,
        mimetype="application/json",
    )
