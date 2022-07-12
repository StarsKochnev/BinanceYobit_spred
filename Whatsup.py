import pywhatkit
import os

def send_messege_inst():
    mobile = '+79202379114'
    messege = '13'
    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=messege)
def main():
    send_messege_inst()
if __name__ == '__main__':
    main()
