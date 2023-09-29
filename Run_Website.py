from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def serve_html():
    return send_file("Website.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)