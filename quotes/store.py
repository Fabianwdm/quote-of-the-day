import json
from pathlib import Path

from quotes.models import Quote


class QuoteStore:
    def __init__(self, path: Path) -> None:
        self.path = path

    def add(self, quote: Quote) -> None:
        if not self.path.exists():
            self.path.write_text("[]", encoding="utf-8")

        quotes = json.loads(self.path.read_text(encoding="utf-8"))
        quotes.append(quote.to_dict())
        self.path.write_text(json.dumps(quotes, indent=2), encoding="utf-8")

    def list_all(self) -> list[Quote]:
        quotes = json.loads(self.path.read_text(encoding="utf-8"))
        return [Quote.from_dict(item) for item in quotes]
