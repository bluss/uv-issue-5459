import sys
import subprocess


def main():
    # yeah I'll just execute whatever command you give me
    if sys.argv[1:]:
        subprocess.call(sys.argv[1:])


if __name__ == "__main__":
    main()
