import json
import sys

from quotes.__main__ import main


def test_list_command_with_existing_quotes(tmp_path, monkeypatch, capsys):
    path = tmp_path / "quotes.json"
    path.write_text(
        json.dumps(
            [
                {
                    "text": "Be yourself; everyone else is already taken.",
                    "author": "Oscar Wilde",
                    "added_at": "2024-01-15T09:30:00",
                }
            ]
        ),
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    main(["quotes", "list"])

    captured = capsys.readouterr()

    assert "Be yourself; everyone else is already taken." in captured.out


def test_add_command(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["quotes", "add", "Hello world", "--author", "Anon"])

    main()

    store_path = tmp_path / "quotes.json"
    assert store_path.exists()

    data = json.loads(store_path.read_text(encoding="utf-8"))
    assert len(data) == 1
    assert data[0]["text"] == "Hello world"
