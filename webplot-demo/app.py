from flask import Flask, render_template, request
from mistral_embed_utils import get_embedding, cosine_similarity, llm_filter_relevant

app = Flask(__name__)

# In-memory storage
users = []


@app.route("/", methods=["GET", "POST"])
def index():
    recommendations = None

    if request.method == "POST":
        nickname = request.form["nickname"]
        message = request.form["message"]

        embedding = get_embedding(message)

        # Compare with existing users
        scored = []
        for u in users:
            sim = cosine_similarity(embedding, u["embedding"])
            scored.append({
                "nickname": u["nickname"],
                "message": u["message"],
                "similarity": sim
            })

        # Top-3 by similarity
        top3 = sorted(scored, key=lambda x: x["similarity"], reverse=True)[:3]

        if top3:
            recommendations = llm_filter_relevant(message, top3)

        # Save new user AFTER comparison
        users.append({
            "nickname": nickname,
            "message": message,
            "embedding": embedding
        })

    return render_template("index.html", recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)
