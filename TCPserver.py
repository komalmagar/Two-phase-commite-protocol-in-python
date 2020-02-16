import socket
s=socket.socket()
host=socket.gethostname()
port=9000
s.bind((host,port))
s.listen(1)
print("Waiting for connections")
conn,addr=s.accept()
print("client 1 is connected")
c="Welcome i am server"
conn.send(c.encode())
print("Waiting for 1 connection")
conn1,addr=s.accept()
print("client 2 is connected")
p="Welcome i am server"
conn1.send(p.encode())
while 1:
    message="Enter the response, either VOTE_COMMIT or VOTE_ABORT"
    message=message.encode()
    conn.send(message)
    conn1.send(message)
    print("message sent....")
    recv_message=conn.recv(1024)
    recv_message1=conn1.recv(1024)
    print("Vote of client 1 is",recv_message)
    print("Vote of client 2 is",recv_message1)
    mess="Let me think what to do now"
    mess=mess.encode()
    conn.send(mess)
    conn1.send(mess)
    if recv_message==recv_message1:
        message1="Transaction is Global Committed"
        message1=message1.encode()
        conn.send(message1)
        conn1.send(message1)
        recv_message2=conn.recv(1024)
        recv_message3=conn1.recv(1024)
        if recv_message2 or recv_message3:
            print("client  1",recv_message1)
            print("client  2",recv_message2)
    else:
       message2="Transaction is Global Aborted"
       message2=message2.encode()
       conn.send(message2)
       conn1.send(message2)
       conn.close()
       conn1.close()
       
