#!/usr/bin/python3

if __name__ == "__main__":
    """The names defined in a hidden_4 module to be printed."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
