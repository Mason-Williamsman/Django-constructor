import os
import codecs
import pathlib

def read_a_file(path):

    encoder = 'UTF-8'

    with codecs.open(path, 'r', encoder) as f1:
        readed_data = f1.read()
        f1.close()
    return readed_data


def write_a_file(path, filename, new_data):
    with codecs.open(path + filename, 'w') as f2:
        f2.write(new_data)
    f2.close()


def path_fixer(directory):
    path = [directory, '', '']

    last_symbol = ([i for i in path[0][::-1]][0])

    def check_last_symbol(last_symbol):
        if (([i for i in path[0][::-1]][0]) == '/'):
            return True
        else:
            return False

    if check_last_symbol(last_symbol):
        print(last_symbol + ' exist')
        return directory
    else:
        last_symbol_fix = (directory + '/')
        print(last_symbol_fix + ' fixed')
        return last_symbol_fix


class DirCreateClass:
    def __init__(self, path):
        self.path = path

    def dir_create(self):
        if self.path:
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            else:
                print("dir structuree \"" + self.path + "\" already exist!")
        else:
            pass


class FileReplacerClass:
    def __init__(self, map_data):
        self.read_maped_file = map_data["target_to_read_sutf8"]
        self.write_maped_file = map_data["target_to_write_file"]
        self.old_map_data = map_data["old_data"]
        self.new_map_data = map_data["new_data"]
        self.directory = map_data["directory"]

    def fileReplacer(vars):

        dir = path_fixer(vars.directory)

        old_data_file = read_a_file(vars.read_maped_file)
        new_data = old_data_file.replace(vars.old_map_data,
                                         vars.new_map_data)

        cdir = DirCreateClass(path_fixer(dir))
        cdir.dir_create()

        write_a_file(dir, vars.write_maped_file, new_data)


class FileAppenderClass:
    def __init__(self, map_data):
        self.read_maped_file = map_data["target_to_read_sutf8"]
        self.write_maped_file = map_data["target_to_write_file"]
        self.new_data_set = map_data["substitution_set"]
        self.directory = map_data["directory"]

    def fileReplacer(vars):
        dir = path_fixer(vars.directory)
        old_data_file = read_a_file(vars.read_maped_file)
        new_data = (old_data_file % vars.new_data_set)
        cdir = DirCreateClass(path_fixer(dir))
        cdir.dir_create()
        write_a_file(dir, vars.write_maped_file, new_data)


class FileAppenderClassTest:
    def __init__(self, path):
        self.path = path

    def prin_path(vars):
        cwd6 = pathlib.Path(__file__).parent.resolve()

