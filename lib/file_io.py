def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w", encoding="UTF-8") as file:
        file.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt", "a", encoding="UTF-8") as file:
        file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", encoding="UTF-8") as file:
        return file.read()

