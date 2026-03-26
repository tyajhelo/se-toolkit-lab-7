import argparse
from handlers import handle_command


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", dest="test_input")
    args = parser.parse_args()

    if args.test_input is not None:
        print(handle_command(args.test_input))
        return 0

    print("Telegram mode is not implemented yet. Use --test.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
