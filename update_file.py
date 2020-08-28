from datetime import datetime

with open('timestamp.txt', 'w') as FPtr:
	content = "Update : {}".format(datetime.now().strftime("%d-%m-%y %H:%M:%S"))
	FPtr.write(content)
