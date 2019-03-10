import datetime
import uuid
from src.common.database import Database
from src.models.post import Post



class Post(object):

    def __init__(self, blog_id, content, author, create_date=datetime.datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.create_date = create_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())
    
    def json(self):
        return {
            '_id' : self._id,
            'blog_id':self.blog_id,
            'author': self.author,
            'content':self.content,
            'title':self.title,
            'create_date' :self.create_date
        }
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id':id})
        return cls(blog_id=post_data['blog_id'],
                    title=post_data['title'],
                    content=post_data['author'],
                   create_date=post_data['created_date'],
                    _id=post_data['_id'])

    @staticmethod
    def from_blog(id):
        return [Post for post in Database.find(collection='posts', query={'blog_id':id})]
