from app.models import User,Blog
from app import db

def setUp(self):
        self.user_annick = User(username = 'annick',password = 'escofavi', email = 'mfannick1@gmail.com')
        self.blog= Blog(blogId=1,blogWrite='blog content',blogTitle="blog",user = self.user_annick )

def tearDown(self):
        Blog.query.delete()
        User.query.delete()
def test_check_instance_variables(self):
        self.assertEquals(self.blog.id,1)
        self.assertEquals(self.blog.BlogWrite,'blog content')
        self.assertEquals(self.blog.BlogTitle,'blog')
        self.assertEquals(self.blog.userId.user,self.user_annick)
def test_saveBlog(self):
        self.Blog.saveBlog()
        self.assertTrue(len(Blog.query.all())>0)
def test_getBlog_by_id(self):

        self.Blog.saveBlog()
        gotBlog= Blog.getBlog(1)
        self.assertTrue(len(Blog.getBlogs) == 1)


    