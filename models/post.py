from . import db, sa, datetime

class Post(db.Model):
  id = sa.Column(sa.BigInteger, primary_key = True)
  title = sa.Column(sa.Text, nullable = False)
  subTitle = sa.Column(sa.Text)
  content = sa.Column(sa.Text, nullable=False)
  image = sa.Column(sa.String(300), nullable = False)
  datePosted = sa.Column(sa.DateTime, default=datetime.datetime.utcnow, server_default=sa.func.now())

  def __repr__(self):
    return '<Post %r>' % self.title