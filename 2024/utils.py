from pathlib import Path

def readFile(path):
    file1 = open(Path(__file__).parent / "inputs" / path, 'r')
    return file1.readlines()