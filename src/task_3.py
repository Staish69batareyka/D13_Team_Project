from typing import List, Dict, Any, Optional

def comparison_dict_and_list(dictionary: Dict[str, str], strings: List[str]) -> bool:
    return any(item in dictionary.values() for item in strings)

def get_user_info(users: List[Dict[str, Any]], name: str) -> Optional[Dict[str, Any]]:
    for user in users:
        if user.get('name') == name:
            return user
    return None