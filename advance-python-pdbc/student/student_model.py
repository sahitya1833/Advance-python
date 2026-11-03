import pymysql
import datetime


class StudentModel:
    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select max(id) from student"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = StudentModel.next_pk(self)
        first_name = data['first_name']
        last_name = data['last_name']
        dob = data['dob']
        mobile_number = data['mobile_number']
        email = data['email']
        college_id = data['college_id']
        college_name = data['college_name']
        student_exist = self.find_by_email(email)
        if len(student_exist)>0:
            raise Exception("student details alread exist")
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "insert into student values( %s, %s, %s, %s, %s, %s, %s, %s)"
        data = (id, first_name, last_name, dob, mobile_number, email, college_id, college_name)
        cursor.execute(sql, data)
        print("sql>", sql)
        connection.commit()
        connection.close()
        print("record update succesfully")

    def update(self, data):
        id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        dob = data['dob']
        mobile_number = data['mobile_number']
        email = data['email']
        college_id = data['college_id']
        college_name = data['college_name']

        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "update student set first_name = %s, last_name =%s, dob =%s, mobile_number =%s, email = %s, college_id = %s, college_name = %s where id =%s "
        data = (first_name, last_name, dob, mobile_number, email, college_id, college_name, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("record update successfully")

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "delete from student where id =%s"
        data = (id,)
        cursor.execute(sql, data)
        print("sql>", sql)
        connection.commit()
        connection.close()
        print("record delete successfully")

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from student where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ('id', 'first_name', 'last_name', 'dob', 'mobile_number', 'email', 'college_id', 'college_name')
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_email(self, email):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from student where email= %s"
        data = (email,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ('id', 'first_name', 'last_name', 'dob', 'mobile_number', 'email', 'college_id', 'college_name')
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def search(self, data):
        id = data.get('id', 0)
        first_name = data.get('first_name','')
        last_name = data.get('last_name','')
        dob = data.get('dob',0)
        mobile_number = data.get('mobile_number','')
        email = data.get('email','')
        college_id = data.get('college_id',0)
        college_name = data.get('college_name','')
        page_no = data.get("page_no", 0)
        page_size = data.get("page_size", 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root',
                                     database='advance_python')
        cursor = connection.cursor()
        sql = "select * from student where 1=1 "
        if id != 0:
            sql += " and id = " + str(id)
        if first_name != '':
            sql += " and first_name like '" + first_name + "%'"
        if last_name != '':
            sql += " and last_name like '" + last_name + "%'"
        if dob!= 0:
            sql += " and dob =" + str(dob)
        if mobile_number != '':
            sql += " and mobile_number like '" + mobile_number + "%'"
        if email != '':
            sql += " and email like '" + email + "%'"
        if college_id != 0:
            sql += " and college_id = " + str(college_id)
        if college_name != '':
            sql += " and college_name like '" + college_name + "%'"
        if page_no > 0:
            page_no = (page_no - 1) * page_size
            sql += " limit " + str(page_no) + "," + str(page_size)
        print("sql>",sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ('id', 'first_name', 'last_name', 'dob', 'mobile_number', 'email', 'college_id', 'college_name')
        list = []
        for x in result:
            #print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})

        connection.close()
        return list
