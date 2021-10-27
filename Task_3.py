import os

dirfiles = os.listdir("files")

data_files = {}
for file in dirfiles:
    with open(os.path.join('files', file)) as f:
        line_count = 0
        for line in f:
            line_count += 1
        data_files.update({file: line_count})
sorted_data_files = {}
sorted_data_keys = sorted(data_files, key=data_files.get)

for w in sorted_data_keys:
    sorted_data_files[w] = data_files[w]
# print(sorted_data_files)

for file in sorted_data_files:
    temp_data = None
    with open(os.path.join('files', file)) as f:
        temp_data = f'{file}\n{sorted_data_files[file]}\n{f.read()}\n'
    with open('Result.txt', 'a') as f:
        f.write(temp_data)

print(temp_data)

