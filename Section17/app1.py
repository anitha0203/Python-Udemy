import functools

user = {'username': 'jose123', 'access_level': 'user'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get('access_level') == 'user':
            return func(panel)

    return secure_func


@user_has_permission('admin')
def my_function(panel):
    return f'Password for {panel} panel is 1234.'


print(my_function.__name__)
my_function = user_has_permission('admin')(my_function)
