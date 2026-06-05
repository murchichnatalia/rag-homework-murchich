import streamlit as st

from app.generator import ask
from app.config import VECTORIZER_PATH, MATRIX_PATH


st.set_page_config(page_title="Netflix Titles RAG", layout="wide")

st.title("Учебный RAG по каталогу Netflix Titles")

st.write(
    "Система ищет релевантные фильмы и сериалы в корпусе Netflix Titles "
    "и формирует demo-ответ только на основе найденных источников."
)

st.sidebar.header("Demo-вопросы")

demo_questions = [
    "astronauts Mars mission",
    "crime TV shows",
    "science nature documentaries",
    "how to cook borscht"
]

selected_question = st.sidebar.radio("Выберите вопрос", demo_questions)
 
question = st.text_input("Введите вопрос", value=selected_question)

if not VECTORIZER_PATH.exists() or not MATRIX_PATH.exists():
    st.error("Индекс не найден. Сначала запустите: python -m scripts.build_index")
else:
    if st.button("Спросить"):
        result = ask(question)

        st.subheader("Ответ")
        st.write(result["answer"])

        st.subheader("Источники")
        for source in result["sources"]:
            with st.expander(
                f"doc_id={source['doc_id']} | {source['name']} | score={source['score']:.4f}"
            ):
                st.write(source["text"])