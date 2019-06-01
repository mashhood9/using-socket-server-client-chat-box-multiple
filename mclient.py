import socket
SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))
name = input()
while True:
  in_data =  client.recv(1024)
  print("From Server :" ,in_data.decode())
  def send_cl(msg,cl_name)
  out_data = input()
  message= ("from client" + " " + name + ":- " + out_data)  
  client.sendall(bytes(message,'UTF-8'))
  if out_data=='bye':
      break
client.close()
