import os
import unicodedata
import win_unicode_console
win_unicode_console.enable()

SRC = 'geojson'
OUTPUT = 'parsed'


def unicodes(string):
    return ' '.join('U+{:04X}'.format(ord(c)) for c in string)


def decode(line):
    nfd_example = unicodedata.normalize("NFD", line)
    nfd_example.encode('WINDOWS-1252', 'ignore')


for file_name in sorted(os.listdir(SRC)):
    print('current file ', file_name)
    with open(os.path.join(SRC, file_name)) as file:
        lines = file.readlines()
        new_file_data = [
            decode(data)
            for data in lines
        ]

    with open(os.path.join(OUTPUT, file_name), 'w', encoding='utf_8_sig') as file:
        file.write(''.join(lines))
