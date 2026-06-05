from app.chunker import chunk_text


def test_short_text():
    chunks = chunk_text("hello world")
    assert len(chunks) == 1


def test_long_text():
    text = "a" * 1000
    chunks = chunk_text(text, chunk_size=200, overlap=50)
    assert len(chunks) > 1