import json
import datetime
from serialization_module import to_json


# dictionary with various data types
# serializable: list, tuple, dictionary string, integer, float, boolean, none                                                                                        
entry_example = {
    'id': b'\304\x24',
    'title': "Jurassic Park: Original Motion Picture Soundtrack",
    'authors': ("John Williams", "Alexander Courage", "Conrad Pope", "John Neufeld"),
    'tracklist': {
        1: ["Opening Titles", "0:33"],
        2: ["Theme from Jurassic Park","3:27"],
        3: ["Incident at Isla Nublar", "5:20"],
        4: ["Journey to the Island", "8:52"],
        5: ["The Raptor Attack", "2:49"],
        6: ["Hatching Baby Raptor", "3:20"],
        7: ["Welcome to Jurassic Park","7:54"],
        8: ["My Friend, the Brachiosaurus", "4:16"],
        9: ["Dennis Steals the Embryo", "4:55"],
        10: ["A Tree for My Bed", "2:12"],
        11: ["High-Wire Stunts", "4:08"],
        12: ["Remembering Petticoat Lane", "2:48"],
        13: ["Jurassic Park Gate", "2:03"],
        14: ["Eye to Eye", "6:32"],
        15: ["T-Rex Rescue and Finale" "7:39"],
        16: ["End Credits" "3:26"]
    },
    'released': datetime.datetime(1993, 5, 25),
    'filmscore': True,
    'comments': None,
}


with open('basic.json', mode='w', encoding='utf-8') as f:
    json.dump(entry_example, f, indent=2, default=to_json)
