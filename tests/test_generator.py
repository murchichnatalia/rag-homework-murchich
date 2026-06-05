from app.generator import ask


def test_generator_returns_dict():
    result = ask("crime TV shows")

    assert isinstance(result, dict)
    assert "answer" in result
    assert "sources" in result


def test_negative_question():
    result = ask("how to cook borscht")

    assert "нет достаточной информации" in result["answer"].lower()