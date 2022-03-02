class Property:
    """This class will represent a property"""

    def __init__(
        self,
        locality: str = None,
        _type: str = None,
        sub_type: str = None,
        price: float = None,
        type_of_sale: str = None,
        amount_of_rooms: int = None,
        area: int = None,
        has_full_kitchen: int = None,
        is_furnished: bool = None,
        has_open_fire: bool = None,
        has_terrace: bool = None,
        terrace_area: int = None,
        has_garden: bool = None,
        garden_area: int = None,
        surface_land: int = None,
        surface_area_plot: int = None,
        amount_of_facades: int = None,
        has_pool: bool = None,
        building_state: str = None,
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

    header = [
        "locality",
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
        "building_state",
    ]
