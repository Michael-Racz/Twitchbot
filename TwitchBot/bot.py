#bot.py

import cfg
import utils
import socket
import re
import time, _thread
from time import sleep


def main():
    #Networking functions
    s= socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN {}\r\n".format(cfg.CHAN).encode("utf-8"))

    #_thread.start_new_thread(utils.threadFillOpList, ())
    #CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
    utils.chat(s, "hi mizzy wizzy!")

    start = time.time()
    while True:
        response = s.recv(2048).decode("utf-8")
        print(response)
        utils.mirror_msg(s,response)
        #sleep(5)
            
if __name__ == '__main__':
    main()