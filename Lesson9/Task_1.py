# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path

def delete_numbers():
    """
    Функция берет построчно текст из одного файла, и переносит его в другой, пропуская цифры
    """
    first_file = open(Path(Path.cwd(), 'test_file', 'task1_data.txt'), encoding='utf-8')
    file_line_list = first_file.readlines()
    with open(Path(Path.cwd(), 'test_file', 'task1_answer.txt'), 'w', encoding='utf-8') as second_file:
        line_in_first_file = ''

        for i in file_line_list:
            for j in i:
                if j.isdigit():
                    pass
                else:
                    line_in_first_file = line_in_first_file + j
            second_file.write(line_in_first_file)
            line_in_first_file = ''


delete_numbers()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
