import json

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
