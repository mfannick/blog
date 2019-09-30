from app.models import User,Comment
from app import db

def setUp(self):
        self.user_annick = User(username = 'annick',password = 'escofavi', email = 'mfannick1@gmail.com')
        self.comment= Comment(commentId=1,commentWrite='comment content',user = self.user_annick )

def tearDown(self):
        Comment.query.delete()
        User.query.delete()
def test_check_instance_variables(self):
        self.assertEquals(self.comment.id,1)
        self.assertEquals(self.comment.commentWrite,'comment content')
        self.assertEquals(self.comment.userId.user,self.user_annick)
def test_savecomment(self):
        self.Comment.saveComment()
        self.assertTrue(len(Comment.query.all())>0)
def test_getcomment_by_id(self):

        self.comment.saveComment()
        getcomment= Comment.getComment(1)
        self.assertTrue(len(Comment.getComment) == 1)