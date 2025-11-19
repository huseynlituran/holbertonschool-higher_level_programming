#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    visible_names = []

    for name in names:
        if not name.startswith("__"):
            visible_names.append(name)

    visible_names.sort()

    for name in visible_names:
        print(name)
