#!/usr/bin/python3
def read_file(filename=""):
    with open("my_file_0.txt", mode="r", encoding="utf-8") as f:
        lines = f.read()
        print(lines)
    f.closed