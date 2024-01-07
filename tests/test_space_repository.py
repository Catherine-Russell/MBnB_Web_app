from lib.space_repository import SpaceRepository
from lib.space import Space

"""
Tests:
    - when we read all spaces, we see a list of all spaces
    - when we create a new space, it is displayed in the list of all spaces
    - When we call find_space_by_title, we see the space displayed
    TODO:
    - when we update a space, we see the change in the list of all spaces X
    - when we delete a space X
"""

# when we read all spaces, we see a list of all spaces in database

def test_list_all_spaces(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
        Space(1, 'Mediterranean Villa', 'Nice', 'France', 'In the heart of local life, this charming villa has superb panoramic views of the sea. You have the beach within easy reach, but are not too far away from the city to enjoy all the amenities Nice has to offer.', 281, 2, 'static/images/mediterraneanVilla.jpeg', 5),
        Space(2, 'English Cottage', 'Wimborne', 'UK', 'This chocolate box 16th Century Grade II listed cottage is full of the character you would expect from such an old property yet with just the right degree of up-dating to give you a comfortable stay: the perfect country retreat!', 150, 4, 'static/images/cottage.jpeg', 6),
        Space(3, 'Alpine lodge', 'Brig-Glis', 'Switzerland', 'Welcome to our lovely cosy chalet. We are located in a quiet car free village, only reachable by cablecar. Enjoy an incredible view of stunning mountains from your bedroom. Perfect for hiking, skiing and relaxing.', 105, 1, 'static/images/snowyCabin.jpeg', 6),
        Space(4, 'Studio Apartment', 'New York', 'USA', 'Luxury 1 Bedroom in the heart of NYC! Central to all shopping, restaurants, and attractions. Highrise Apartment with Floor to Ceiling windows provide a breathtaking view of the River and Skyline.', 197, 2, 'static/images/studioApartment.jpeg', 2),
        Space(5, 'Tent', 'Tenby', 'UK', 'A 5 metre, cotton canvas bell tent which can comfortably accommodate up to 4 people with any combination of single beds or double bed, duvets and pillows with linen, rugs, blankets, cushions, lighting, side tables, seating and plants.', 75, 2, 'static/images/tent.jpeg', 4),
        Space(6, 'Bamboo Cabin', 'Tampaksiring', 'Indonesia', 'Located just a 20-minute scooter ride from the vibrant centre of Ubud, the Dome is a newly built one bedroom bamboo cabin situated within the Eco Six Resort.', 230, 3, 'static/images/cabin.jpeg', 3)
    ]


# - when we create a new space, it is displayed in the list of all spaces
def test_create_a_new_space(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    repository.create(Space(None, 'Test', 'Test', 'Test', 'Test', 5, 3, 'images/test.jpeg', 3))
    assert repository.all() == [
        Space(1, 'Mediterranean Villa', 'Nice', 'France', 'In the heart of local life, this charming villa has superb panoramic views of the sea. You have the beach within easy reach, but are not too far away from the city to enjoy all the amenities Nice has to offer.', 281, 2, 'static/images/mediterraneanVilla.jpeg', 5),
        Space(2, 'English Cottage', 'Wimborne', 'UK', 'This chocolate box 16th Century Grade II listed cottage is full of the character you would expect from such an old property yet with just the right degree of up-dating to give you a comfortable stay: the perfect country retreat!', 150, 4, 'static/images/cottage.jpeg', 6),
        Space(3, 'Alpine lodge', 'Brig-Glis', 'Switzerland', 'Welcome to our lovely cosy chalet. We are located in a quiet car free village, only reachable by cablecar. Enjoy an incredible view of stunning mountains from your bedroom. Perfect for hiking, skiing and relaxing.', 105, 1, 'static/images/snowyCabin.jpeg', 6),
        Space(4, 'Studio Apartment', 'New York', 'USA', 'Luxury 1 Bedroom in the heart of NYC! Central to all shopping, restaurants, and attractions. Highrise Apartment with Floor to Ceiling windows provide a breathtaking view of the River and Skyline.', 197, 2, 'static/images/studioApartment.jpeg', 2),
        Space(5, 'Tent', 'Tenby', 'UK', 'A 5 metre, cotton canvas bell tent which can comfortably accommodate up to 4 people with any combination of single beds or double bed, duvets and pillows with linen, rugs, blankets, cushions, lighting, side tables, seating and plants.', 75, 2, 'static/images/tent.jpeg', 4),
        Space(6, 'Bamboo Cabin', 'Tampaksiring', 'Indonesia', 'Located just a 20-minute scooter ride from the vibrant centre of Ubud, the Dome is a newly built one bedroom bamboo cabin situated within the Eco Six Resort.', 230, 3, 'static/images/cabin.jpeg', 3),
        (Space(7, 'Test', 'Test', 'Test', 'Test', 5, 3, 'images/test.jpeg', 3))
    ]

# When we call find_space_by_title, we see the space displayed

def test_find_space_by_name_returns_single_space(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = SpaceRepository(db_connection)
    space = repository.find_by_space_name("Alpine lodge")
    assert space == Space(3, 'Alpine lodge', 'Brig-Glis', 'Switzerland', 'Welcome to our lovely cosy chalet. We are located in a quiet car free village, only reachable by cablecar. Enjoy an incredible view of stunning mountains from your bedroom. Perfect for hiking, skiing and relaxing.', 105, 1, 'static/images/snowyCabin.jpeg', 6)