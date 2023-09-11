import json
import os.path


class JsonEditor:
    def __init__(self):
        self.file_path = os.path.join("saved_data", "vacancies.json")

    def add_vacancy(self, vacancy_data):
        """Запись в файл"""
        with open(self.file_path, 'w') as file:
            json_file = json.dumps(vacancy_data, indent=4, ensure_ascii=False)
            file.write(json_file)

    def clear_file(self):
        with open(self.file_path, 'w') as file:
            file.write("")
