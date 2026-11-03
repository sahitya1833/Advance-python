import pymysql
from pymysql import connect


class MarksheetModel:
    def next_pk(self):
        pk = 0
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = 'select max(id) from marksheet'
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.close()
        return pk + 1

    def add(self, data):
        id = MarksheetModel.next_pk(self)
        roll_no = data['roll_no']
        name = data['name']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        student_id = data['student_id']
        # roll_exist = self.find_by_roll_no(roll_no)
        # if len(roll_exist) > 0:
        #     raise Exception("roll_no already exist")
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "insert into marksheet values(%s, %s, %s, %s, %s, %s, %s)"
        data = (id, roll_no, name,student_id, physics, chemistry, maths)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print('data inserted successfully')

    def update(self,data):
        id = data['id']
        roll_no = data['roll_no']
        name = data['name']
        student_id = data['student_id']
        physics = data['physics']
        chemistry = data['chemistry']
        maths = data['maths']
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "update marksheet set roll_no = %s, name = %s, student_id =%s, physics = %s, chemistry = %s, maths = %s where id = %s"
        data = (roll_no, name,student_id, physics, chemistry, maths, id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("data update successfully")

    def delete(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "delete from marksheet where id = %s"
        data = (id)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()

    def get(self, id):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from marksheet where id = %s"
        data = (id,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "roll_no", "student_id", "name", "physics", "chemistry", "maths")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list

    def find_by_roll_no(self, roll_no):
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from marksheet where roll_no = %s"
        data = (roll_no,)
        cursor.execute(sql, data)
        result = cursor.fetchall()
        column_name = ("id", "roll_no", "student_id", "name", "physics", "chemistry", "maths")
        list = []
        for x in result:
            # print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
    

    def search(self, data):
        id = data.get('id', 0)
        name = data.get('name', '')
        roll_no = data.get('roll_no', 0)
        physics = data.get('physics', 0)
        chemistry = data.get('chemistry', 0)
        maths = data.get('maths', 0)
        student_id = data.get('student_id', 0)
        page_size = data.get('page_size', 0)
        page_number = data.get('page_number', 0)
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='advance_python')
        cursor = connection.cursor()
        sql = "select * from marksheet where 1=1"
        if id != 0:
            sql += " and id = " + str(id)
        if name != '':
            sql += " and name like '" + name + "%'"
        if roll_no != 0:
            sql += " and roll_no = " + str(roll_no)
        if physics != 0:
            sql += " and physics = " + str(physics)
        if chemistry != 0:
            sql += " and chemistry = " + str(chemistry)
        if maths != 0:
            sql += " and maths = " + str(maths)
        if student_id != 0:
            sql += " and student_id = " + str(student_id)
        if page_number > 0:
            page_number = (page_number - 1) * page_size
            sql += ' limit ' + str(page_number) + ',' + str(page_size)
        print("sql>", sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        column_name = ("id", "rollNo", "name", "physics", "chemistry", "maths", "student_id")
        list = []
        for x in result:
            print({column_name[i]: x[i] for i, _ in enumerate(x)})
            list.append({column_name[i]: x[i] for i, _ in enumerate(x)})
        connection.close()
        return list
