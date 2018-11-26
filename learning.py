# this is the assessment test, challenge 5 for andela

import datetimeclass user:
 def __init__(self, name):
     self.__name = name
     self.__is_logged_in = False
     self.__last_logged_in = None  @property
 def name(self):
     return self.__name  @name.setter
 def name(self, value):
     self.__name = value  def is_logged_in(self):
     return self.__is_logged_in  @property
 def last_logged_in_at(self):
     return self.__last_logged_in  def log_in(self):
     self.__is_logged_in = True
     self.__last_logged_in = datetime.datetime.now()  def log_out(self):
     self.__is_logged_in = False  def can_edit(self, comment):
     return permission.can_edit(comment, self)  def can_delete(self, comment):
     return permission.can_delete(comment, self)  def to_string(self):
     return self.__nameclass moderator(user):
 passclass admin(moderator):
 passclass comment:
 def __init__(self, author, message, replied_to=None):
     self.__author = author
     self.__message = message
     self.__replied_to = replied_to
     self.__created_at = datetime.datetime.now()  @property
 def author(self):
     return self.__author  @author.setter
 def author(self, value):
     self.__author = value  @property
 def message(self):
     return self.__message  @message.setter
 def message(self, value):
     self.__message = value  @property
 def created_at(self):
     return self.__created_at  @property
 def replied_to(self):
     return self.__replied_to  @replied_to.setter
 def replied_to(self, value):
     self.__replied_to = value  def to_string(self):
     comment_string = "{} by {}".format(
         self.__message,
         self.author.to_string()
     )
     if self.__replied_to:
         comment_string = "{} (replied to {})".format(
         comment_string,
         self.__replied_to.author.to_string()
     )
     return comment_stringclass permission:
 """Class to delegate comment permission rules to.  Using lower case class names here as mentioned.
 """
 USER, MOD, ADMIN = range(3)  def __get_permission_level(user):
     permission_map = {
         user: USER,
         moderator: MOD,
         admin: ADMIN
     }
     user_type = type(user)
     return permission.PERMISSION_MAP[user_type]  @classmethod
 def can_edit(cls, comment, user):
     permission_level = cls.__get_permission_level(user)
     if permission_level in {permission.USER, permission.MOD}:
         return comment.author == user
     elif permission_level == permission.ADMIN:
         return True
     # Could raise an error for unknown permission type.
     # Don't give them permission regardless.
     return False  @classmethod
 def can_delete(cls, comment, user):
     return cls.__get_permission_level(user) in {permission.MOD, permission.ADMIN}
