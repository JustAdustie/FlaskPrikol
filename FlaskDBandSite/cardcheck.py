from time import sleep
def check():
	import paramiko
	import sqlite3

	temp = []

	host = "192.168.1.133"
	port = 22
	user = "pi"
	secret = "raspberry"

	try:
		client = paramiko.SSHClient()
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		client.connect(hostname=host, username=user, password=secret, port=port)
		sftp = client.open_sftp()
		sftp.get("./Desktop/tgs.txt","F:/Утилиты/Project/FlaskPrikol/FlaskDBandSite/logs/tgs.txt")
		
		sftp.close()

		connection = sqlite3.connect('db.sqlite')
		cursor = connection.cursor()

		with open("F:/Утилиты/Project/FlaskPrikol/FlaskDBandSite/logs/tgs.txt") as f:
			for i in f:
				temp.append(i[:-1])
			temp = temp[len(temp)-1]

		checking = cursor.execute("SELECT * FROM card WHERE card=?",(temp,))
		if checking.fetchone() is None:
			#return 0
			print("Карта не найдена!!")
		else:
			print("Карта найдена!!")

		connection.close()
	except Exception as e:
		print(e)

def main_check():
	while True:
		sleep(2)
		check()

if __name__ == '__main__':
	main_check()