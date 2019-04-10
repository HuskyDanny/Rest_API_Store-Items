from user import User
from werkzeug.security import safe_str_cmp


users = []
users.append(User(23,'Junchen','131325'))

id_mapping = { user.id : user for user in users}
name_mapping = {user.name : user for user in users}


def authenticate(name, password):
    user = name_mapping.get(name, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return id_mapping.get(user_id, None)
