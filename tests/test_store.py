from quotes.models import Quote
from quotes.store import QuoteStore


def test_add_then_list(tmp_path):
    store = QuoteStore(tmp_path / "quotes.json")
    quote = Quote(text="Do or do not. There is no try.", author="Yoda")

    store.add(quote)

    quotes = store.list_all()

    assert len(quotes) == 1
    assert quotes[0].text == quote.text
    assert quotes[0].author == quote.author


def test_list_returns_empty_list_on_new_store(tmp_path):
    path = tmp_path / "quotes.json"
    path.write_text("[]", encoding="utf-8")
    store = QuoteStore(path)

    quotes = store.list_all()

    assert quotes == []


def test_persistence_across_instances(tmp_path):
    path = tmp_path / "quotes.json"
    store_a = QuoteStore(path)
    quote = Quote(text="The only way out is through.", author="Robert Frost")

    store_a.add(quote)

    store_b = QuoteStore(path)
    quotes = store_b.list_all()

    assert len(quotes) == 1
    assert quotes[0].text == quote.text
    assert quotes[0].author == quote.author
