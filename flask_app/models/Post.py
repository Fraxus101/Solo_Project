from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models.User import User

class Post:

    def __init__(self , data):
        self.id = data['id']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None
        self.user_like_post = []
        self.user_id_who_like = []

    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id WHERE posts.id = %(id)s;" 
        results = connectToMySQL(DB).query_db(query , data)

        review = None
        if results:
            review = cls(results[0])
            user_data = {
                'id': results[0]['users.id'],
                'email': results[0]['email'],
                'name': results[0]['name'],
                'alias': results[0]['alias'],
                'password': results[0]['password'],
                'created_at': results[0]['users.created_at'],
                'updated_at': results[0]['users.updated_at'],
            }
            review.user = User(user_data)
        return review
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        reviews = []

        if results:
            for row in results:
                review = cls(row)
                user_data = {
                    'id': row['users.id'],
                    'email': row['email'],
                    'name': row['name'],
                    'alias': row['alias'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                }
                review.user = User(user_data)
                reviews.append(review)

        return reviews
    
    @classmethod
    def get_by_user_id(cls, data):
        query = "SELECT * FROM posts JOIN users ON posts.user_id = users.id where users.id=%(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        reviews = []

        if results:
            for row in results:
                review = cls(row)
                user_data = {
                    'id': row['users.id'],
                    'email': row['email'],
                    'name': row['name'],
                    'alias': row['alias'],
                    'password': row['password'],
                    'created_at': row['users.created_at'],
                    'updated_at': row['users.updated_at'],
                }
                review.user = User(user_data)
                reviews.append(review)
        return reviews

    @classmethod 
    def create(cls , data):
        query = "INSERT INTO posts (description, user_id) VALUES(%(description)s,%(user_id)s);"
        print(query)
        result = connectToMySQL(DB).query_db(query , data)
        return result 

    
    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET description= %(description)s WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        return result
    
    @classmethod 
    def delete(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    
    #---------------------------------------#

    @classmethod 
    def add_user_like(cls, data):
        query = "INSERT INTO user_like_post (user_id, post_id) VALUES (%(user_id)s, %(post_id)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result
    @classmethod
    def remove_user_like(cls , data):
        query = "DELETE FROM user_like_post WHERE user_id = %(user_id)s AND post_id = %(post_id)s;"
        result = connectToMySQL(DB).query_db(query , data)
        return result