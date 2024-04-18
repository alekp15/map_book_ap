users: list[dict] = [
    {"name": "Alek", "surname": "Piasek", "posts": 15},
    {"name": "Maciej", "surname": "Przybytek", "posts": 45},
    {"name": "Bartosz", "surname": "Pietrasik", "posts": 61},
    {"name": "Tymoteusz", "surname": "Miszczak", "posts": 21},
    {"name": "Mateusz", "surname": "Matysiak", "posts": 33},
]


def create_user(users: list[dict])->None:
    name: str = input("Podaj imię użytkownika: ")
    surname: str = input("Podaj nazwisko użytkownika: ")
    posts: int = int(input("Podaj liczbę postów: "))
    user: dict = {"name": name, "surname": surname, "posts": posts}
    users.append(user)

create_user(users)
print(users)