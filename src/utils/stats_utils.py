from typing import List, Dict, Any


class StatsUtils:
    @staticmethod
    def _convert_value(value: Any) -> Any:
        if isinstance(value, str):
            if value.isdigit():
                return int(value)
            try:
                return float(value)
            except ValueError:
                pass
            if value.lower() in ("true", "false"):
                return value.lower() == "true"
            if "," in value:
                return [StatsUtils._convert_value(v.strip()) for v in value.split(",")]
        return value

    @staticmethod
    def calculate_stats(data: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        if not data:
            return {}

        stats = {}
        for key in data[0].keys():
            values = [StatsUtils._convert_value(item[key]) for item in data]
            if isinstance(values[0], (int, float)):
                stats[key] = {
                    "min": min(values),
                    "max": max(values),
                    "average": sum(values) / len(values),
                }
            elif isinstance(values[0], bool):
                stats[key] = {
                    "true_percentage": (sum(values) / len(values)) * 100,
                    "false_percentage": 100 - (sum(values) / len(values)) * 100,
                }
            elif isinstance(values[0], list):
                stats[key] = {
                    "min_length": min(len(v) for v in values),
                    "max_length": max(len(v) for v in values),
                    "average_length": sum(len(v) for v in values) / len(values),
                }
            else:
                stats[key] = {"type": "string", "values": list(set(values))}
        return stats
