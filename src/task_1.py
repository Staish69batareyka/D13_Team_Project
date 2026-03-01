from typing import List, Dict, Tuple, Optional

def process_numbers(numbers: List[int]) -> Tuple[int, int, float]:
    if not numbers:
        return None
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = round(sum(numbers) / len(numbers), 1)
    return (min_val, max_val, avg_val)

def find_item(collection: Dict[str, int], key: str) -> Optional[int]:
    if key in collection:
        return collection[key]
    else:
        return None

# print(process_numbers([1, 2, 3]))
# print(find_item({'a': 1, 'b': 2}, 'a'))