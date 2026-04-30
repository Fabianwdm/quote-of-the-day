import argparse
from typing import Optional

from quotes.cli import handle_add, handle_list


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="quotes")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("text")
    add_parser.add_argument("--author", required=True)
    add_parser.set_defaults(func=handle_add)

    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=handle_list)

    if argv and argv[0] == "quotes":
        argv = argv[1:]

    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    main()
