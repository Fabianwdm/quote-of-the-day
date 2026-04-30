import argparse
from typing import Optional

from quotes.cli import handle_list


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="quotes")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=handle_list)

    if argv and argv[0] == "quotes":
        argv = argv[1:]

    args = parser.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    main()
