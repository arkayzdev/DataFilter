from typing import List, Dict, Any, Callable


class FilterUtils:
    @staticmethod
    def filter_data(
        data: List[Dict[str, Any]], condition: Callable[[Dict[str, Any]], bool]
    ) -> List[Dict[str, Any]]:
        return [item for item in data if condition(item)]

    @staticmethod
    def create_condition(
        field: str, operator: str, value: Any
    ) -> Callable[[Dict[str, Any]], bool]:
        def condition(item: Dict[str, Any]) -> bool:
            match operator:
                case "==":
                    return item[field] == value
                case "!=":
                    return item[field] != value
                case ">":
                    return item[field] > value
                case "<":
                    return item[field] < value
                case ">=":
                    return item[field] >= value
                case "<=":
                    return item[field] <= value
                case "contains":
                    return value in item[field]
                case "starts_with":
                    return item[field].startswith(value)
                case "ends_with":
                    return item[field].endswith(value)
                case _:
                    raise ValueError(f"Unsupported operator: {operator}")

        return condition
