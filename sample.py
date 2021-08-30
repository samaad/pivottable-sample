from flask import Flask, jsonify, request, json

app = Flask(__name__)

incomes = [
  { 'description': 'salary', 'amount': 5000 },
  { 'description': 'salary', 'amount': 9000 },
  { 'description': 'salary', 'amount': 10000 }
]


@app.route('/incomes')
def get_incomes():
  return jsonify(incomes)


@app.route('/dumps')
def get_dumps():
  return json.dumps(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204


app.run()