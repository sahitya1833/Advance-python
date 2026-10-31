from user_model import UserModel
import datetime


def test_add():
    data = {}
    data['first_name'] = 'sahtiya'
    data['last_name'] = 'kanojiya'
    data['login_id'] = 'sk105'
    data['password'] = 'sah1234'
    data['dob'] = datetime.date(2004, 3, 18)
    data['address'] = 'indore'
    model = UserModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)


test_add()


def test_update():
    data = {}
    data['id'] = 5
    data['first_name'] = "shivam"
    data['last_name'] = "thakur"
    data['login_id'] = "shiv343"
    data['password'] = 'sah1234'
    data['dob'] = datetime.date(2004, 9, 18)
    data['address'] = 'indore'
    model = UserModel()
    model.update(data)


# test_update()

def test_delete():
    model = UserModel()
    model.delete(5)


# test_delete()

def test_get():
    model = UserModel()
    model.get(4)


# test_get()


def test_find_by_login_id():
    model = UserModel()
    model.find_by_login_id('neha104')


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
    data['page_size'] = 4
    model = UserModel()
    model.search(data)

# test_search()
