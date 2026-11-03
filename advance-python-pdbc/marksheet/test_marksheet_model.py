from marksheet.marksheet_model import MarksheetModel
from student.student_model import StudentModel


def do_print(data):
    print(data['id'], '\t', data['roll_no'], '\t', data['name'], '\t', data['student_id'], '\t', data['physics'],
          '\t', data['chemistry'], '\t', data['maths'])


def test_add():
    data= {}
    # data['id'] = 8
    data['roll_no'] = 139
    data['student_id'] = 2
    student_list = StudentModel().get(data['student_id'])
    first_name = student_list[0].get['first_name']
    last_name = student_list[0].get['last_name']
    data['name'] = first_name + ' ' + last_name
    data['physics'] = 70
    data['chemistry'] = 67
    data['maths'] = 79

    model = MarksheetModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)

# test_add()

def test_update():
    data = {}
    data['id'] = 1
    data['roll_no'] = 108
    data['name'] = 'Arjun Singh'
    data['student_id'] = 2
    data['physics'] = 70
    data['chemistry'] = 67
    data['maths'] = 79

    model = MarksheetModel()
    model.update(data)

# test_update()

def test_delete():
    model = MarksheetModel()
    model.delete(2)

# test_delete()

def test_get():
    model = MarksheetModel()
    list =model.get(1)
    for data in list:
        do_print(data)

# test_get()

def test_find_by_roll():
    model = MarksheetModel()
    list = model.find_by_roll_no(139)
    for data in list:
        do_print(data)

# test_find_by_roll()

def test_search():
    data = {}
    # data['name'] = 'Priya'
    # data['roll_no'] = 139
    # data['student_id'] = 2
    data['pageNo'] = 5
    data['pageSize'] = 10
    model = MarksheetModel()
    model.search(data)

test_search()

