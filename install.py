import getpass
import os
USER_NAME = getpass.getuser()


file_path=os.getcwd()

def save_path(file_path):
    with open(file_path+"\\"+"config.py","w+") as py_file:
        py_file.write('PATH = "%s"' % file_path)

def add_to_startup(file_path):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME # CREATE BAT FILE IN STARTUP
    with open(bat_path + '\\' + "Sound.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)

add_to_startup(file_path+"\main.pyw")
save_path(file_path)

os.system(r'"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Sound.bat"' % USER_NAME) # RUN BAT FILE

