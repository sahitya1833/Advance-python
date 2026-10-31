import pymysql
from pymysql import connect


class FacultyModel:

    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from faculty"
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
        id = FacultyModel.next_pk(self)
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        address = data['address']
        gender = data['gender']
        dob = data['dob']
        college_id = data['college_id']
        college_name = data['college_name']
        course_id = data['course_id']
        course_name = data['course_name']
        subject_id = data['subject_id']
        subject_name = data['subject_name']
        email_exist = self.find_by_email(email)
        if len(email_exist) > 0:
            raise Exception("email already exist")
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "insert into faculty values( %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s, %s, %s, %s)"
        data = (id, first_name, last_name, email, password, address, gender, dob, college_id, college_name, course_id,
                course_name, subject_id, subject_name)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record inserted successfully")

    def update(self, data):
        id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        password = data['password']
        address = data['address']
        gender = data['gender']
        dob = data['dob']
        college_id = data['college_id']
        course_id = data['course_id']
        subject_id = data['subject_id']
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "update faculty set first_name =%s, last_name =%s, email =%s, password =%s, address =%s, gender = %s, dob =%s, college_id =%s, course_id =%s, subject_id = %s where id =%s"
        data = (first_name, last_name, email, password, address, gender, dob, college_id, course_id, subject_id, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record update successfully")

    def delete(self, id):
        connection = pymysql.connect(host="localhost", port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "delete from faculty where id =%s"
        data = (id,)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record delete successfully")

    def get(self, id):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "select * from faculty where id = %s"
        data = (id)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = (
            'id', 'first_name', 'last_name', 'email', 'password', 'address', 'gender', 'dob', 'college_id', 'course_id',
            'subject_id')
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_email(self, name):
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "select * from faculty where email =%s"
        data = (name,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = (
            'id', 'first_name', 'last_name', 'email', 'password', 'address', 'gender', 'dob', 'college_id', 'course_id',
            'subject_id')
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
        email = data.get('email', '')
        password = data.get('password', '')
        address = data.get('address', '')
        gender = data.get('gender', '')
        dob = data.get('dob', 0)
        college_id = data.get('college_id', 0)
        course_id = data.get('course_id', 0)
        subject_id = data.get('subject_id', 0)
        page_no = data.get('page_no', 0)
        page_size = data.get('page_size', 0)
        connection = pymysql.Connection(host="localhost", port=3306, user="root", password="root",
                                        database="advance_python")
        cursor = connection.cursor()
        sql = "select * from faculty where 1=1 "
        if id != 0:
            sql += " and id = " + str(id)
        if first_name != '':
            sql += " and first_name like '" + first_name + "%'"
        if last_name != '':
            sql += " and last_name like '" + last_name + "%'"
        if email != '':
            sql += " and email like '" + email + "%'"
        if password != '':
            sql += " and password like '" + password + "%'"
        if address != '':
            sql += " and address like '" + address + "%'"
        if gender != '':
            sql += " and gender like '" + gender + "%'"
        if dob != 0:
            sql += " and dob =%s " + str(dob)
        if college_id != 0:
            sql += " and college_id = " + str(college_id)
        if course_id != 0:
            sql += " and course_id = " + str(course_id)
        if subject_id != 0:
            sql += " and subject_id = " + str(subject_id)
        if page_no > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + ", " + str(page_size)
        cursor.execute(sql)
        print("sql>", sql)
        result = cursor.fetchall()
        column_name = (
            'id', 'first_name', 'last_name', 'email', 'password', 'address', 'gender', 'dob', 'college_id', 'course_id',
            'subject_id')
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
