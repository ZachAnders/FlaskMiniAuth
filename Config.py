#!/usr/bin/env python

class Config():
	def __init__(self, prefix="_mini_auth_"):
		self.prefix = prefix
	def get_prefix(self, keyword=""):
		return str(self.prefix) + str(keyword)
	def username_key(self):
		return self.get_prefix("username")
	def timestamp_key(self):
		return self.get_prefix("timestamp")

DefaultConfig = Config()
