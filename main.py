# Isabella Tarsitano
# Lab 6 creation

def encode(paswrd):
	# Create a new string for the result
	newPas = ''

	# iterate through each element in the string
	for number in paswrd:
		# convert each string element into a number,
		# preform the calculation,
		# convert back to a string,
		# then concatenate with the new password string.
		newPas += str(int(number) + 3)
	return newPas


def decode(pas):
	pass


def menu():
	# Create the menu selection. I just like it this way.
	print('Menu')
	print('-------------')
	print('1. Encode')
	print('2. Decode')
	print('3. Quit')


if __name__ == "__main__":
	# The main logic:

	# get everything set up :)
	menu()
	print()
	user_choice = int(input('Please enter an option:'))

	# while the user wants to continue
	while user_choice == 1 or user_choice == 2:
		if user_choice == 1:
			# if it one then they want the password to be encoded
			password = input('Please enter your password to encode: ')
			encoded = encode(password)
			print('Your password has been encoded and stored!')
		if user_choice == 2:
			# if it is 2, they want the password to be decoded. Get the password from option 1 :)
			# I don't know what is supposed to happen if they haven't already given their password
			decoded = decode(encoded)
			print(f'The encoded password is {encoded}, and the original password is {decoded}')

		# start the option selection all over again :)))
		print()
		menu()
		print()
		user_choice = int(input('Please enter an option:'))
