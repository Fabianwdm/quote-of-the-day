import json
import sys

from quotes.__main__ import main


def test_add_command(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["quotes", "add", "Hello world", "--author", "Anon"])

    main()

    store_path = tmp_path / "quotes.json"
    assert store_path.exists()

    data = json.loads(store_path.read_text(encoding="utf-8"))
    assert len(data) == 1
    assert data[0]["text"] == "Hello world"
