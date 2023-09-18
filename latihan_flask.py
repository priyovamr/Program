from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Selamat Datang!'

if __name__ == "__main__":
    app.run(debug = True)