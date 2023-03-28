from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    new_dict = {}
    for i in args:
        for k in i.keys():
            if k in new_dict.keys():
                new_dict[k] += i[k]
            else:
                new_dict[k] = i[k]
    return new_dict

