from fileinput import close

import pymysql
from pymysql import connect


class CourseModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from course"
        cursor.execute(sql)
        print("sql>", sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = CourseModel.next_pk(self)
        name = data['name']
        description = data['description']
        details = data['details']
        name_exist = self.find_by_name(name)
        if len(name_exist) > 0:
            raise Exception("name already exist")
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "insert into course values(%s, %s, %s, %s)"
        data = (id, name, description, details)
        print("sql>", sql)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def update(self, data):
        id = data['id']
        name = data['name']
        description = data['description']
        details = data['details']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "update course set name =%s, description =%s, details = %s where id = %s"
        data = (name, description, details, id)
        print("sql>", sql)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "delete from course where id =%s"
        data = (id,)
        print("sql>", sql)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def search(self, data):
        id = data.get('id', 0)
        name = data.get('name', '')
        description = data.get('description', '')
        details = data.get('details', '')
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from course where 1=1 "
        if id != 0:
            sql += "and id =" + str(id)
        if name != '':
            sql += "and name like'" + name + "%'"
        if description != '':
            sql += "and description like '" + description + "%'"
        if details != '':
            sql += "and details like '" + details + "%'"
        if page_no > 0:
            page_no = (page_no - 1) * page_size
            sql += "limit " + str(page_no) + "," + str(page_size)
        cursor.execute(sql)
        print("sql>", sql)
        result = cursor.fetchall()
        # print(result)
        column_name = ("id", "name", "description", "details")
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})

        connection.close()
        return list

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from course where id = %s"
        data = (id,)
        cursor.execute(sql, id)
        print("sql>", sql)
        result = cursor.fetchall()
        column_name = ('id', 'name', 'description', 'details')
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_name(self, name):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from course where name = %s"
        data = (name,)
        print("sql>", sql)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ('id', 'name', 'description', 'details')
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
