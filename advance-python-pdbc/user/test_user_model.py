from role.role_model import RoleModel
from user_model import UserModel
import datetime
import datetime


def do_print(data):
    print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['login_id'], '\t',
                data['password'], '\t', data['dob'], '\t', data['address'], '\t', data['role_id'], '\t',
                data['role_name'])


def test_add():
    data = {}
    data['first_name'] = 'deepak'
    data['last_name'] = 'yadav'
    data['login_id'] = 'dy999'
    data['password'] = 'sah1234'
    data['dob'] = datetime.date(2004, 3, 18)
    data['address'] = 'indore'
    data['role_id'] = 4
    role_list = RoleModel().get(data["role_id"])
    role_name = role_list[0].get('name')
    data['role_name'] = role_name
    model = UserModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)


# test_add()


def test_update():
    data = {}
    data['id'] = 5
    data['first_name'] = "shivam"
    data['last_name'] = "thakur"
    data['login_id'] = "shiv343"
    data['password'] = 'sah1234'
    data['dob'] = datetime.date(2004, 9, 18)
    data['address'] = 'indore'
    data['role_id'] = 4
    role_list = RoleModel().get(data['role_id'])
    role_name = role_list[0].get('name')
    data['role_name'] = role_name

    model = UserModel()
    model.update(data)


# test_update()

def test_delete():
    model = UserModel()
    model.delete(5)


# test_delete()

def test_get():
    model = UserModel()
    list = model.get(4)
    for x in list:
        do_print(x)


# test_get()


def test_find_by_login_id():
    model = UserModel()
    list = model.find_by_login_id('neha104')
    for x in list:
        do_print(x)


# test_find_by_login_id()


def test_search():
    data = {}
    # data['id'] = 1
    # data['first_name'] = 'r'
    # data['last_name'] = 'sharma'
    # data['login_id'] = 'rahul101 '
    # data['password'] ='Rahul@123'
    # data['address'] ='indore'
    # data['dob'] = 2002 - 5 - 15
    data['page_no'] = 1
    data['page_size'] = 10
    model = UserModel()
    list = model.search(data)
    for x in list:
        do_print(x)
# test_search()
