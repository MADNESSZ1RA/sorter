import os

path = input('Введите путь: ')
files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
print(files)

extention = list(set([file.split('.')[-1] for file in files]))

for abc in extention:
    try:
        os.mkdir(os.path.join(path, abc))
    except:
        pass
    for bca in files:
        try:
            if bca.endswith(abc):
                os.replace(os.path.join(path, bca), os.path.join(path, abc, bca))
        except:
            pass