import json
import joblib
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

from app.config import VECTORIZER_PATH, MATRIX_PATH, CHUNKS_PATH, TOP_K


class Retriever:
    def __init__(self):
        self.vectorizer = joblib.load(VECTORIZER_PATH)
        self.matrix = sparse.load_npz(MATRIX_PATH)
        self.chunks = self._load_chunks()

    def _load_chunks(self):
        chunks = []
        with open(CHUNKS_PATH, "r", encoding="utf-8") as f:
            for line in f:
                chunks.append(json.loads(line))
        return chunks

    def search(self, query: str, k: int = TOP_K):
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix).flatten()
        top_indices = scores.argsort()[::-1][:k]

        results = []
        for idx in top_indices:
            chunk = self.chunks[idx].copy()
            chunk["score"] = float(scores[idx])
            results.append(chunk)

        return results