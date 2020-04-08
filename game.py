print('escape from cave terror')

action_input = input('action: ')
print(action_input)

if action_input == 'n' or action_input == 'N':
	print('go north? ok!')
elif action_input == 's' or action_input == 'S':
	print('go south, pardner!')
elif action_input == 'e' or action_input == 'E':
	print('hey! go east!')
elif action_input == 'w' or action_input == 'W':
	print('go west! u can rest l8r')
else:
	print('invalid action')