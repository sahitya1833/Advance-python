from faculty_model import FacultyModel
import datetime


def test_add():
    data = {}
    data['first_name'] = 'sahtiya'
    data['last_name'] = 'kanojiya'
    data['email'] = 'sahitya@gmail.com'
    data['password'] = 'sah1234'
    data['address'] = 'bhopal'
    data['gender'] = 'male'
    data['dob'] = datetime.date(2004, 3, 18)
    data['college_id'] = 1
    data['college_name'] = 'ips'
    data['course_id'] = 2
    data['course_name'] = 'corporate python'
    data['subject_id'] = 1
    data['subject_name'] = 'python'
    model = FacultyModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)


test_add()


def test_update():
    data = {}
    data['id'] = 1
    data['first_name'] = 'Sahitya'
    data['last_name'] = 'Kanojiya'
    data['email'] = 'sk18@gmail.com'
    data['password'] = 'sk@123'
    data['address'] = 'Rajendr nagar'
    data['gender'] = 'Male'
    data['dob'] = datetime.date(2001, 5, 15)
    data['college_id'] = 2
    data['course_id'] = 1
    data['subject_id'] = 2
    faculty = FacultyModel()
    faculty.update(data)


# test_update()

def test_delete():
    model = FacultyModel()
    model.delete(2)


# test_delete()

def test_get():
    model = FacultyModel()
    model.get(1)


# test_get()

def test_find_by_name():
    model = FacultyModel()
    model.find_by_email('sk18@gmail.com')


# test_find_by_name()

def test_search():
    data = {}
    data['id'] = 1
    data['first_name'] = 'S'
    model = FacultyModel()
    list = model.search(data)


# test_search()
