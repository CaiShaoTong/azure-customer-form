@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        description = request.form.get("description")
        return f"""
        <html>
        <head>
          <meta charset="UTF-8">
          <style>
            body {{
              background-color: #f4fff4;
              font-family: Arial, sans-serif;
              display: flex;
              justify-content: center;
              align-items: center;
              height: 100vh;
              animation: fadeIn 1s ease;
            }}
            .msg {{
              background: white;
              padding: 30px;
              border-radius: 12px;
              box-shadow: 0 0 15px rgba(0,0,0,0.1);
              text-align: center;
            }}
            @keyframes fadeIn {{
              from {{ opacity: 0; transform: scale(0.9); }}
              to {{ opacity: 1; transform: scale(1); }}
            }}
          </style>
        </head>
        <body>
          <div class="msg">
            <h2>感謝您的回報，{name}！</h2>
            <p><strong>Email：</strong>{email}</p>
            <p><strong>問題描述：</strong>{description}</p>
          </div>
        </body>
        </html>
        """
    return render_template("form.html")
