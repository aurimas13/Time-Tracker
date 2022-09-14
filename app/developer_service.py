from app.models import Developer
from app.database_utils import save_changes


def add_developer(form):
    developer = Developer(name=form['developer_name'])
    result = save_changes(developer)
    return result


