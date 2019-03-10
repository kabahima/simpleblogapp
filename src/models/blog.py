import datetime
import uuid
from src.common.database import Database
from src.models.blog import Blog


class Blog(object):
    def __init__(self, author, author_id,  title, description, _id=None):
        self.author = author
        self.author_id = author_id
        self.title = title
        self.description = description
        self._id = uuid.uuid4().hex if _id is None else _id

    def new_post(self, title, content, date=datetime.datetime.utcnow():
        # title = input("Enter post title: ")
        # content = input("Enter post content: ")
        # date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")
        # if date == "":
        #     date = datetime.datetime.utcnow()
        # else:
        #         date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author,
                    create_date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        return {
                'author' : self.author,
                'title': self.title,
                'author_id': self.author_id,
                '_id': self.id
                }
    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection= blogs,
                                    query={'_id':id})
        return cls(**blog_data)

    @classmethod
    def find_by_author_id(cls, author_id):
        blogs = Database.find(collection='blogs',
                                query={'author_id':author_id})
        return [cls(**blog) for blog in blogs]
