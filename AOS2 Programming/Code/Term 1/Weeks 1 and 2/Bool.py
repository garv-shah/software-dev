sample_users = {
    'admin': {
        'first_name': 'admin',
        'last_name': 'admin',
        'email': '',
        'password': 'admin',
        'is_admin': True,
    },
    'user': {
        'first_name': 'user',
        'last_name': 'user',
        'email': '',
        'password': 'user',
        'is_admin': False,
    },
}

current_role = 'user'

if sample_users[current_role]['is_admin']:
    print('You are an admin')
else:
    print('You are not an admin')
