from ..operators.file_maker import FileReplacerClass, FileAppenderClass, FileAppenderClassTest


app_name_l = "test_part_8"
structures_source_path_default = ("/sourse_apps_structures/")
target_path_default = "/home/www/Documents/Django_constructor_ENV/public_applications/Django-constructor/django_constructor/"


def create_file(source_path, source_file_name, target_path, target_file_name, values):
    frc = FileAppenderClass(map_data = {
    "target_to_read_sutf8" : (source_path + source_file_name),
    "target_to_write_file"  : target_file_name,
    "substitution_set" : values,
    "directory" : target_path,
    })

    frc.fileReplacer()


class CreateAppClass:
    def __init__(self, app_name, path):
        app_name_input = app_name
        app_name_valid = app_name_input # validation input data
        self.app_name = app_name_valid
        self.path = path


    def app_create(self):
        if self.app_name:
            frc = FileAppenderClassTest(self.path)
            frc.prin_path()
            def create_substitution_test(path, app_name):
                source_file_name = "test.tpl"
                target_file_name = "test.py"
                values = (
                    "question_one__________",
                    "answer2_______",
                    "var3___________"
                )
                create_file(path,
                            source_file_name,
                            (target_path_default + app_name),
                            target_file_name,
                            values)
            create_substitution_test(self.path + structures_source_path_default, self.app_name)
        else:
            pass
