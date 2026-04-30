from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Quote:
    text: str
    author: str
    added_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict[str, str]:
        return {
            "text": self.text,
            "author": self.author,
            "added_at": self.added_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, d: dict[str, str]) -> "Quote":
        return cls(
            text=d["text"],
            author=d["author"],
            added_at=datetime.fromisoformat(d["added_at"]),
        )
