import os

for folder in os.listdir(".."):
    if os.path.isdir(f'..\\{folder}'):
        for innerFolder in os.listdir(f'..\\{folder}'):
            if innerFolder == "migrations":
                for file in os.listdir(f'..\\{folder}\\{innerFolder}'):
                    if '__' not in file:
                        print(f"Removing {file}")
                        os.remove(f'..\\{folder}\\{innerFolder}\\{file}')