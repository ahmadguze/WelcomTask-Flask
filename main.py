import json

from flask import Flask, request, make_response

app = Flask(__name__)


@app.get('/occurrencesOfCharacters')
def occurrences_of_characters():
    str = request.args.get('str')
    occurrences = {}
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
    app.run(debug=True, port=5000)
