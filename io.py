import os, shelve, shutil, send2trash, json

name = input("What's your name?\n")
age = int(input("Age?\n"))
print("Name : {}  Age : {}".format(name,age))

def print_file(filename):
    """Prints the contents of a file"""
    f = open(filename)
    print(f.read())
    f.close()

filename = "temp.txt"

#write to a file
temp_file = open(filename,'w')
temp_file.write('First line.\nSecond line.\n')
temp_file.close()

print_file(filename)

#append to file
temp_file = open('temp.txt','a')
temp_file.write('Third line')
temp_file.close()

print_file(filename)

print(os.path.join('home','plog','Desktop'))
print(os.getcwd())
os.chdir('modules')
print(os.getcwd())
os.chdir('../')
print(os.getcwd())

if not os.path.exists('./files_demo'):
    os.mkdir('./files_demo')

print(os.path.getsize('./temp.txt'))
print(os.listdir('./'))

print(os.path.isdir('./files_demo'))
print(os.path.isfile('./temp.txt'))

shelf = shelve.open('shelve_test')
langs = ['python', 'java', 'php']
shelf['langs'] = langs
shelf.close()

shelf = shelve.open('shelve_test')
print(shelf['langs'])
shelf.close()

shutil.copy('./temp.txt','./files_demo')
shutil.copytree('./modules','./modules_backup')
shutil.move('./temp.txt','./files_demo/temp_backup.txt')

if not os.path.exists('./files_demo_2'):
    os.mkdir('./files_demo_2')

shutil.move('./files_demo_2','files_demo')
shutil.move('./shelve_test','./files_demo/files_demo_2')

send2trash.send2trash('./files_demo')
send2trash.send2trash('./modules_backup')

for folderName, subfolders, filenames in os.walk('./'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'
parsed_json = json.loads(json_string)
print(parsed_json['first_name'])
print(json.dumps(parsed_json))