import getpass
import os
USER_NAME = getpass.getuser()
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME

file_path=os.getcwd()

def save_path(file_path):
    with open(file_path+"\\"+"config.py","w+") as config_file:
        file_path=(str(file_path).replace('\\','\\\\'))
        config_file.write('PATH = "%s"' % file_path)

def add_to_startup(file_path):
    # CREATE BAT FILE IN STARTUP
    with open(bat_path + '\\' + "Sound.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)

def delete_file(file_path):
    with open(file_path + '\\' + "delete.bat", "w+") as delete_file:
        delete_file.write(r'del "%s\Sound.bat"' % bat_path)


add_to_startup(file_path+"\main.pyw")
save_path(file_path)
delete_file(file_path)

os.system(r'"C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Sound.bat"' % USER_NAME) # RUN BAT FILE

