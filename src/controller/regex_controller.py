from flask import Blueprint, Response, request, json
from http import HTTPStatus

from src.dto.regex_dto import RegexDTO, SSRDTO
from src.service.regex import regexService

regex = Blueprint("regex", __name__)


@regex.route("", methods=["GET", "POST"])
def handle_search() -> Response:
    if request.method == "GET":
        return Response(
            response=json.dumps({"status": "you have no permission"}),
            status=HTTPStatus.UNAUTHORIZED,
            mimetype="application/json",
        )

    else:
        data = request.json
        dto = RegexDTO(data)

        if dto.is_valid() == False:
            return Response(
                response=json.dumps({"status": "request not satisfied"}),
                status=HTTPStatus.BAD_REQUEST,
                mimetype="application/json",
            )

        service = regexService()
        print(service.PatternSearch(dto))

        return Response(
            response=json.dumps(data), status=200, mimetype="application/json"
        )


@regex.route("ssr", methods=["POST"])
def handle_ssr() -> Response:
    data = request.json
    dto = SSRDTO(data)

    if dto.is_valid() == False:
        return Response(
            response=json.dumps({"status": "request not satisfied"}),
            status=HTTPStatus.BAD_REQUEST,
            mimetype="application/json",
        )

    service = regexService()
    response_data = service.SSRSearch(dto)

    return Response(
        response=json.dumps(
            {
                "res": {
                    "2": response_data.result["2"],
                    "3": response_data.result["3"],
                    "4": response_data.result["4"],
                    "5": response_data.result["5"],
                    "6": response_data.result["6"],
                },
            },
        ),
        status=200,
        mimetype="application/json",
    )
