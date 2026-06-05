# Netflix Titles RAG

Учебный Retrieval-Augmented Generation (RAG) проект, реализованный на основе каталога фильмов и сериалов Netflix.

Проект демонстрирует полный RAG pipeline:

данные → документы → чанки → TF-IDF индекс → поиск → генерация ответа → Streamlit UI.

В качестве источника данных используется открытый датасет Netflix Titles, содержащий информацию о фильмах и сериалах, их жанрах, годе выпуска и кратком описании.

## Технологии

* Python 3.10+
* Streamlit
* Scikit-learn
* TF-IDF
* Cosine Similarity
* Pytest

## Структура проекта

```text
app/
scripts/
tests/
data/
doc/
homework/
```

## Запуск проекта

Создание окружения и установка зависимостей:

```bash
uv sync
```

Построение индекса:

```bash
uv run python scripts/build_index.py
```

Запуск пользовательского интерфейса:

```bash
uv run streamlit run app/main.py
```

## Demo-вопросы

1. crime TV shows
2. science nature documentaries
3. Korean TV Shows

## Negative-вопрос

how to cook borscht

Ожидаемое поведение: система должна вернуть отказ, так как информация отсутствует в корпусе данных.

## Возможности проекта

* Индексация 8807 фильмов и сериалов Netflix
* Автоматическая нарезка документов на чанки
* TF-IDF поиск релевантных документов
* Отображение источников ответа
* Демонстрация отказа при отсутствии релевантного контекста
* Streamlit интерфейс для взаимодействия с системой
