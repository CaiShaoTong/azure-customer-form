from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        description = request.form.get("description")
        return f"""
            <h2>感謝您的回報，{name}！</h2>
            <p>我們已收到您的問題描述：</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>內容:</strong> {description}</p>
        """
    return render_template("form.html")
