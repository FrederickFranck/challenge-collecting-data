import csv

class Property:
    """This class will represent a property"""

    def __init__(self) -> None:
        self.locality: str = None
        self.type: str = None
        self.sub_type: str = None
        self.price: float = None
        self.type_of_sale: str = None
        self.amount_of_rooms: int = None
        self.area: int = None
        self.has_full_kitchen: bool = None
        self.is_furnished: bool = None
        self.has_open_fire: bool = None
        self.has_pool: bool = None
        self.has_terrace: bool = None
        self.terrace_area: int = None
        self.has_garden: bool = None
        self.garden_area: int = None
        self.surface_land: int = None
        self.surface_area_plot: int = None
        self.amount_of_facades: int = None
        self.building_state: str = None

    def __init__(
        self,
        locality: str,
        _type: str,
        sub_type: str,
        price: float,
        type_of_sale: str,
        amount_of_rooms: int,
        area: int,
        has_full_kitchen: int,
        is_furnished: bool,
        has_open_fire: bool,
        has_terrace: bool,
        terrace_area: int,
        has_garden: bool,
        garden_area: int,
        surface_land: int,
        surface_area_plot: int,
        amount_of_facades: int,
        has_pool: bool,
        building_state: str,
    ) -> None:

        self.locality: str = locality
        self.type: str = _type
        self.sub_type: str = sub_type
        self.price: float = price
        self.type_of_sale: str = type_of_sale
        self.amount_of_rooms: int = amount_of_rooms
        self.area: int = area
        self.has_full_kitchen: bool = has_full_kitchen
        self.is_furnished: bool = is_furnished
        self.has_open_fire: bool = has_open_fire
        self.has_pool: bool = has_pool
        self.has_terrace: bool = has_terrace
        self.terrace_area: int = terrace_area
        self.has_garden: bool = has_garden
        self.garden_area: int = garden_area
        self.surface_land: int = surface_land
        self.surface_area_plot: int = surface_area_plot
        self.amount_of_facades: int = amount_of_facades
        self.building_state: str = building_state

    def __iter__(self) -> None:
        return iter(
            [
                self.locality,
                self.type,
                self.sub_type,
                self.price,
                self.type_of_sale,
                self.amount_of_rooms,
                self.area,
                self.has_full_kitchen,
                self.is_furnished,
                self.has_open_fire,
                self.has_terrace,
                self.terrace_area,
                self.has_garden,
                self.garden_area,
                self.surface_land,
                self.surface_area_plot,
                self.amount_of_facades,
                self.has_pool,
                self.building_state,
            ]
        )

    header = ["locality",
               "type",
               "sub_type",
               "price",
               "type_of_sale",
               "amount_of_rooms",
               "area",
               "has_full_kitchen",
               "is_furnished",
               "has_open_fire",
               "has_terrace",
               "terrace_area",
               "has_garden",
               "garden_area",
               "surface_land",
               "surface_area_plot",
               "amount_of_facades",
               "has_pool",
               "building_state"]


test = Property(
    "De Panne",
    "House",
    "rijhuis",
    299000,
    "normal",
    4,
    284,
    True,
    True,
    False,
    False,
    None,
    False,
    None,
    193,
    284,
    2,
    False,
    "normal"
)
t = [test,test]

with open("test.csv","w",newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(Property.header)
    writer.writerows(t)

print("test")