from typing import List, Dict, Any


class SortUtils:
    @staticmethod
    def sort_data(
        data: List[Dict[str, Any]], key: str, reverse: bool = False
    ) -> List[Dict[str, Any]]:
        return sorted(data, key=lambda x: x[key], reverse=reverse)

    @staticmethod
    def sort_by_multiple_fields(
        data: List[Dict[str, Any]], keys: List[str], reverses: List[bool] = None
    ) -> List[Dict[str, Any]]:
        if reverses is None:
            reverses = [False] * len(keys)
        return sorted(
            data,
            key=lambda x: tuple(x[key] for key in keys),
            reverse=any(reverses),
        )
