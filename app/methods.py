from app.models import MainMenu, Users, Posts
from app import db
from sqlalchemy import select


def get_menu():
    try:
        res = MainMenu.query.all()
        print(res)
        if res:
            return res
    except:
        print("Ошибка чтения из БД")
    return []


def getPostsAnounce():
    try:
        res = Posts.query.order_by(Posts.datetime.desc()).all()
        print(res)
        if res:
            return res
    except Exception as ex:
        print("Ошибка чтения из БД", ex)
    return []


def get_post(post_id):
    try:
        res = Posts.query.where(Posts.id == post_id).one()
        print(res)
        if res:
            return res
    except Exception as ex:
        print("Ошибка чтения из БД", ex)

    return {}


def getUserByEmail(email):
    try:
        row = Users.query.where(Users.email == email).one()
        if not row:
            print("Пользователь не найден")
            return False
        return row
    except Exception as ex:
        print("Ошибка чтения из БД", ex)

    return {}


def getUser(user_id):
    try:
        res = Users.query.where(Users.id == user_id).one()
        if not res:
            print("Пользователь не найден")
            return False
        return res
    except Exception as ex:
        print("Ошибка чтения из БД", ex)

    return {}