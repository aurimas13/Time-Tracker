import logging
from app import db


def save_changes(data=False) -> bool:
    """
    Persists data to the database.
    Don't use `data` if you .delete()
    """
    try:
        if data is not False:
            db.session.add(data)
        db.session.commit()
        return True
    except Exception as e:
        logging.error(e)
        return False