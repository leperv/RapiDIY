import re
from src.Engine.engine_consts import QUERY_REGEX

def extract_query(response : str):
    match = re.search(QUERY_REGEX, response)
    if  not match:
        raise ValueError('Query response did not match expected format')
    return match.group(1)