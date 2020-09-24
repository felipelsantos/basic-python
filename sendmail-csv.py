#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
import csv
import sys

sender_mail = "xxxxxx@xxxx.xxx"
sender_pass = "xxxxxxxxxx"


s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(sender_mail, sender_pass)

with open(sys.argv[1], encoding="utf-16") as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0

	for row in csv_reader:
		line_count +=1

		name = row[0]
		receiver_mail = row[1]

		from_mail = "xxxxxxxx"
		subject = "xxxxxxxxxx"
		text = "xxxxxxx {}".format(row[0])

		msg = 'From: {}\nSubject: {}\n\n{}'.format(from_mail,subject, text).encode('utf-8')

		s.sendmail(sender_mail, receiver_mail, msg)
s.quit()
