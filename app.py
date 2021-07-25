import json
from flask import Flask, request

app = Flask(__name__)


@app.get('/oOfc')
@app.get('/occurrencesOfCharacters')
def occurrences_of_characters():
    str = request.args.get('str')
    occurrences = {}

    if str is None:
        return app.response_class(
            response=json.dumps({"msg": 'please put the string in query parameter \'str\''}),
            status=400,
            mimetype='application/json'
        )

    for char in str:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1
    response = app.response_class(
        response=json.dumps(occurrences),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
