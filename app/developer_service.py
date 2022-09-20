from app.models import Developer
from app.database_utils import save_changes


def g_developer(form):
    """
    This a method that creates a new developer and saves it to a database.

    args:
        form (str)

    return:
        resUlt (boolean) saves to the database
    """
    developer = Developer(name=form['developer_name'])
    result = save_changes(developer)
    return result
