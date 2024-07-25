import sys


def main():
    try:
        import jinja2
    except ImportError:
        print("Pass, all is good")
    else:
        print("What? I thought I was isolated.. nooo")

    print("This is my sys path:")
    for elt in sys.path:
        print(elt)


if __name__ == "__main__":
    main()
