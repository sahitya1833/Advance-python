from college.college_model import CollegeModel
from student_model import StudentModel
import datetime


def do_print(data):
    print(data['id'], '\t', data['first_name'], '\t', data['last_name'], '\t', data['dob'], '\t', data['mobile_number'],
          '\t', data['email'], '\t', data['college_id'], '\t', data['college_name'])


def test_add():
    data = {}
    data['first_name'] = 'sahitya'
    data['last_name'] = 'kanojiya'
    data['dob'] = datetime.date(2004, 3, 18)
    data['mobile_number'] = '8085766291'
    data['email'] = 'shaitya@123'
    data['college_id'] = 1
    data['college_name'] = 'ips academy'
    model = StudentModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)


# test_add()

def test_update():
    data = {}
    data['id'] = 1
    data['first_name'] = 'rhul'
    data['last_name'] = 'sharma'
    data['dob'] = datetime.date(2002, 5, 28)
    data['mobile_number'] = '9565766291'
    data['email'] = 'shrama@123'
    data['college_id'] = 2
    # data['college_name'] = 'ips academy'
    college_list = CollegeModel().get(data['college_id'])
    college_name = college_list[0].get('name')
    data['college_name'] = college_name
    model = StudentModel()
    model.update(data)


test_update()


def test_delete():
    model = StudentModel()
    model.delete(5)


# test_delete()

def test_get():
    model = StudentModel()
    list = model.get(2)
    for data in list:
        do_print(data)


# test_get()

def test_find_by_email():
    model = StudentModel()
    list = model.find_by_email('rahul@gmail.com')
    for data in list:
        do_print(data)


# test_find_by_email()

def test_search():
    data = {}
    # data['id'] = 4
    # data['first_name'] = 'rhul'
    # data['last_name'] = 'sharma'
    # data['dob'] = datetime.date(2002, 5, 28)
    # data['mobile_number'] = '9565766291'
    # data['email'] = 'shrama@123'
    # data['college_id'] = 2
    # data['college_name'] = 'ips academy'
    data['page_no'] = 1
    data['page_size'] = 5
    model = StudentModel()
    list = model.search(data)
    for data in list:
        do_print(data)


# test_search()
