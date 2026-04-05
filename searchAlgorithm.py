import re
from typing import Union

def searchAlgo(doc: list[str], keyword: Union[str, list[str]]) -> list[str]:
    

    if not isinstance(keyword, (str,list)):
        raise TypeError(f"keyword must be a string or a list, got {TypeError(keyword).__str__}")

    if isinstance(keyword, (str, list)):
        keywordSize = set(keyword.lower().split())
    else:
        keywordSize = {kw.lower() for kw in keyword if isinstance(kw, str)}

    if not keywordSize:
        return []
    
    return [item for item in doc if isinstance(item, str)]