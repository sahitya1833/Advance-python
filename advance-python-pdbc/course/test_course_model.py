from course_model import CourseModel


def test_add():
    data = {}
    data['name'] = 'AI'
    data['description'] = "AI technology"
    data['details'] = "learn AI algorithms"
    model = CourseModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)



test_add()

def test_update():
    data = {}
    data['id'] = '7'
    data['name'] = 'deep learning'
    data['description'] = "deep learning technology"
    data['details'] = "learn deep learnings algorithms"
    model = CourseModel()
    model.update(data)


# test_update()

def test_delete():
    model = CourseModel()
    model.delete(6)


# test_delete()

def test_search():
    data = {}
    # data['id'] = 4
    # data['name'] = "p"
    # data['description'] = 'd'
    # data['detail'] = 'learn'
    data['page_no'] = 1
    data['page_size'] = 5
    model = CourseModel()
    list = model.search(data)
    for data in list:
        print(data['id'], '\t', data['name'], '\t', data['description'], '\t', data['details'])


# test_search()

def test_get():
    model= CourseModel()
    model.get(3)

# test_get()


def test_find_by_name():
    model =CourseModel()
    model.find_by_name("python")

# test_find_by_name()



