from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! docker is running this python app successfully"

if __name__ == "__main__":  # Fixed: == instead of =
    app.run(host="0.0.0.0", port=5000)

