from college_model import CollegeModel


def do_print(data):
    print(data['id'], '\t', data['name'], '\t', data['address'], '\t', data['state'], '\t',
          data['city'], '\t', data['phone_number'])


def test_add():
    data = {}
    data['name'] = 'medicaps'
    data['address'] = 'rau bypass'
    data['state'] = 'MP'
    data['city'] = 'indore'
    data['phone_number'] = '9343565898'
    model = CollegeModel()
    model.add(data)

# test_add()

def test_update():
    data = {}
    data['id'] = '5'
    data['name'] = 'RPL'
    data['address'] = 'collectorate'
    data['state'] = 'Madhaya pradesh'
    data['city'] = 'indore'
    data['phone_number'] = '9343567889'
    model = CollegeModel()
    model.update(data)

# test_update()

def test_delete():
    model = CollegeModel()
    model.delete(5)

# test_delete()

def test_get():
    model = CollegeModel()
    list = model.get(1)
    for data in list:
        do_print(data)

# test_get
def test_find_by_name():
    model = CollegeModel()
    list = model.find_by_name('ips academy')
    for data in list:
        do_print(data)

# test_find_by_name()


def test_search():
    data = {}
    # data['id'] = 1
    # data['name'] = 'ips academy'
    # data['address'] = 'rau bypass'
    # data['state'] = 'madhya pradesh'
    # data['city'] = 'indore'
    # data['phone_number'] = '9876500002'
    data['page_no'] = 1
    data['page_size'] = 5
    model = CollegeModel()
    list = model.search(data)
    for data in list:
        do_print(data)

# test_search()

