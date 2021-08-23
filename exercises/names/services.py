from typing import List

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
'julian sequeira', 'sandra bullock', 'keanu reeves',
'julbob pybites', 'bob belderbos', 'julian sequeira',
'al pacino', 'brad pitt', 'matt damon', 'Brad pitt']

def clean_and_title_case_names(names: List[str]) -> List[str]:
    return list( set([name.title() for name in names]) )


def sort_by_surename(names: List[str]) -> List[str]:
    names = clean_and_title_case_names(names)
    temp = [ name.split() for name in names ]
    temp = [' '.join(reversed(x)) for x in temp]
    return sorted(
        names, reverse=True, key = lambda x: temp[names.index(x)]
    )

def find_shortest_name(names: List[str]) -> str:
    first_names = [name.split()[0] for name in names]
    sort_names = sorted(first_names, key= lambda x: len(x))
    return sort_names[0]
