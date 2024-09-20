from typing import Optional, Union, Any

def get_name(name: Optional[str] = None) -> str:
    if name:
        return name
    return "Anonim"

print(get_name("Alma"))

def process_value(vlera: Union[int, str]) -> str:
    if isinstance(vlera, int):
        return f"Number:{vlera}"
    if isinstance(vlera, float):
        return ValueError("not a float pleaseee")
    return f"STR:{vlera} "

try:
    print(process_value(2.5))
except ValueError as e:
    print(e)

def process_anything(vlera: Any)->str:
    return f"Processed {vlera}"

print(process_anything(2.5))