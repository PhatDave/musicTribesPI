import os

for folder in os.listdir(".."):
    if os.path.isdir(folder):
        for innerFolder in os.listdir(folder):
            if innerFolder == "migrations":
                for file in os.listdir(f'{folder}\\{innerFolder}'):
                    if '__' not in file:
                        os.remove(f'{folder}\\{innerFolder}\\{file}')