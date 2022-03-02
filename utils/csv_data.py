import pandas as pd
from typing import List, Dict, Union, Optional

def raw_to_csv(list_of_properties: List[Dict[str, Optional[Union[str,float,int]]]]) -> None:
    '''
    A function that will create two CSV files with the provided list of properties ( estates ).
    User needs to specify each file name (raw and clean), the file is created in the same directory as main.py.
    list_of_properties: a list of dictionaries containing the properties
    '''

    raw_table = pd.DataFrame(list_of_properties)
    raw_table.to_csv(f"Immoweb_Data_Scraper.csv")

def _cleaner(table: pd.DataFrame) -> pd.DataFrame:
    '''
    This function cleans up the DataFrame by reordering columns, converting some columns
    into binary values and taking care of NaN values.
    '''
    cols = table.columns.tolist()
    # Reordering columns
    cols = [cols[10], cols[0], cols[9], cols[11], cols[12], cols[14], cols[15], cols[16], cols[1], cols[2], cols[13],
            cols[5], cols[4], cols[6], cols[7], cols[8], cols[3]]
    table = table[cols]

    # Converting into int and NaN by None
    table.bedroomCount = table.bedroomCount.fillna(333)
    table = table.astype({"bedroomCount": int})
    table.bedroomCount = table.bedroomCount.replace({333: None})

    # Converting into int and NaN by None
    table.facadeCount = table.facadeCount.fillna(333)
    table = table.astype({"facadeCount": int})
    table.facadeCount = table.facadeCount.replace({333: None})

    # Converting into binary values
    table.loc[table.kitchen.isin(['INSTALLED', 'SEMI_EQUIPPED', 'NOT_INSTALLED']), 'kitchen'] = False
    table.loc[table.kitchen.isin(['HYPER_EQUIPPED', 'USA_HYPER_EQUIPPED', 'USA_INSTALLED']), 'kitchen'] = True

    # Replacing NaN by None
    table.fillna('£%+¨')
    table.replace({'£%+¨': None})

    return table