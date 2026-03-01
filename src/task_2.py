from typing import List, Union, Tuple, Optional

def number_of_differences(list1: List[Union[int, str, bool]], list2: List[Union[int, str, bool]]) -> int:
    allowed_types = (int, str, bool)
    set1 = set()
    for item in list1:
        if isinstance(item, allowed_types):
            set1.add((type(item), item))
    set2 = set()
    for item in list2:
        if isinstance(item, allowed_types):
            set2.add((type(item), item))
    diff = set2 - set1
    return len(diff)

def calculate_area(shape: str, size: Union[Tuple[float, float], float]) -> Optional[float]:
    pi = 3.14159
    if not isinstance(shape, str):
        return None
    if shape == "rectangle":
        if isinstance(size, tuple) and len(size) == 2:
            a, b = size
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                area = float(a) * float(b)
                return round(area, 2)
        return None
    elif shape == "circle":
        if isinstance(size, (int, float)):
            area = pi * float(size) * float(size)
            return round(area, 2)
        return None
    else:
        return None

# print(number_of_differences([1, 2, 3], ['asd', 'qwe', 'fgh', 1, 3]))
# print(calculate_area('rectangle', (5, 4)))
# print(calculate_area('circle', (5)))