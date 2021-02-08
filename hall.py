class Hall:
    def __init__(self, title = None, city = None, address = None, category = None, picture = None, owner = None, phone = None, description = None, several_places = None, price = None):
        self.title = title
        self.city = city
        self.address = address
        self.category = category
        self.picture = picture
        self.owner = owner
        self.phone = phone
        self.description = description
        self.several_places = several_places
        self.price = price


def get_hall_from_dict(hall_dict):
    hall = Hall(hall_dict["title"], hall_dict["city"], hall_dict["address"], hall_dict["category"], hall_dict["picture"], hall_dict["owner"], hall_dict["phone"], hall_dict["description"], hall_dict["several_places"], hall_dict["price"])
    return hall