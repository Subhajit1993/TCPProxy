# from mongoengine import Document, StringField, SequenceField, BooleanField, DateTimeField
# import jwt
# import datetime
# from flask import current_app as app
#
#
# class Users(Document):
#     FirstName = StringField(required=True)
#     LastName = StringField()
#     UniqueName = StringField()
#     About = StringField()
#     Email = StringField(required=True)
#     EmailVerified = BooleanField()
#     Password = StringField()
#     PhoneNumber = StringField()
#     PhoneVerified = BooleanField()
#     DOB = StringField()
#     ProfilePic = StringField()
#     AuthProvider = StringField()
#     Gender = StringField()
#     PushToken = StringField()
#     PushTokenActive = BooleanField()
#     CreatedDate = DateTimeField(default=(datetime.datetime.now()))
#
#     @staticmethod
#     def encode_auth_token(user_id):
#         """
#         Generates the Auth Token
#         :return: string
#         """
#         try:
#             payload = {
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=3, seconds=30),
#                 'iat': datetime.datetime.utcnow(),
#                 'sub': user_id
#             }
#             return jwt.encode(
#                 payload,
#                 (app.config['SECRET_KEY'])[0],
#                 algorithm='HS256'
#             ).decode('utf-8')
#         except Exception as e:
#             return e
#
#     @staticmethod
#     def decode_auth_token(auth_token):
#         """
#         Decodes the auth token
#         :param auth_token:
#         :return: integer|string
#         """
#         try:
#             payload = jwt.decode(auth_token, (app.config['SECRET_KEY'])[0])
#             return payload['sub']
#         except jwt.ExpiredSignatureError:
#             return 'Token expired. Please log in again.'
#         except jwt.InvalidTokenError:
#             return 'Invalid token. Please log in again.'
