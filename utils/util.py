
def _wrap(color: str, text: str) -> str:
    colors = {
        "r": "\033[91m", 
        "g": "\033[92m", 
        "y": "\033[93m",
        "b": "\033[94m", 
        "m": "\033[95m", 
        "c": "\033[96m"
    }
    return f"{colors.get(color, '')}{text}\033[0m"

def pp(module: str, info: str, color='c') -> None:
    tag = _wrap(color, f"[{module.upper()} CONFIG]")
    print(f"{tag} {info}")