from flask_app.config.mysqlconnection import connectToMySQL

class User:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.full_name = f'{self.first_name} {self.last_name}'
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def showAll(cls):
        query = 'SELECT * FROM users;'
        result = connectToMySQL('users_schema').query_db(query)
        users = [cls(user).__dict__ for user in result]
        exclusions = ['first_name','last_name','updated_at']
        for user in users:
            for excl in exclusions:
                del user[excl]
        return users

    @classmethod
    def showUser(cls, id):
        query = 'SELECT * FROM users '
        query += f'WHERE users.id = {id};'
        result = connectToMySQL('users_schema').query_db(query)
        result = cls(result.pop())
        return result

    @classmethod
    def addNewUser(cls, data):
        query = 'INSERT INTO users( first_name, last_name, email ) '
        query += 'VALUES( %(first_name)s, %(last_name)s, %(email)s);'
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    @classmethod
    def editExistingUser(cls, id, data):
        query = 'UPDATE users '
        query += 'SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s '
        query += f'WHERE id = {id};'
        result = connectToMySQL('users_schema').query_db(query, data)
        return result

    @classmethod
    def deleteExistingUser(cls, id):
        query = 'DELETE FROM users '
        query += f'WHERE id = {id};'
        result = connectToMySQL('users_schema').query_db(query)
        return result