#!/usr/bin/python
# -*- coding: utf-8 -*-
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import sys, smtplib, getopt , re, os, csv
import mimetypes
import config_vars
from ConvertCsvToHtml import ConvertCsvToHtml
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

class ManageMail(object):
    def __init__(self,inputVariable):
        self.__smtp_server = config_vars.smtp_server
        self.__email_from = config_vars.smtp_from

        self.__email_to = inputVariable['emailTo']
        self.__email_to_splited = self.__splitByComma(inputVariable['emailTo'])

        self.__message_user = inputVariable['emailMessage']

        self.__message_adds = ''

        self.__message_attach = inputVariable['emailAttach']
        self.__message_attach_splited = self.__splitByComma(inputVariable['emailAttach'])

        self.__message_csv_to_html = inputVariable['csvToHtml']
        self.__message_csv_to_html_splited = self.__splitByComma(inputVariable['csvToHtml'])

        self.__message_header = config_vars.message_header
        self.__message_footer = config_vars.message_footer

        self.__message_body = ''
        self.__message_subject = inputVariable['emailSubject']

    def sentMessage(self):
        self.__initEmailConfiguration()
        self.__treatAttach()
        self.__treatCsvToHtml()
        self.__mountFinalMessage()
        self.__attachMessageToEmail()
        self.__sentMessage()

    def __treatCsvToHtml(self):
        if self.__message_csv_to_html_splited != None:
            for csv in self.__message_csv_to_html_splited:
                csv_stripped = csv.strip()
                if self.__verifyIfExist(csv_stripped):
                    converted_csv = ConvertCsvToHtml(csv_stripped)
                    converted_csv_answer = converted_csv.convertCsv()
                    self.__message_adds += '<br>'
                    self.__message_adds += converted_csv_answer

    def __sentMessage(self):
        server = smtplib.SMTP(self.__smtp_server)
        result = server.sendmail(self.__email_from , self.__email_to_splited, self.__message_html.as_string())
        server.quit()

    def __splitByComma(self, variable):
        if variable == None:
            variable_splited = None
        else:
            variable_splited = re.split(',', variable)

        return variable_splited

    def __initEmailConfiguration(self):
        self.__message_html = MIMEMultipart()
        self.__message_html["From"] = self.__email_from
        self.__message_html["To"] = self.__email_to
        self.__message_html["Subject"] = self.__message_subject
        self.__message_html.preamble = self.__message_subject

    def __mountFinalMessage(self):
        self.__final_message = "{}<br>".format(self.__message_header)
        self.__final_message += "{}<br> ".format(self.__message_user)
        self.__final_message += "{}<br> ".format(self.__message_adds)
        self.__final_message += "{}<br> ".format(self.__message_footer)

    def __attachMessageToEmail(self):
        self.__message_html.attach(MIMEText(self.__final_message, 'html'))

    def __convertAttach(self,fileToSend):
        ctype, encoding = mimetypes.guess_type(fileToSend)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)

        if maintype == "text":
            fp = open(fileToSend)
            attachment = MIMEText(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "image":
            fp = open(fileToSend, "rb")
            attachment = MIMEImage(fp.read(), _subtype=subtype)
            fp.close()
        elif maintype == "audio":
            fp = open(fileToSend, "rb")
            attachment = MIMEAudio(fp.read(), _subtype=subtype)
            fp.close()
        else:
            fp = open(fileToSend, "rb")
            attachment = MIMEBase(maintype, subtype)
            attachment.set_payload(fp.read())
            fp.close()
            encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=os.path.basename(fileToSend))
        return attachment

    def __treatAttach(self):
        if self.__message_attach_splited != None:
            for attach in self.__message_attach_splited:
                attach_stripped = attach.strip()
                if self.__verifyIfExist(attach_stripped):
                    attach_filtered = self.__convertAttach(attach_stripped)
                    self.__message_html.attach(attach_filtered)

    def __verifyIfExist(self, file):
        result = os.path.isfile(file)
        return result
