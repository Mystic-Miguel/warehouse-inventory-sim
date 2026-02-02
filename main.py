import argparse, sys
def main():
    p = argparse.ArgumentParser(description="CLI tool")
    p.add_argument("--input", help="input file")
    args = p.parse_args()
    print("OK - CLI skeleton ready.", "input=", args.input)
if __name__ == "__main__":
    sys.exit(main())
