from typing import Any, Iterable, Optional

def sum_numbers(
    numbers: Optional[Iterable[Any]] = None
) -> int:
    return sum(numbers) if numbers else sum(range(1,101))
