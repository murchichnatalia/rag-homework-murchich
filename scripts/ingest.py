import json

from app.config import RAW_DATA_PATH, DOCUMENTS_PATH


def clean_text(text: str) -> str:
    return " ".join(text.split())


def ingest():
    DOCUMENTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(RAW_DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    documents = []

    for item in data["datasets"]:
        documents.append({
            "doc_id": str(item["id"]),
            "name": item["name"],
            "text": clean_text(item["text"]),
            "source_file": str(RAW_DATA_PATH)
        })

    with open(DOCUMENTS_PATH, "w", encoding="utf-8") as f:
        for doc in documents:
            f.write(json.dumps(doc, ensure_ascii=False) + "\n")

    print(f"Saved {len(documents)} documents to {DOCUMENTS_PATH}")


if __name__ == "__main__":
    ingest()