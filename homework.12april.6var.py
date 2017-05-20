import os
import re
def open_folder(my_folder):
    folder_names= [item for item in os.listdir(my_folder)if os.path.isfile(item) and re.search('[^.]*\..*?[,.""!-(_?<>'')].*?',str(item)[::-1])]
    return len(folder_names)
print('Количество файлов:',open_folder ('.'))
