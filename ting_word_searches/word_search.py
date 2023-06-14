from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    results = []

    for file_path in instance.queue:
        lines = txt_importer(file_path["nome_do_arquivo"])

        occurrences = [
            {"linha": line_number}
            for line_number, line_content in enumerate(lines, start=1)
            if word.lower() in line_content.lower()
        ]

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_path["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return results


def search_by_word(word, instance):
    results = []

    for file_path in instance.queue:
        lines = txt_importer(file_path["nome_do_arquivo"])

        occurrences = []
        for line_number, line_content in enumerate(lines, start=1):
            if word.lower() in line_content.lower():
                occurrences.append({
                    "linha": line_number,
                    "conteudo": line_content
                })

        if occurrences:
            results.append({
                "palavra": word,
                "arquivo": file_path["nome_do_arquivo"],
                "ocorrencias": occurrences
            })

    return results