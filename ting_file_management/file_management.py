import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, "r") as file:
            # print(file.read())
            content = file.read().split("\n")
            print(type(content))
            return content
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
