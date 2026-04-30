from pathlib import Path

from quotes.models import Quote
from quotes.store import QuoteStore


def handle_add(args) -> None:
    quote = Quote(text=args.text, author=args.author)
    store = QuoteStore(Path("quotes.json"))
    store.add(quote)
    print(f'Added: "{quote.text}" — {quote.author}')


def handle_list(args) -> None:
    del args
    store = QuoteStore(Path("quotes.json"))
    quotes = store.list_all()

    if not quotes:
        print("No quotes yet.")
        return

    for quote in quotes:
        print(f'"{quote.text}" — {quote.author}')
