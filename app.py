from flask import Flask, render_template, request

app = Flask(__name__)


def analyze_code(code, language):

    score = 100

    result = f"Language: {language}\n\n"

    if len(code.strip()) < 20:
        score -= 20
        result += "⚠ Code is very short.\n\n"

    if "print(" in code:
        result += "✓ This code outputs data.\n\n"

    if "password" in code.lower():
        score -= 20
        result += "⚠ Possible security issue detected.\n\n"

    if "while True" in code:
        score -= 15
        result += "⚠ Possible infinite loop.\n\n"

    if "/b" in code or "/ b" in code:
        score -= 15
        result += "⚠ Possible division-by-zero risk.\n\n"

    if score < 0:
        score = 0

    result += f"\nCode Quality Score: {score}/100\n"

    result += "\nSuggestions:\n"
    result += "- Add comments.\n"
    result += "- Handle errors properly.\n"
    result += "- Use meaningful variable names.\n"

    return result


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        code = request.form.get("code", "")

        language = request.form.get(
            "language",
            "Python"
        )

        result = analyze_code(
            code,
            language
        )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)