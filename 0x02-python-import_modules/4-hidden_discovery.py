#!/usr/bin/python3

if __name__ == "__main__":
    """prints names from hidden_4.py line by line"""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
