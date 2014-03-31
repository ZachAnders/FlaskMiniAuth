#!/usr/bin/pythonCoreAuthenticator
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from CoreAuth import AbstractUser
from DbSession import DbSession
#import math
#from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base, AbstractUser):
	__tablename__ = "User"
	Id = Column(Integer, primary_key=True)
	Username = Column(String(32), index=True)
	Password = Column(Text)
	Timestamp = Column(Integer)

	def get_username(self):
		return self.Username

	def get_password(self):
		return self.Password

	def get_timestamp(self):
		return self.Timestamp

if __name__ == "__main__":
	sess = DbSession()
	sess.build_tables(Base)
