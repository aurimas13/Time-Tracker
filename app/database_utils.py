import logging
from app import db


def save_changes(data=False) -> bool:
    """
    This is the method that persists data to the database.

    args:
        data (boolean)
    return:
        boolean
    """
    try:
        if data is not False:
            db.session.add(data)
        db.session.commit()
        return True
    except Exception as e:
        logging.error(e)
        return False
