# automatic whatsapp messages

using this short script, you can send whatsapp messages at specific times to specific contacts/groups through whatsapp web.
this script uses the [selenium](http://www.seleniumhq.org/) module.

**includes:**

* _a main script (you need to replace here the variable values to your contatct/message/time)._
* _a time config file which contains time functions that helps the main program._

## instructions for use

* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _MY_MESSAGE's_ value to the message you would like to send.
* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _target's_ value to the name of the group or contact you want to send the message to.
* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _bot_message's_ value to a something you would like to change at the end of every message.
* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _COMPUTER_PHONE_DELAY's_ value to the delay in seconds between your computer's time and your phone's time.
* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _CHROME_PROFILE_PATH's_ value to the chrome profile you want to open.

Of course, it's much more simple just writing the parameters through the command line, which of course you can do.
The first parameter is the target time, the second is your message and the third is the contact's/group's name.

### using a profile

_note: it is recommended to make a chrome profile specifically for this program's use as when the program ends, it closes all chrome tabs of the profile._

In order to use a chrome profile so that you can load the program each time without logging into whatsapp, you must follow these instructions:
* if you're using your default chrome profile, just change _CHROME_PROFILE_PATH's_ value to the directory containing the Default folder.
* if not: copy your profile folder (named something like profile1) into a seperate folder. Personally, I recommend an unused folder as while the program runs, this folder will be filled with files.
* Change the folder name (profile1 or something similar) to "Default".
* change _CHROME_PROFILE_PATH's_ value to the directory containing the folder.

**Always link to the parent directory of the default folder.**
For example: if my path is C:\profile\default, then CHROME_PROFILE_PATH's value'll be C:\profile.

 

### loading the program on start
For instructions on how to load the program on computer start click [here](https://stackoverflow.com/questions/4438020/how-to-start-a-python-file-while-windows-starts).
These are simple instructions from a stack overflow page.