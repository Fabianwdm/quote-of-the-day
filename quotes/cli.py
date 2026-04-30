from pathlib import Path

from quotes.store import QuoteStore


def handle_list(args) -> None:
    del args
    store = QuoteStore(Path("quotes.json"))
    quotes = store.list_all()

    if not quotes:
        print("No quotes yet.")
        return

    for quote in quotes:
        print(f'"{quote.text}" — {quote.author}')
