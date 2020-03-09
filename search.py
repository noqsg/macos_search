import pyautogui, click

@click.command()
@click.option(
	'--search',
	'-s',
	prompt='Search Parameter',
	help='Enter Search paramter which is then used to search MacOS.',
)
@click.option(
	'--enter',
	'-e',
	help='Set to automatically press enter after search param.',
	is_flag=True,
)

def main(search, enter):
	parameter = search
	pyautogui.hotkey('command', 'space')
	if enter:
		pyautogui.typewrite(parameter + '\n')
	else:
		pyautogui.typewrite(parameter)

if __name__ == '__main__':
	main()
