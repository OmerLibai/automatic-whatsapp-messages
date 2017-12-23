# automatic whatsapp messages

using this short script, you can send whatsapp messages at specific times to specific contacts/groups through whatsapp web.
this script uses the [selenium](http://www.seleniumhq.org/) module.

**includes:**

* _a main script (you need to replace here the variable values to your contatct/message/time)._
* _a time config file which contains time functions that helps the main program._

## instructions for use

* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _message's_ value (in the main function's declaration) to the message you would like to send.
* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _target's_ value to the name of the group or contact you want to send the message to.
* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _bot_message's_ value to a something you would like to change at the end of every message.
* In [main.py](https://github.com/OmerLibai/automatic-whatsapp-messages/blob/master/main.py) change _COMPUTER_PHONE_DELAY's_ value to the delay in seconds between your computer's time and your phone's time.
