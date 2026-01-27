from flask import Flask, render_template, request
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import math
import os
import requests
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

app = Flask(__name__)

def llm_to_expression(user_request):
    url = "https://api.mistral.ai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Convert the following user request into a valid Python mathematical
expression using variable x.

Rules:
- Use only x, math, or numpy
- Do not explain anything
- Output ONLY the expression

User request:
{user_request}
"""

    data = {
        "model": "mistral-small",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"].strip()

@app.route("/", methods=["GET", "POST"])
def index():
    user_text = ""
    expression = ""
    a, b = -10, 10
    color = "blue"

    if request.method == "POST":
        user_text = request.form.get("expression", "")
        a = float(request.form.get("a", a))
        b = float(request.form.get("b", b))
        color = request.form.get("color", color)

        expression = llm_to_expression(user_text)

        x = np.linspace(a, b, 400)

        try:
            y = eval(expression, {"x": x, "math": math, "np": np})

            plt.figure()
            plt.plot(x, y, color=color)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"y = {expression}")
            plt.grid(True)
            plt.savefig("static/plot.png")
            plt.close()

        except Exception as e:
            print("Plot error:", e)

    return render_template(
        "index.html",
        user_text=user_text,
        expression=expression,
        a=a,
        b=b,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)
