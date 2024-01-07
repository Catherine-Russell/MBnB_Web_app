from lib.user_repository import UserRepository
from lib.user import User

"""
When all is called, returns a list of all users
"""
def test_all_users_returns_lists_of_users(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'WillPat', 'makers456!'),
        User(2, 'KatyP82', 'thunderbolt*'),
        User(3, 'TomR', 'catan1234!'),
        User(4, 'BusyLizzie', 'downwarddog!')
    ]

"""
When a user is created using create, the new user appears in a list of all users
"""
def test_create_new_user(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = UserRepository(db_connection)
    new_user = User(None, 'test', 'testUser25!')
    repository.create(new_user)
    assert repository.all() == [
        User(1, 'WillPat', 'makers456!'),
        User(2, 'KatyP82', 'thunderbolt*'),
        User(3, 'TomR', 'catan1234!'),
        User(4, 'BusyLizzie', 'downwarddog!'),
        User(5, 'test', 'testUser25!')
    ]

"""
When a user is searched for using user id, the user information is returned as user class
"""
def test_search_for_user_by_user_id(db_connection):
    db_connection.seed("seeds/MBnB.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user_by_user_id(4)
    assert user == User(4, 'BusyLizzie', 'downwarddog!')
