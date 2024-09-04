# Automated Telegram Group Messaging Enable/Disable Python Script
This script helps you enable/disable messaging on a target telegram group that you're an admin of or have administrative permission using the telethon library

# Concept
This Python script uses the official telegram core API wrapper telethon to control group message-sending ability and is useful for situations where you want to turn off messaging automatically at some specific time of the day and reopen it again after that time has passed. 

# Instructions
Install Python first and then install Telethon using the command
<pre>pip install telethon</pre>
Now, collect your <code>api_id</code> and <code>api_hash</code> from https://my.telegram.org/apps by creating an app first. Once collected, place them in the script placeholders.<br>
Now, set the correct group title and phone number used in your telegram account. First-time execution will ask you to create a session by logging in. It supports 2FA too.<br>
Once the session is ready, it can be used without authentication from the next time. At the bottom of the code, you may select whether you want to enable messaging or disable it in your target group.<br>
Only the name of the group is enough to find its unique group ID and control it.<br>
You may set different conditions as needed and schedule it at a specific time of the day and running the script will automate actions on your telegram group. Thanks to the telethon library.
