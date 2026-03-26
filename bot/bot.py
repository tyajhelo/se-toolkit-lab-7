import argparse
from handlers import handle_command

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str)
    args = parser.parse_args()

    if args.test:
        print(handle_command(args.test))
        return 0

    print("Run with --test")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
