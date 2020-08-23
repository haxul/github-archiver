import wget
import json
import zipfile
import requests
import os
import shutil

# get zip files from github and put them in archive directory

url = "https://api.github.com/users/haxul/repos"

response = requests.get(url)
reps_list = json.loads(response.text)

cur_path = "/home/haxul/Development/python_development/"
new_path = cur_path + "archives"
if not os.path.exists(new_path):
    os.mkdir(new_path)

for rep in reps_list:
    wget.download(f"https://github.com/haxul/{rep['name']}/archive/master.zip")
    os.rename(f"{cur_path}{rep['name']}-master.zip", f"{new_path}/{rep['name']}.zip")
    print(f"{rep['name']} is downloaded")


# zip archive directory
def retrieve_file_paths(dir_name):
    file_dirs = []
    for root, directories, files in os.walk(dir_name):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_dirs.append(file_path)
    return file_dirs


archive_directory = cur_path + "archives"

file_paths = retrieve_file_paths(archive_directory)

print('The following list of files will be zipped:')
for file_name in file_paths:
    print(file_name)

zip_file = zipfile.ZipFile(archive_directory + '.zip', 'w')
with zip_file:
    for file in file_paths:
        zip_file.write(file)

shutil.rmtree(archive_directory)
print(archive_directory + '.zip file is created successfully!')
