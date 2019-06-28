#!/usr/bin/python
# -*- coding: utf-8 -*-
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import sys, getopt , re, os, csv
from ManageMail import ManageMail

def main(argv):
    inputVariable = getVariables(argv)
    mail = ManageMail(inputVariable)
    mail.sentMessage()

def showHelp():
    print ('-----help menu ---- \n\
            -t to email\n\
            -s subject\n\
            -m message\n\
            -D Debug \n\
            -a Attach \n\
            -H Convert to html \n\
            ')

def getVariables(argv):
    mail_attach = []
    mail_to = 'marcel@uninet.com.br'
    inputVariable={}
    inputVariable.update( { 'emailTo' : mail_to } )
    inputVariable.update( { 'emailMessage' : 'No Message' } )
    inputVariable.update( { 'emailSubject' : 'No Subject' } )
    inputVariable.update( { 'emailAttach' : None } )
    inputVariable.update( { 'csvToHtml' : None } )
    try:
        opts, args = getopt.getopt(argv,"ht:s:m:a:C:")
    except getopt.GetoptError:
        showHelp()
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            showHelp()
            sys.exit()
        elif opt in ("-t"):
            inputVariable.update( { 'emailTo' : arg } )

        elif opt in ("-m"):
            inputVariable.update( { 'emailMessage' : arg } )

        elif opt in ("-s"):
            inputVariable.update( { 'emailSubject' : arg } )

        elif opt in ("-a"):
            inputVariable.update( { 'emailAttach' : arg } )

        elif opt in ("-C"):
            inputVariable.update( { 'csvToHtml' : arg } )


    return inputVariable


def validateAttach(attach_raw):
    attach = attach_raw.strip()
    if os.path.exists(attach):
        return attach
    else:
        print('file {} - not find'.format(attach))
        exit (-1)

if __name__ == "__main__":
    main(sys.argv[1:])
