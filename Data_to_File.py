
# Picks up a list, tuple or hash table and write out to a .txt file to go somewhere else
# This contrasts with the Data program
import json
import os  # for saving in a given directory


def nestedlist_to_txt(in_list, indir, file_name):
    if not isinstance(in_list, list):
        raise TypeError("Input variable is not a List")  # better with try, except?

    complete_path = os.path.join(indir,  file_name+".txt")

    try:
        with open(complete_path, 'w') as file:
            s = ""
            for it1 in in_list:
                # it1 = it1 if isinstance(it1, list) else [it1]  # TODO loop without needing the if
                # we assume that the list is nested to loop through and write
                for it2 in it1:
                    s = s + str(it2) + ' '
                s += '\n'
            file.write(s)
            file.close()
    except FileNotFoundError:
        print("Directory provided does not exist")
        return False
    else:
        print("File written successfully")
        return True
    # if os.path.exists(dir):
    #     with open(complete_path, 'w') as file:
    #         s = ""
    #         for it in in_list:
    #             s = s + str(it) + ' '
    #
    #         file.write(s)
    # else:
    #     print("Directory provided does not exist")
    #     raise FileNotFoundError

def dict_to_txt(in_dict, write_path, file_name):



def list_to_json(in_list, indir, file_name):
    if not isinstance(in_list, list):
        raise TypeError("Input variable is not a List")

    complete_path = os.path.join(indir,  file_name+".json")
    with open(complete_path, 'w') as w_file:
        json.dump(in_list, w_file)


if __name__ == '__main__':
    li = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    path = "/home/eduardo/Documents/Python/UtilsPY"
    h = nestedlist_to_txt(li, path, "test")  # nas células unidimensionais aparece separado
# TODO better testing for bi-dimensional arrays, problems with string inputs occurred
