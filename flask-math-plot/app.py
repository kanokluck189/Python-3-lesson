from flask import Flask, render_template, request
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    expression = "x**2"
    a, b = -10, 10
    color = "blue"

    if request.method == "POST":
        expression = request.form.get("expression", expression)
        a = float(request.form.get("a", a))
        b = float(request.form.get("b", b))
        color = request.form.get("color", color)

        x = np.linspace(a, b, 400)

        try:
            y = eval(expression, {
                "x": x,
                "math": math,
                "np": np
            })

            plt.figure()
            plt.plot(x, y, color=color)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title(f"y = {expression}")
            plt.grid(True)
            plt.savefig("static/plot.png")
            print("PLOT SAVED!")
            plt.close()

        except Exception as e:
            print("Plot error:", e)

    return render_template(
        "index.html",
        expression=expression,
        a=a,
        b=b,
        color=color
    )

if __name__ == "__main__":
    app.run(debug=True)
