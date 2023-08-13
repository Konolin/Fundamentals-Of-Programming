def afisare():
    pfad = input('Pfad zur Datei: ')
    word = input('Wort zu ersetzen: ')
    replacement = input('Ersatzwort: ')

    count = replace_words(pfad, word, replacement)

    print(f"Ersetzt '{word}' durch '{replacement}' an {count} Stelle(n)")


def replace_words(pfad, word, replacement):
    f = open(pfad, 'r')
    original_lines = f.readlines()
    new_lines = []
    count = 0

    for line in original_lines:
        count += line.count(word)
        new_lines.append(line.replace(word, replacement))

    f.close()

    with open(pfad, 'w') as f:
        for line in new_lines:
            f.write(line)

    return count


afisare()
