from typing import Optional
from config_4 import Configuration
from doctor_5 import Doctor

def main() -> str:
    config = Configuration()
    doctor = Doctor(config)
    save_answer = input("Do I need to save the recipe to the file? ")
    filename = None
    if save_answer:
        filename = input("Enter the name of the file where the recipe should be saved: ")
    recipe = doctor.write_recipe(filename)
    #print(recipe)
    return recipe


if __name__ == "__main__":
    main()