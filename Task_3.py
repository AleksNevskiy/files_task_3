import os

def line_counter(path):
    dirfiles = os.listdir(path)
    data_files = {}
    for file in dirfiles:
        with open(os.path.join(path, file)) as f:
            line_count = 0
            for line in f:
                line_count += 1
            data_files.update({file: line_count})
    return data_files

def sorting_dict(dict):
    sorted_data_files = {}
    sorted_data_keys = sorted(dict, key=dict.get)
    for w in sorted_data_keys:
        sorted_data_files[w] = dict[w]
    return sorted_data_files
    # print(sorted_data_files)

def writing_sorted(dict, path):
    for file in dict:
        with open(os.path.join(path, file)) as f:
            temp_data = f'{file}\n{dict[file]}\n{f.read()}\n'
        with open('Result.txt', 'a') as f:
            f.write(temp_data)

# line_counter("files")
# sorting_dict(line_counter("files"))
writing_sorted(sorting_dict(line_counter("files")), "files")
# print(temp_data)

