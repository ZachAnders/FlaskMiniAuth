from AlchemySchema import User
from CoreAuth import AbstractAuthenticator 
from Config import DefaultConfig
#from DbSession import DbSession
#from flask import session
#from functools import wraps

class AlchemyAuthenticator(AbstractAuthenticator):
	def __init__(self, config=DefaultConfig):
		AbstractAuthenticator.__init__(self, config)
		self.session = None
	
	def lookup_user(self, some_user):
		#sess = DbSession().get_session()
		res = self.session.query(User).filter(User.Username == some_user).all()
		if len(res) != 1:
			return None
		return res[0]

	def create_user(self, username, passw):
		new_user = User()
		new_user.Username = username
		#new_user.Password = passlib_ctx.encrypt(passw)
		new_user.Password = self.secure_password(passw)
		return new_user


#	def has_valid_credentials(self, username, passw):
#		db_sess = DbSession().get_session()
#
#		user = get_user(db_sess, username)
#		if user and passlib_ctx.verify(passw, user.Password):
#			user.Timestamp = time.time()
#			db_sess.commit()
#			return True
#		return False


