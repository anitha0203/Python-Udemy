user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)

    return secure_func


@user_has_permission
def my_function(panel):
    return f'Password for {panel} panel is 1234.'


print(my_function('movie'))
print(my_function.__name__)
