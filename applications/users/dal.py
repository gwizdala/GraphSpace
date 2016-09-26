from models import *
from django.utils.datetime_safe import datetime
from graphspace.utils import generate_uid
from sqlalchemy.orm.exc import NoResultFound
from graphspace.wrappers import sqlalchemy_operation

# TODO: Add documentation about exception raised.


@sqlalchemy_operation
def add_user(db_session, email="public_user_%s@graphspace.com" % generate_uid(size=10), password="public", is_admin=0):
	"""
	Add a new user. If email and password is not passed, it will create a user with default values.
	By default a user has no admin access.

	:param db_session: Database session.
	:param email: User ID of the user. Default value is dynamically generated user id.
	:param password: Password of the user. Default value is "public".
	:param admin: 1 if user has admin access else 0. Default value is 0.
	:return: User
	"""

	user = User(email=email, password=password, is_admin = is_admin)
	db_session.add(user)
	return user


@sqlalchemy_operation
def get_user(db_session, email):
	"""
	Get a user with given email.

	:param db_session: Database session.
	:param email: email of the user.
	:return: User if email exists else None.
	"""
	return db_session.query(User).filter(User.email == email).one_or_none()


@sqlalchemy_operation
def update_user(db_session, email, updated_user):
	"""
	Update the user data with given email with the given updated user data.

	:param db_session: Database session.
	:param email: User ID of the user.
	:param updated_user: Updated user data. Data is stored in dictionary format where keys store the column names and values store the updated value.
	:return: User
	"""
	user = db_session.query(User).filter(User.email == email)
	for (key, value) in updated_user.items():
		setattr(user, key, value)
	return user


@sqlalchemy_operation
def delete_user(db_session, email):
	"""
	:param db_session: Database session.
	:param email: User ID of the user.
	:return: None
	"""
	user = db_session.query(User).filter(User.email == email)
	db_session.delete(user)



@sqlalchemy_operation
def add_password_reset(db_session, email):
	"""
	Add a password reset entry for given user id.
	'code' and 'created' column values are generated programmatically. Their values cannot be set by a user.
	:param db_session: Database session.
	:param email: User ID for which password reset row will be generated.
	:return: None
	"""
	password_reset = PasswordResetCode(email=email, code=generate_uid(), created=datetime.now())
	db_session.add(password_reset)
	return password_reset



@sqlalchemy_operation
def get_password_reset_by_code(db_session, code):
	"""
	:param db_session: Database session.
	:param code: Password reset code
	:return: PasswordReset if code exists else None
	"""


@sqlalchemy_operation
def update_password_reset(db_session, id, updated_user):
	"""
	:param db_session: Database session.
	:param id: primary key in password_reset table.
	:param updated_user: updated password_reset row.
	:return: None
	"""


@sqlalchemy_operation
def add_group(db_session, group_id, name, owner_id, description):
	"""
	:param db_session: Database session.
	:param group_id: Unique ID of the group
	:param name: Name of the group
	:param owner_id: ID of user who owns the group
	:param description: Description of the group
	:return: None
	"""


@sqlalchemy_operation
def get_group(db_session, group_id):
	"""
	Get group by group id.
	:param db_session: Database session.
	:param group_id: Unique ID of the group
	:return: Group if group_id exists else None
	"""


@sqlalchemy_operation
def update_group(db_session, group_id, updated_group):
	"""
	Update group row entry.
	:param db_session: Database session.
	:param group_id: Unique ID of the group
	:param updated_group: Updated group row entry
	:return: None
	"""


@sqlalchemy_operation
def delete_group(db_session, group_id):
	"""
	Delete group from Group table.
	:param db_session: Database session.
	:param group_id: Unique ID of the group
	:return: None
	"""


@sqlalchemy_operation
def add_group_to_user(db_session, group_id, email):
	"""
	:param db_session: Database session.
	:param group_owner: Unique ID of the user who owns the group.
	:param group_id: Unique ID of the group
	:param email: Unique ID of a member of the group
	:return: None
	"""


@sqlalchemy_operation
def delete_group_to_user(db_session, group_id, email):
	"""
	:param db_session: Database session.
	:param group_owner: Unique ID of the user who owns the group.
	:param group_id: Unique ID of the group
	:param email: Unique ID of a member of the group
	:return: None
	"""


@sqlalchemy_operation
def get_groups_by_email(db_session, email):
	"""
	Returns all groups where user with give email is a member.
	:param db_session: Database session.
	:param email: email of a user who is a member of one or many groups.
	:return: list of Groups
	"""

@sqlalchemy_operation
def get_groups_by_owner_id(db_session, owner_id):
	"""
	Returns all groups where user with give email is a owner.

	:param owner_id: email of a user who owns one or many groups.
	:return: list of Groups
	"""


@sqlalchemy_operation
def get_users_by_group(db_session, group_id):
	"""
	Returns all users who are member of a group with given group_id.
	:param db_session: Database session.
	:param group_owner: Unique ID of the user who owns the group.
	:param group_id: Unique ID of the group.
	:return: list of Users
	"""


