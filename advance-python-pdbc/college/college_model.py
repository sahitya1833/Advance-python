import pymysql


class CollegeModel:
    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from college"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = CollegeModel.next_pk(self)
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['phone_number']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "insert into college values( %s, %s, %s, %s, %s, %s)"
        data = (id, name, address, state, city, phone_number)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record insert successfully")

    def update(self, data):
        id = data['id']
        name = data['name']
        address = data['address']
        state = data['state']
        city = data['city']
        phone_number = data['phone_number']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "update college set name =%s, address = %s, state = %s, city = %s, phone_number = %s where id = %s"
        data = (name, address, state, city,phone_number, id)
        print("sql>", sql)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record update successfully")

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "delete from college where id= %s"
        data = (id,)
        print("sql>", sql)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record delete successfully")


    def get(self,id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where id =%s"
        data = (id,)
        cursor.execute(sql,data)
        result = cursor.fetchall()
        column_name =('id', 'name','address','state', 'city', 'phone_number')
        list = []
        for x in result:
            list.append({column_name[i]:x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where name = %s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name =('id', 'name','address','state', 'city', 'phone_number')
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        id = data.get('id', 0)
        name = data.get('name','')
        address = data.get('address','')
        state = data.get('state','')
        city = data.get('city','')
        phone_number = data.get('phone_number','')
        page_no = data.get("page_no", 0)
        page_size = data.get("page_size", 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from college where 1=1 "
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if address != '':
            sql += " and address like '" + address + "%'"
        if state!= '':
            sql += " and state like '" + state + "%'"
        if city != '':
            sql += " and city like '" + city + "%'"
        if phone_number != '':
            sql += "and phone_number like '" + phone_number + "%'"
        if page_no > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + "," + str(page_size)
        print("sql>",sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ('id', 'name', 'address', 'state', 'city', 'phone_number')
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})

        connection.close()
        return list




