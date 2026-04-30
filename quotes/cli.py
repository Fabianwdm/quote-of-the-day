from pathlib import Path

from quotes.models import Quote
from quotes.store import QuoteStore


def handle_add(args) -> None:
    quote = Quote(text=args.text, author=args.author)
    store = QuoteStore(Path("quotes.json"))
    store.add(quote)
    print(f'Added: "{quote.text}" — {quote.author}')
