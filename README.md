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

1. astronauts Mars mission
2. crime TV shows
3. science nature documentaries

## Negative-вопрос

how to cook borscht

Ожидаемое поведение: система должна вернуть отказ, так как информация отсутствует в корпусе данных.

## Демонстрация интерфейса

<img width="2552" height="1007" alt="RAG" src="https://github.com/user-attachments/assets/3a430ce1-5027-4b5f-878a-f8a8faa9038d" />


## Возможности проекта

* Индексация 8807 фильмов и сериалов Netflix
* Автоматическая нарезка документов на чанки
* TF-IDF поиск релевантных документов
* Отображение источников ответа
* Демонстрация отказа при отсутствии релевантного контекста
* Streamlit интерфейс для взаимодействия с системой
