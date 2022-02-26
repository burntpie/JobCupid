from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/qn1")
def qn1():
    return "<p>qn1!</p>"
"""
& C:/Users/ngliw/AppData/Local/Programs/Python/Python38-32/python.exe "c:/Users/ngliw/OneDrive - Nanyang Technological University/intuition hackathon/xiaolongbaoz/main.py"
"""


if __name__ == "__main__":
    app.run(debug= True)