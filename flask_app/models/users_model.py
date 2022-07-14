from flask_app.config.mysqlconnection import connectToMySQL

class User:
    
    def __init__(self, data) -> None:
        self.id = data['id']
        self.full_name = f"{data['first_name']} {data['last_name']}"
        self.email = data['email']
        self.created_at = data['created_at']
    
    @classmethod
    def showAll(cls):
        query = 'SELECT * FROM users'
        result = connectToMySQL('users_schema').query_db(query)
        users = [cls(user).__dict__ for user in result]
        return users
    
    @classmethod
    def addNewUser(cls, data):
        query = 'INSERT INTO users( first_name, last_name, email )'
        query += 'VALUES( %(first_name)s, %(last_name)s, %(email)s)'
        result = connectToMySQL('users_schema').query_db(query, data)
        return result