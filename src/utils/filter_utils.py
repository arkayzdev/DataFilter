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
            if operator in [">", "<", ">=", "<="]:
                try:
                    item_value = float(item[field])
                    casted_value = float(value)
                except ValueError:
                    raise TypeError(
                        f"Cannot compare {item[field]} with {value} using {operator}"
                    )
            else:
                item_value = item[field]
                casted_value = value
            match operator:
                case "==":
                    return str(item_value) == str(casted_value)
                case "!=":
                    return str(item_value) != str(casted_value)
                case ">":
                    return item_value > casted_value
                case "<":
                    return item_value < casted_value
                case ">=":
                    return item_value >= casted_value
                case "<=":
                    return item_value <= casted_value
                case "contains":
                    return str(casted_value) in str(item[field])
                case "starts_with":
                    return str(item[field]).startswith(str(casted_value))
                case "ends_with":
                    return str(item[field]).endswith(str(casted_value))
                case _:
                    raise ValueError(f"Unsupported operator: {operator}")

        return condition
