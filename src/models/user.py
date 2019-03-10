# this lets our users to login and signup to be able to write to the blog
from src.common.database import Database
import uuid
from src.models.blog import Blog

class User(object):
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id
    @classmethod
    def get_by_email(cls, email):
        data =Database.find_one("users", {"email": email})
        if data is not None:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data =Database.find_one("users", {"_id": _id})
        if data is not None:
            return cls(**data)

    
    def login_vaild(self, email, password):
        # check whether a user's email matches the password
        user = User.get_by_email(email) # this creates the user object
        if user is not None: # and if the user is not None
            # check the password
            return user.password == password
        return False
    @classmethod
    def register(cls, email, password):
        # if the user alreadly exits, it should fail but if he doesnot exit the it should pass
        user = cls.get_by_email(email)
        if user is None:
            new_user = cls(email, password)
            new_user.save_to_mongo()
            session['email'] = user_email
            return True
        else:
            # user exits
            return False
    
    @staticmethod
    def login(user_email):
        # login_vaild has 
        session['email'] = user_email
        
    @staticmethod
    def logout():
        # login_vaild has 
        session['email'] = none
       =

    def get_blogs(self):
       return Blog.find_by_author_id(self._id)
    # new blog
    def new_blog(self, title, description):
        # author, title, description, author_id
        # instancsing a new blog object 
        blog = Blog(author=self.email,
                    title=title,
                    description = description,
                    author_id=self._id)
        
        blog.save_to_mongo()
    
    @staticmethod
    def new_post(blog_id, title, content, datetime.datetime.utcnow()):
        # title, content, datetime.datetime.utcnow()):
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title=title,
                        content=content,
                        date=date)
    

    def json(self):
        return
                {
                "email": self.email,
                "_id": self._id,
                "password": self.password
                }

    def save_to_mongo(self):
        Database.insert("user", self.json())
            



