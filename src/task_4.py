import json
import os
from typing import Dict, Any
from config_4 import Configuration

def main() -> Dict[str, Any]:
    """
    Основная функция, которая читает карточку врача по логину из конфига
    
    Returns:
        Dict[str, Any]: словарь с данными врача из JSON файла
    """
    config = Configuration()
    # Путь: base_folder/doctors/login.json
    file_path = os.path.join(
        config.base_folder, 
        "doctors", 
        f"{config.login}.json"
    )
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
    
    with open(file_path, "r", encoding="utf-8") as file:
        doctor_data: Dict[str, Any] = json.load(file)
    
    return doctor_data

if __name__ == "__main__":
    result = main()
    #print(result)