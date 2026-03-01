from typing import List, Dict, Any, Optional

def comparison_dict_and_list(dictionary: Dict[str, str], strings: List[str]) -> bool:
    return any(item in dictionary.values() for item in strings)

def get_user_info(users: List[Dict[str, Any]], name: str) -> Optional[Dict[str, Any]]:
    for user in users:
        if user.get('name') == name:
            return user
    return None

# print(comparison_dict_and_list({'asd': '1', 'qwe': '2'}, ['asd', 'zxc']))

user_list = [
     {'name': 'Ivan', 'age': 15, 'weight': 49.5, 'has_wife': False},
     {'name': 'Petr', 'age': 35, 'weight': 80.1, 'has_wife': True},
]

# print(get_user_info(user_list, 'Kirkorov'))
