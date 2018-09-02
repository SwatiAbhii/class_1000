import imaplib
import email
import os

#svdir = 'C:\\Users\\swatthakur\\desktop\\EMAIL ADP'

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("username", "pwd")
mail.select("Inbox")
