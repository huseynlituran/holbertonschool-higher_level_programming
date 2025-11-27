#!/usr/bin/python
def write_file(filename="", text=""):
    """Fayla mətn yazır (overwrite) və yazılan simvol sayını qaytarır."""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
