from http import HTTPStatus
from flask import Blueprint, Response, json, request

from src.dto.regex_dto import SsrDTO
from src.service.evaluation import evaluationService

eval_func = Blueprint("eval_func", __name__)


@eval_func.route("/", methods=["GET"])
def handle_search() -> Response:
    data = request.json
    dto = SsrDTO(data)

    if dto.is_valid() == False:
        return Response(
            response=json.dumps({"status": "request not satisfied"}),
            status=HTTPStatus.BAD_REQUEST,
            mimetype="application/json",
        )

    service = evaluationService(dto)
    response_data = service.evaluation()
    response_json = json.dumps(response_data, default=lambda o: o.encode(), indent=4)

    return Response(
        response=response_json,
        status=200,
        mimetype="application/json",
    )
