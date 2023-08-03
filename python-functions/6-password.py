def validate_password(password):
	if ((len(password) >= 8) &  (any(char.islower() for char in password)) & (any(char.isupper() for char in password))):
		return True
	else:
		return False