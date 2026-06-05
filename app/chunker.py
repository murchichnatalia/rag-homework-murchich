def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    text = " ".join(text.split())

    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start = end - overlap

    return chunks


def chunk_documents(documents: list[dict], chunk_size: int = 500, overlap: int = 50) -> list[dict]:
    chunks = []

    for doc in documents:
        parts = chunk_text(doc["text"], chunk_size, overlap)

        for i, part in enumerate(parts):
            chunks.append({
                "chunk_id": f"{doc['doc_id']}_{i}",
                "doc_id": doc["doc_id"],
                "name": doc["name"],
                "text": part
            })

    return chunks