from app.generator import ask


def main():
    questions = [
    "crime TV shows",
    "science nature documentaries",
    "Korean TV Shows",
    "how to cook borscht"
    ]

    for question in questions:
        result = ask(question)

        print("QUESTION:", question)
        print("ANSWER:", result["answer"])
        print("SOURCES:")
        for source in result["sources"]:
            print(source["doc_id"], source["name"], round(source["score"], 4))
        print("=" * 100)


if __name__ == "__main__":
    main()