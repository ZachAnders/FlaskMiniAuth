#from flask import session, render_template
#from functools import wraps
from passlib.apps import custom_app_context as passlib_ctx
from abc import ABCMeta, abstractmethod
from flask import session
from functools import wraps
import time

#def is_valid_user(some_user, timestamp):
#	"""Given a user, is this a valid user?"""
#	if some_user == "admin":
#		return True
class AbstractAuthenticator():
	__metaclass__ = ABCMeta

	def __init__(self, configuration):
		self.config = configuration

	@abstractmethod
	def lookup_user(self, username):
		pass

	@abstractmethod
	def create_user(self, username, passw):
		pass

	def valid_session(self):
		"""Returns True only if there is currently a valid username in the session"""
		user_session = self.get_session()
		if user_session:
			user = self.lookup_user(user_session[0])
			# TODO: Make this not hardcoded
			if user and user.get_timestamp() + (60*60*24*7) > time.time():
				return True
		else:
			return False
	
	def login(self, username, password):
		user = self.lookup_user(username)
		if user and self.verify_password(user.get_password(), password):
			self.set_session(username)

		return 

	def valid_session_for_user(self, username, timestamp, duration, now=time.time()):
		# Make sure username exists in session
		if 'username' in session:
			# The username should be in the session
			if username == session['username']:
				if timestamp+duration > now:
					return True
		return False
			
	def set_session(self, username, now=time.time()):
		session[self.config.username_key()] = username
		session[self.config.timestamp_key()] = now

	def get_session(self):
		user_key = self.config.username_key()
		t_stamp_key = self.config.timestamp_key()
		if user_key in session and t_stamp_key in session:
			user = session[self.config.username_key()]
			t_stamp = session[self.config.timestamp_key()]
			return (user, t_stamp)
		return None

	def verify_password(self, submitted_passw, known_passw):
		if passlib_ctx.verify(submitted_passw, known_passw):
			return True
		return False

	def secure_password(self, submitted_passw):
		return passlib_ctx.encrypt(submitted_passw)

	def requires_session(self, some_route):
		# Flask requires that decorators are implemented utilizing functools
		@wraps(some_route)
		def protected(*args, **kwargs):
			if valid_session():
				return some_route(*args, **kwargs)
			else:
				return render_template("login.html", error="Please login before continuing.")
		return protected

class AbstractUser():
	__metaclass__ = ABCMeta

	@abstractmethod
	def get_username(self):
		pass

	@abstractmethod
	def get_password(self):
		pass

	@abstractmethod
	def get_timestamp(self):
		pass

