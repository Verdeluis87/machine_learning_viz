import pickle
from sklearn.ensemble import RandomForestClassifier

with open('Machine_Learning/static/models/encoders.pkl', 'rb') as ff:
    encoders = pickle.load(ff)

with open('Machine_Learning/static/models/rf_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

class ModelException(Exception):
    pass


class ModelInput:
    def __init__(
        self,
        budget: float,
        actor: str,
        director: str,
        language: str,
        production: str,
        writer: str,
        runtime: float,
        country: str,
        rated: str,
        genre: str,
    ):
        self.budget = budget
        self.actor = actor
        self.director = director
        self.language = language
        self.production = production
        self.writer = writer
        self.runtime = runtime
        self.country = country
        self.rated = rated
        self.genre = genre


class ModelOutput:
    def __init__(
        self,
        profitable: bool,
    ):
        self.profitable = profitable


def clean_value(value: str) -> str:
    value = value or ''
    value = ' '.join(value.lower().strip().split())
    return value


def _transform_value(label: str, model_input: ModelInput):
    value = getattr(model_input, label)
    value = clean_value(value)
    return encoders[label].transform([value])[0]


def _get_data(model_input):
    return [
        model_input.budget,
        _transform_value('actor', model_input),
        _transform_value('director', model_input),
        _transform_value('language', model_input),
        _transform_value('production', model_input),
        _transform_value('writer', model_input),
        model_input.runtime,
        _transform_value('country', model_input),
        _transform_value('rated', model_input),
        _transform_value('genre', model_input),
    ]


def run_model(model_input: ModelInput) -> ModelOutput:
    try:
        data = _get_data(model_input)
        model_result = rf_model.predict([data])
        result = ModelOutput(
            profitable=bool(model_result[0]),
        )
        return result
    except (ValueError) as err:
        raise ModelException(str(err))
