from role.role_model import RoleModel

def do_print(x):
    print(x['id'], '\t', x['name'], '\t', x['description'])


def test_add():
    data={}
    data['name'] = 'HR'
    data['description'] = 'manage recruitments'
    model = RoleModel()
    try:
        model.add(data)
    except Exception as e:
        print(e)

test_add()

def test_update():
    data={}
    data['id'] = 5
    data['name'] = 'marketing'
    data['description'] = 'manage marketing department'
    model = RoleModel()
    model.update(data)

# test_update()

def test_delete():
    model = RoleModel()
    model.delete(1)

# test_delete()

def test_get():
    model = RoleModel()
    list = model.get(2)
    for data in list:
        do_print(data)

# test_get()

def test_find_by_name():
    model = RoleModel()
    list = model.find_by_name('faculty')
    for x in list:
        do_print(x)

# test_find_by_name()


def test_search():
    data = {}
    data['id'] = 2
    # data['name'] = 'faculty'
    data['page_no'] = 1
    data['page_size'] = 5
    model = RoleModel()
    list1 = model.search(data)
    for x in list1:
        do_print(x)

# test_search()

