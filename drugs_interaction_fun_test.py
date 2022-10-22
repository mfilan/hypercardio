import os

import pandas as pd


def drag_interaction(search_drugs: list, new_drug: str) -> list:
    df = pd.read_csv(os.path.join("data", "drug_interactions.csv"), encoding='utf-8')
    search_drugs = [i.lower() for i in search_drugs]

    df.loc[:, 'drug_name'] = df.loc[:, 'drug_name'].str.lower()
    df.loc[:, 'name'] = df.loc[:, 'name'].str.lower()
    result = df[(df['drug_name'].isin(search_drugs)) & (df['name'] == new_drug.lower())]
    print(result.to_dict(orient='index').values())

    return "dupa"


if __name__ == '__main__':
    print(drag_interaction(['Abilify', 'Abilify Maintena', 'Allegra'], 'amoxapine'))  # wstępna wersja algorytmu
