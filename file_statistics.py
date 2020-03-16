import os


def file_stats(file_path):
    if os.path.isfile(file_path):
        num_of_lines = 0
        num_of_empty_lines = 0
        num_of_lines_with_z = 0
        num_of_z_in_file = 0
        num_of_and_in_file = 0

        with open(file_path, 'r') as file:
            for line in file.readlines():
                num_of_lines += 1
                if not line.strip():
                    num_of_empty_lines += 1
                else:
                    if 'z' in line:
                        num_of_lines_with_z += 1
                        num_of_z_in_file += line.count('z')
                    num_of_and_in_file += line.count('and')

        print(f'File: {file_path}\n\t'
              f'total lines:      {num_of_lines} \n\t'
              f'empty lines:      {num_of_empty_lines}\n\t'
              f'lines with "z":   {num_of_lines_with_z}\n\t'
              f'"z" count:        {num_of_z_in_file} \n\t'
              f'lines with "and": {num_of_and_in_file}')

    else:
        print('Sorry,such file doesn`t exist!')


if __name__=='__main__':

    while True:
        file_path = input('Enter the path to the statistics file you want to find out:\n')
        file_stats(file_path)
        choice = input('Do you want to enter another file`s path? (y/n):\n')
        if choice not in ('y', 'yes'):
            break
