from database import Database
from admin import Admin

a = Admin('Anitha', '1234', 2)
b = Admin('Ani', '1234', 1)

a.save()
b.save()

user = Database.find(lambda x: x['username'] == 'Anitha')[0]
user_obj = Admin(**user)
print(user_obj.username)
