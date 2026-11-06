
from flask import Flask, request
from difflib import SequenceMatcher
from html import escape

app = Flask(__name__)

TRUSTED_DOMAIN = "konami.com"

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        domain = request.form.get("domain", "").strip().lower()

        similarity = SequenceMatcher(
            None, TRUSTED_DOMAIN, domain
        ).ratio()

        if domain == TRUSTED_DOMAIN:
            result = "This matches the reference domain."
        elif similarity >= 0.75:
            result = "WARNING: This domain looks similar. Verify it carefully!"
        else:
            result = "This domain does not match the reference domain."

    return f"""
    <html>
    <head>
        <title>Konami Security Lab</title>
    </head>
    <body style="background:#151515;color:white;
                 text-align:center;padding:50px;
                 font-family:Arial;">

        <h1>KONAMI SECURITY LAB</h1>
        <h2>Typosquatting Detector</h2>

        <p>Reference domain: konami.com</p>

        <form method="POST">
            <input name="domain"
                   placeholder="Enter a domain"
                   required>
            <button type="submit">Check Domain</button>
        </form>

        <h3>{escape(result)}</h3>

        <p>Educational cybersecurity demonstration</p>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=False)
