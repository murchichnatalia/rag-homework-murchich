import json
import joblib
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer

from app.config import (
    DOCUMENTS_PATH,
    CHUNKS_PATH,
    VECTORIZER_PATH,
    MATRIX_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)
from app.chunker import chunk_documents
from scripts.ingest import ingest


def load_documents():
    documents = []

    with open(DOCUMENTS_PATH, "r", encoding="utf-8") as f:
        for line in f:
            documents.append(json.loads(line))

    return documents


def save_chunks(chunks):
    CHUNKS_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(CHUNKS_PATH, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")


def build_index():
    ingest()

    documents = load_documents()
    chunks = chunk_documents(documents, CHUNK_SIZE, CHUNK_OVERLAP)
    save_chunks(chunks)

    texts = [chunk["text"] for chunk in chunks]

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(texts)

    VECTORIZER_PATH.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(vectorizer, VECTORIZER_PATH)
    sparse.save_npz(MATRIX_PATH, matrix)

    print(f"Saved {len(chunks)} chunks to {CHUNKS_PATH}")
    print(f"Saved vectorizer to {VECTORIZER_PATH}")
    print(f"Saved matrix to {MATRIX_PATH}")


if __name__ == "__main__":
    build_index()