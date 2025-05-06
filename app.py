from flask import Flask, jsonify
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route("/consultas")
def consultas():
  return jsonify([
    {"consulta": "Hola", "user_name": "Juan Carlos"},
    {"consulta": "Que tal", "user_name": "Ana Maria"}
  ])

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)