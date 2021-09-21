

import json
import os


def txt_to_nestedlist(file_name, dir_location):

    complete_path = os.path.join(dir_location, file_name + ".txt")
    print(complete_path)
    try:
        with open(complete_path, 'r') as file_read:
            list_out = []
            for line in file_read:
                list_line = line.split()  # transforms into list and ditches '\n'
                list_out.append(list_line)
            file_read.close()
    except FileNotFoundError:
        print("Wrong directory or file could not be reached")
        return []
    else:
        print("Data successfully retrieved")
        return list_out


if __name__ == '__main__':
    print(txt_to_nestedlist('test', ''))





