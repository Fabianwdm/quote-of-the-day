# Contributing

## Branching

This project follows a trunk-based workflow. Keep `main` releasable and use short-lived feature branches for focused work that merges back quickly.

Use these branch name prefixes:

- `feat/` for new features, for example `feat/add-list-command`
- `fix/` for bug fixes, for example `fix/handle-missing-store`
- `docs/` for documentation changes, for example `docs/add-contributing-guide`
- `refactor/` for internal code improvements, for example `refactor/simplify-store-loading`
- `chore/` for maintenance work, for example `chore/update-pyproject`

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/).

Supported types in this project:

- `feat`
- `fix`
- `docs`
- `refactor`
- `chore`
- `test`

Write commit subjects in the imperative mood and keep the subject line under 72 characters.

## Pull Requests

Create pull requests from branches based on `main`.

Link the related issue in the pull request description with `Closes #N` when applicable. Pull requests require one approval before merging. Merge with squash-merge, and delete the branch after merge.

## Code Review

Leave substantive review comments that explain concerns, tradeoffs, or suggested changes rather than only writing "LGTM".

Authors should engage with feedback thoughtfully and discuss it when needed rather than reflexively applying every suggestion.

## Running Tests

Install development dependencies and run the test suite with:

```bash
pip install -e ".[dev]"
pytest
```

## Code Style

Follow PEP 8.

No formatter is enforced for a project this small, but a `ruff format` pass is welcome.
