from .models import db, BoatType, User


def import_boats():
    boats = [
        {"id": 0, "name": "SailNavSim Classic"},
        {"id": 1, "name": "Seascape 18"},
        {"id": 2, "name": "Contessa 25"},
        {"id": 3, "name": "Hanse 385"},
        {"id": 4, "name": "Volvo 70"},
        {"id": 5, "name": "Super Maxi Scallywag"},
        {"id": 6, "name": "140-foot Brigantine"},
        {"id": 7, "name": "Maxi Trimaran"},
        {"id": 8, "name": "IMOCA 60"},
        {"id": 9, "name": "Improvised Lifeboat"}
        ]


    for boat in boats:
        boattype = BoatType()
        boattype.id = boat["id"]
        boattype.name = boat["name"]
        db.session.add(boattype)
        db.session.commit()
        print(f"Boat {boat['name']} Imported!")

def import_users():
    users = [
        {"id": 1, "name": "Andrew Holway", "email": "andrew.holway@gmail.com", "password": "sha256$F2xBXoSW$e57f1b72dcbf6514c797612c0521934f8535034a2dc0c652d345cc811ca26e6a", "website": "https://www.skill-sprint.com"},
        {"id": 2, "name": "Bobby Brown", "email": "bobby.brown@gmail.com", "password": "sha256$F2xBXoSW$e57f1b72dcbf6514c797612c0521934f8535034a2dc0c652d345cc811ca26e6a", "website": "https://www.skill-sprint.com"},
        {"id": 3, "name": "Dick Tracy", "email": "dick.tracy@gmail.com", "password": "sha256$F2xBXoSW$e57f1b72dcbf6514c797612c0521934f8535034a2dc0c652d345cc811ca26e6a", "website": "https://www.skill-sprint.com"}
    ]

    for user in users:
        _user = User()
        _user.id = user["id"]
        _user.name = user["name"]
        _user.email = user["email"]
        _user.password = user["password"]
        _user.website = user["website"]
        db.session.add(_user)
        db.session.commit()
        print(f"User {user['name']} Imported!")