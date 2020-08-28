 
from time import sleep
from subprocess import run
from datetime import datetime
if __name__ == "__main__":
	branch = "master"
	seconds = 5
	while True:
		run(['python3', 'update_file.py'])
		run(['git', 'fetch'])
		run(['git', 'pull', 'origin', 'master'])
		run(['git', 'add', '.'])
		run(['git', 'commit', '-m', "Update : {}".format(datetime.now().strftime("%d-%m-%y %H:%M"))])
		run(['git', 'push', 'origin', 'master'])
		sleep(seconds)

