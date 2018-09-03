import  socket
import  os

class Proxy :
    MAX_USER=100
    PORT=8888
    HOST=''
    ADDR=(HOST,PORT)
    MAX_LENGTH=1024

    def __init__(self):
        self.Init()

    def Init(self):
        self.main_fd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.main_fd.bind(self.ADDR)
        self.main_fd.listen(self.MAX_USER)


    def Work(self):
        while True:
            conn_fd,conn_addr=self.main_fd.accept()
            self.conn_msg={}
            self.conn_msg["client"]=conn_fd
            process_fd=os.fork()
            if process_fd is 0:
                self.main_fd.close()
                self.DealConn(conn_fd)
            else:
                conn_fd.close()

    def DealConn(self,fd):
        buf=[]
        buf=fd.recv(self.MAX_LENGTH)
        if buf is None:
            return
        print buf



if __name__ == '__main__':
    a=Proxy()
    a.Work()
