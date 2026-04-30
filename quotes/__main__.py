import argparse

from quotes.cli import handle_add


def main() -> None:
    parser = argparse.ArgumentParser(prog="quotes")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("text")
    add_parser.add_argument("--author", required=True)
    add_parser.set_defaults(func=handle_add)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
