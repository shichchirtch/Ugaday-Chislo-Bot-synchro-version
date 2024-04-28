from bot_base import session_maker, One_game, General

def INSERT_IN_GAME_TABLE(user_tg_id: int):
    with session_maker() as session:
        needed_data = session.query(One_game).filter(One_game.id == user_tg_id).first()
        print('needed data = ', needed_data)
        FK = session.query(General.index).filter(General.id == user_tg_id).scalar()
        print('\n\n\nFR  =  ', FK)
        if not needed_data:
            new_gamer = One_game(id=user_tg_id, us_number=0, user_id = FK)
            session.add(new_gamer)
            session.commit()
        else:
            needed_data.us_number = 0
            session.commit()

def insert_user_number_in_one_game_table(user_tg_id: int, number:int):
    with session_maker() as session:
        needed_data = session.query(One_game).filter(One_game.id == user_tg_id).first()
        needed_data.us_number = number
        session.commit()

def REFRESH_game_table(user_tg_id: int):
    print('REFRESH works')
    with session_maker() as session:
        needed_data = session.query(One_game).filter(One_game.id == user_tg_id).first()
        needed_data.us_number = 0
        session.commit()

