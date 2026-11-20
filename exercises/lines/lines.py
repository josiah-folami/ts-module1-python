import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py filename.py")
        return

    filename = sys.argv[1]

    if not filename.lower().endswith(".py"):
        print("Please provide a .py file.")
        return

    try:
        with open(filename, encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return
    except OSError as error:
        print(f"Could not read the file: {error}")
        return

    code_lines = [
        line for line in lines
        if line.strip() and not line.lstrip().startswith("#")
    ]
    print(len(code_lines))


if __name__ == "__main__":
    main()