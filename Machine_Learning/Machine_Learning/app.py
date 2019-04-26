# import necessary libraries
from Machine_Learning.model import run_model, ModelInput, ModelOutput, ModelException
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

# create route that renders index.html template


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/visualizations.html")
def viz():
    return render_template("visualizations.html")

@app.route("/results.html")
def results():
    return render_template("results.html")

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        data = ModelInput(
            budget=request.form["budget"],
            actor=request.form["actor"],
            director=request.form["director"],
            language=request.form["lenguage"],
            production=request.form["production"],
            writer=request.form["writer"],
            runtime=request.form["runtime"],
            country=request.form["country"],
            rated=request.form["rating"],
            genre=request.form["genre"]
        )

        try:
            result: ModelOutput = run_model(data)
        except ModelException:
            print('Bad input')
        else:
            print('Is profitable?')
            print(result.profitable)
            data = {'result': result.profitable}

        return render_template("results.html", data=data['result'])


if __name__ == "__main__":
    app.run(debug=True)
