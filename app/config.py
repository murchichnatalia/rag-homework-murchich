from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]

RAW_DATA_PATH = ROOT_DIR / "data" / "raw" / "datasets.json"
DOCUMENTS_PATH = ROOT_DIR / "data" / "processed" / "documents.jsonl"
CHUNKS_PATH = ROOT_DIR / "data" / "processed" / "chunks.jsonl"

INDEX_DIR = ROOT_DIR / "data" / "index"
VECTORIZER_PATH = INDEX_DIR / "vectorizer.pkl"
MATRIX_PATH = INDEX_DIR / "matrix.npz"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50
TOP_K = 5
MIN_SCORE = 0.45