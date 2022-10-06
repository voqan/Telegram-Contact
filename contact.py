#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import telethon.sync
from telethon import TelegramClient, utils
from telethon.tl.functions.contacts import GetContactsRequest, ImportContactsRequest
from telethon.tl.types import InputPeerUser, InputPhoneContact, UserFull
from pymongo import MongoClient
from bson.json_util import dumps
from telethon.tl.functions.users import GetFullUserRequest

prof = sys.argv[1]
fname = sys.argv[2]
dict_to_apend= {}

connect_mongo = MongoClient()
ExistingDbs = connect_mongo.database_names()
db = connect_mongo.myDB


api_id = xxxxxx
api_hash = 'FILL ME IN'


client = TelegramClient('/var/www/html/telegram/tracker', api_id, api_hash)
client.start()

contact = InputPhoneContact(client_id = 0, phone = prof, first_name=fname, last_name="")
result = client(ImportContactsRequest([contact]))
contacts = client(GetContactsRequest(0))


me = client.get_entity(prof)

pic = client.download_profile_photo(me, '/var/www/html/telegram/')
#print (pic)

fn = str(me.first_name)
#print("First name: " + str(me.first_name))

ln = str(me.last_name)
#print("Last name: " + str(me.last_name))

jina = str(me.username)
#print("Username: " + str(me.username))

namba = str(me.phone)
#print("Phone number: " + str(me.phone))

picha = str(me.photo)
#print("Photo: " + str(me.photo))

status = str(me.status)
#print("Status: " + str(me.status))

eyed = str(me.id)
#print("id: " + str(me.id))

acces = str(me.access_hash)
#print("access_hash: " + str(me.access_hash))

bot = str(me.bot)
#print("Bot: " + str(me.bot))

contact = str(me.contact)
#print("Contact: " + str(me.contact))

verified = str(me.verified)
#print("Verified: " + str(me.verified))

replycomment = {"First name": fn, "Last name": ln, "Username": jina, "Phone number": namba, "Status": status, "Photo": picha, "user_id": eyed, "access_hash": acces, "Bot": bot, "Contact": contact, "Verified": verified} 
db.telegram.update({"Number": prof, "Name":fname}, {"$push": {"Profile": replycomment}},upsert=True)

print ('output saved to MongoDb')



