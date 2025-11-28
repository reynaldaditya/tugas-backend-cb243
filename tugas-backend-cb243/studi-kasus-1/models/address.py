class Address:
    def __init__(self, street: str, city: str, state: str, postal_code: str, country: str = "Indonesia"):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def get_full_address(self) -> str:
        return f"{self.street}, {self.city}, {self.state} {self.postal_code}, {self.country}"

    def update_address(self, street: str = None, city: str = None, 
                      state: str = None, postal_code: str = None, country: str = None) -> None:
        if street:
            self.street = street
        if city:
            self.city = city
        if state:
            self.state = state
        if postal_code:
            self.postal_code = postal_code
        if country:
            self.country = country

    def __str__(self) -> str:
        return self.get_full_address()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Address):
            return False
        return (self.street == other.street and
                self.city == other.city and
                self.state == other.state and
                self.postal_code == other.postal_code and
                self.country == other.country)

    def __repr__(self) -> str:
        return (f"Address(street='{self.street}', city='{self.city}', "
                f"state='{self.state}', postal_code='{self.postal_code}', country='{self.country}')")