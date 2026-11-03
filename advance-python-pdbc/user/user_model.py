import pymysql
import datetime

from pymysql import connect
from setuptools.config.pyprojecttoml import load_file


class UserModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = UserModel.next_pk(self)
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['dob']
        dob = data['dob']
        address = data['address']
        role_id = data['role_id']
        role_name = data['role_name']
        name_exist = self.find_by_login_id(login_id)
        if len(name_exist) > 0:
            raise Exception("login id already exist")
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "insert into user values( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (id, first_name, last_name, login_id, password, dob, address, role_id, role_name)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record inserted successfully")

    def update(self, data):
        id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        dob = data['dob']
        address = data['address']
        role_id = data['role_id']
        role_name = data['role_name']

        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "update user set first_name =%s, last_name =%s, login_id =%s, password =%s, dob =%s, address =%s, role_id =%s, role_name =%s where id =%s"
        data = (first_name, last_name, login_id, password, dob, address, role_id, role_name, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record update successfully")

    def delete(self, id):
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "delete from user where id =%s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record delete successfully")

    def get(self, id):
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from user where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = (
            'id', 'first_name', 'last_name', 'login_id', 'password', 'dob', 'address', "role_id", "role_name")
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_login_id(self, login_id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from user where login_id = %s"
        data = (login_id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "first_name", "last_name", "login_id", "password", "dob", "address", "role_id", "role_name")
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        id = data.get('id', 0)
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        login_id = data.get('login_id', '')
        password = data.get('password', '')
        dob = data.get('dob', 0)
        address = data.get('address', '')
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from user where 1=1 "
        if id != 0:
            sql += "and id = " + str(id)
        if first_name != '':
            sql += " and first_name like '" + first_name + "%'"
        if last_name != '':
            sql += " and last_name like '" + last_name + "%'"
        if login_id != '':
            sql += " and login_id like '" + login_id + "%'"
        if password != '':
            sql += " and password like '" + password + "%'"
        if dob != 0:
            sql += " and dob = " + str(dob)
        if address != '':
            sql += " and address like '" + address + "%'"
        if page_no > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        print('sql => ', sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "first_name", "last_name", "login_id", "password", "dob", "address", "role_id", "role_name")
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
