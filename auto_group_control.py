from telethon import TelegramClient, types, functions
from telethon.errors.rpcerrorlist import SessionPasswordNeededError
from time import sleep

# pip install telethon

# get api id and api hash from https://my.telegram.org/apps after creating an app there

api_id = ''
api_hash = ''
group_title = 'group name that you want to control'
phone_number = 'place phone number used in telegram account'

# Initialize the client
client = TelegramClient('mysession', api_id, api_hash)
group_id = None


async def disable_group(group_id):
    await client.connect()
    if not await client.is_user_authorized():
        print("User not authorized. Requesting code...")

        await client.send_code_request(phone_number)
        code = input('Enter the code: ')

        try:
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input('Two-step verification password: ')
            await client.sign_in(password=password)

        print("Authenticated")
    await client(functions.messages.EditChatDefaultBannedRightsRequest(
        peer=group_id,
        banned_rights=types.ChatBannedRights(
            until_date=None,
            send_messages=True
        )
    ))
    print("Group disabled successfully.")
    await client.disconnect()


async def reopen_group(group_id):
    await client.connect()
    if not await client.is_user_authorized():
        print("User not authorized. Requesting code...")
        await client.send_code_request(phone_number)
        code = input('Enter the code: ')

        try:
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input('Two-step verification password: ')
            await client.sign_in(password=password)

        print("Authenticated")
    await client(functions.messages.EditChatDefaultBannedRightsRequest(
        peer=group_id,
        banned_rights=types.ChatBannedRights(
            until_date=None,
            send_messages=False  # Allow sending messages
        )
    ))
    await client.disconnect()


async def get_private_group_id(group_title):
    global group_id
    await client.connect()

    if not await client.is_user_authorized():
        print("User not authorized. Requesting code...")
        phone_number = '+8801877524080'
        await client.send_code_request(phone_number)
        code = input('Enter the code: ')

        try:
            await client.sign_in(phone_number, code)
        except SessionPasswordNeededError:
            password = input('Two-step verification password: ')
            await client.sign_in(password=password)

        print("Authenticated")

    async for dialog in client.iter_dialogs():
        if dialog.is_group and dialog.title == group_title:
            group_id = dialog.id
            print(f"Group ID found: {dialog.id}")
            break
    else:
        print("Group not found.")

    await client.disconnect()


client.loop.run_until_complete(get_private_group_id(group_title))
sleep(2)
if group_id:
    # uncomment below link if you want to disable group messages
    # client.loop.run_until_complete(disable_group(group_id))
    
    # below line will reopen group messages
    client.loop.run_until_complete(reopen_group(group_id))
