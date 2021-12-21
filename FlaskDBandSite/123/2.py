
import paramiko

hostname = "192.168.155.136"
port = 22
username = "pi"
password = "raspberry"

transport = paramiko.Transport((hostname, port))
transport.connect(username = username, password = password)

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.get("./Desktop/1.py", "C:/Users\\Artem\\Desktop\\123\\1.py")

sftp.close()