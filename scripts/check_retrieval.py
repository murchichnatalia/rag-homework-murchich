from app.retriever import Retriever


def main():
    retriever = Retriever()

    query = "movies about space and astronauts"
    results = retriever.search(query, k=5)

    print("QUERY:", query)
    print()

    for result in results:
        print("doc_id:", result["doc_id"])
        print("name:", result["name"])
        print("score:", round(result["score"], 4))
        print("text:", result["text"][:500])
        print("-" * 80)


if __name__ == "__main__":
    main()