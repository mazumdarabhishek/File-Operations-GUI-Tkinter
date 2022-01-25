import os

class get_list_of_files:
    def __init__(self,path):
        self.path = path

    def get_list(self):
        file_list = []
        files = os.listdir(self.path)
        for file in files:
            file_list.append(file)
        return file_list



