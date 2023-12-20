from flask import Flask, render_template, request
from src.dto.regex_dto import SsrDTO
from src.routes import api
from src.service.evaluation import evaluationService

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api")

@app.route("/evaluation", methods=["GET", "POST"])
def evaluation_view():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = {}
        temp = request.form["pattern"].split(",")
        data["sequence"] = request.form["sequence"]
        data["pattern"] = temp
        dto = SsrDTO(data)
        service = evaluationService(dto)
        result = service.evaluation()

        return render_template("evaluation.html", data=result)
