from flask import Blueprint, Response, request, json
from http import HTTPStatus

from src.dto.regex_dto import RegexDto
from src.service.regex import regexService

regex = Blueprint("regex", __name__)


@regex.route('', methods = ["GET", "POST"])
def handle_search() -> Response:
    if request.method == "GET":
        return Response(
            response=json.dumps({'status': "you have no permission"}),
            status=HTTPStatus.UNAUTHORIZED,
            mimetype='application/json'
        )

    else:
        data = request.json
        dto = RegexDto(data)

        if dto.is_valid() == False:
            return Response(
                response=json.dumps({'status': 'request not satisfied'}),
                status=HTTPStatus.BAD_REQUEST,
                mimetype='application/json'
            )

        service = regexService()
        print(service.PatternSearch(dto))

        return Response(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )

