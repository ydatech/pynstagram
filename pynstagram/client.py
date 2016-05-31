from pynstagram.session import PynstagramSession
import json
	
class PynstagramClient(object):
	def __init__(self, username, password ,proxies):
		self._session = PynstagramSession()
		self._userlogin = self._session.login(username, password, proxies)
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass
	
	def upload(self, path, caption = ''):
		media_id = self._session.upload_photo(path)
		configure_photo = self._session.configure_photo(media_id, caption)
		
		return configure_photo
	
	def userInfo(self):
		return self._userlogin