# ler arquivos grandes


class FileIterator:
    def __init__(self, filename):  # recebo o arquivo 
        self.file = open(filename)

    def __iter__(self):            # 
        return self

    def __next__(self):
        line = self.file.readline() # faz um controle de linha
        if line != '' :
            return line

        else:
            self.file.close()
            raise StopIteration

for line in FileIterator('large_file.txt'):
    print(line)             


# se for uma lista limples
