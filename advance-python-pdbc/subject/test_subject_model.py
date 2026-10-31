from subject_model import SubjectModel

def test_add():
    data = {}
    data['id'] = 1
    data['name'] = 'python'
    data['description'] = 'data types'
    data['course_id'] = 2
    model = SubjectModel()
    model.add(data)

# test_add()

def test_update():
    data = {}
    data['id'] = 1
    data['name'] = 'python'
    data['description'] = 'basics of pythhon|'
    data['course_id'] = 2
    model = SubjectModel()
    model.update(data)

# test_update()


def test_delete():
    model = SubjectModel()
    model.delete(1)

# test_delete()

def test_search():
    data = {}
    # data['id'] = 1
    # data['name'] = 'python'
    # data['description'] = "data types"
    data['page_no'] = 1
    data['page_size'] = 5
    model =SubjectModel()
    model.search(data)

# test_search()


def test_get():
    model = SubjectModel()
    model.get(2)

# test_get()


def test_find_by_name():
    model = SubjectModel()
    model.find_by_name('python')

test_find_by_name()
