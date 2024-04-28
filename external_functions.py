from bot_base import session_maker, General
from random import randint

def insert_new_user_in_general_table(user_tg_id: int, name: str):
    with session_maker() as session:
        needed_data = session.query(General).filter(General.id == user_tg_id).first()
        if not needed_data:
            new_us = General(id=user_tg_id, user_name=name)
            session.add(new_us)
            session.commit()
        else:
            needed_data.wins = needed_data.total_games = needed_data.secret_number = needed_data.in_game = 0
            needed_data.attempts = 5
            session.commit()

def verify_that_user_into_general(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General).filter(General.id == user_tg_id).first()
    return needed_data

def verify_INGAME_status(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General.in_game).filter(General.id == user_tg_id).scalar()
    return needed_data


def cancel_update(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General).filter(General.id == user_tg_id).first()
        needed_data.in_game = 0
        needed_data.attempts = 5
        session.commit()


def choosing_number(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General).filter(General.id == user_tg_id).first()
        needed_data.in_game = 1
        needed_data.secret_number = randint(1, 100)
        session.commit()

def get_secret_number(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General.secret_number).filter(General.id == user_tg_id).scalar()
        if needed_data:
            return needed_data
        return "This Name Does Not Exist"


def update_after_user_wins(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General).filter(General.id == user_tg_id).first()
        needed_data.in_game =  needed_data.secret_number = 0
        needed_data.wins+=1
        needed_data.total_games+=1
        needed_data.attempts=5
        session.commit()

def minus_one_attempt(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General).filter(General.id == user_tg_id).scalar()
        needed_data.attempts -= 1
        session.commit()

def check_attempts_lost_number(user_tg_id: int):
    with session_maker() as session:
        att_number = session.query(General.attempts).filter(General.id == user_tg_id).scalar()
        if att_number == 0:
            return True
        return False


def user_lost(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(General).filter(General.id == user_tg_id).first()
        needed_data.in_game =  needed_data.secret_number = 0
        needed_data.total_games+=1
        needed_data.attempts=5
        session.commit()

