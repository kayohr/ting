from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    path = txt_importer(path_file)

    list_path = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(path),
        "linhas_do_arquivo": path,
    }

    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    instance.enqueue(list_path)
    print(list_path, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
