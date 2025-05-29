from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        return f"<h2>謝謝您的留言，{name}！</h2><p>{message}</p>"
    return render_template("form.html")
