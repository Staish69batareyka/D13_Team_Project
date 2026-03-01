import os
import json
from typing import Optional
from config_4 import Configuration

class Doctor:
    def __init__(self, config: Configuration) -> None:
        self.config = config
        doctor_file_path = os.path.join(
            os.getcwd(),
            config.base_folder,
            "doctors",
            f"{config.login}.json"
        )
        with open(doctor_file_path, "r", encoding="utf-8") as file:
            doctor_data = json.load(file)
            
        surname = doctor_data.get("Surname", "")
        name = doctor_data.get("Name", "")
        patronymic = doctor_data.get("Patronymic", "")
        self.name = f"{surname} {name} {patronymic}".strip()
        
        self.speciality = doctor_data.get("Speciality", "")
    
    def __write_receipt_to_file(self, recipe: str, filename: str) -> None:
        file_path = os.path.join(
            os.getcwd(),
            self.config.base_folder,
            f"{filename}.txt"
        )
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(recipe)
    
    def write_recipe(self, filename: Optional[str] = None) -> str:
        print("Enter recipe (to finish press Enter twice):")
        lines = []
        empty_count = 0
        while True:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count == 2:
                    break
            else:
                lines.append(line)
                empty_count = 0
        recipe_text = "\n".join(lines)
        signed_recipe = f"{recipe_text}\n\n{self.name}\nDoctor-{self.speciality}"
        if filename is not None:
            self.__write_receipt_to_file(signed_recipe, filename)
        return signed_recipe