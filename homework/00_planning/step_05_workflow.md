# Workflow

Netflix CSV → datasets.json → documents.jsonl → chunks.jsonl → TF-IDF index → retrieval → answer generation → Streamlit UI.

Каждый этап реализован отдельным модулем и может быть протестирован независимо.
