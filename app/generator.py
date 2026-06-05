from app.config import MIN_SCORE, TOP_K
from app.retriever import Retriever


REFUSAL_TEXT = "В найденных источниках нет достаточной информации для ответа."


def ask(question: str):
    retriever = Retriever()
    sources = retriever.search(question, k=TOP_K)

    best_score = sources[0]["score"] if sources else 0

    if best_score < MIN_SCORE:
        return {
            "answer": REFUSAL_TEXT,
            "sources": sources
        }

    best = sources[0]

    answer = (
        "Ответ сформирован на основе найденного фрагмента из корпуса Netflix Titles.\n\n"
        f"{best['text']}"
    )

    return {
        "answer": answer,
        "sources": sources
    }