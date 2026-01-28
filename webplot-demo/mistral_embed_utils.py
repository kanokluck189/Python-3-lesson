import numpy as np
from mistralai import Mistral

MODEL_EMBED = "mistral-embed"
MODEL_CHAT = "mistral-small"

client = Mistral(api_key="7W0O9quqWKRibucc2oYpuMFzoGSWPFxw")


MODEL_EMBED = "mistral-embed"
MODEL_CHAT = "mistral-small"

client = Mistral(api_key="7W0O9quqWKRibucc2oYpuMFzoGSWPFxw")


def get_embedding(text: str) -> np.ndarray:
    response = client.embeddings.create(
        model=MODEL_EMBED,
        inputs=[text]
    )
    return np.array(response.data[0].embedding)



def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))


def llm_filter_relevant(user_message, candidates):
    system_prompt = (
        "You help find people who share similar thoughts or plans. "
        "Select only messages that are truly relevant. "
        "Explain briefly why they match. "
        "If none match, say NONE."
    )

    user_prompt = f"User message:\n{user_message}\n\nCandidates:\n"
    for c in candidates:
        user_prompt += f"- {c['nickname']}: {c['message']}\n"

    response = client.chat.complete(
        model=MODEL_CHAT,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content
