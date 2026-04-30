# Quote of the Day

A tiny CLI for collecting and recalling quotes you don't want to forget.

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)

## Features

- Store quotes locally as JSON
- Add quotes via CLI
- List all saved quotes
- Pick a random quote

## Installation

```bash
git clone <your-repo-url>
cd quote-of-the-day
pip install -e .
```

## Usage

```bash
quotes add "Stay hungry, stay foolish." --author "Steve Jobs"
quotes list
quotes list --random
```

## Development

```bash
pip install -e ".[dev]"
pytest
```

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on setting up your environment, proposing changes, and opening pull requests.

## License

MIT — see LICENSE file.
