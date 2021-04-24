#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram import Update, Bot
from telegram.ext import *
from telegram.ext import CallbackContext
from emoji import emojize
import csv, sys, time, os.path, pandas, telegram
from telegram.utils.request import Request



def checkMessage(update, bot):
    print(update.message.text) 	# take text message

    user_message = update.message.text
    user = update.message.from_user
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id
    
    if update.message.text in ("f"):
        print(chat_id)
        print(user)
        # bot.kickChatMember(chat_id, user.id)
        print(bot)
        # bot.kick_chat_member(self, chat_id, user_id, revoke_messages)
        bot.kickChatMember(self, chat_id, user_id, revoke_messages)
    else:
        print("ok ko xoa")


def main():
    #    importCSV()
    print("start")
    updater = Updater("1775245963:AAHwADeOSyKbbUA4XvIGXxFlJQLiJVycKLg")
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, checkMessage))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
