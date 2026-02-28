from typing import List, Dict, Tuple, Optional

def process_numbers(numbers: List[int]) -> Tuple[int, int, float]:
    if not numbers:
        return (0, 0, 0.0)
    min_val = min(numbers)
    max_val = max(numbers)
    avg_val = round(sum(numbers) / len(numbers), 1)
    return (min_val, max_val, avg_val)

def find_item(collection: Dict[str, int], key: str) -> Optional[int]:
    if key in collection:
        return collection[key]
    else:
        return None
