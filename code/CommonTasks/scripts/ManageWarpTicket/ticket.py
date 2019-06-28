#!/usr/bin/python
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import sys, getopt
from ManageTicket import ManageTicket
import config_vars

def main(argv):
    inputVariable=getVariables(argv)
    ticket = ManageTicket(inputVariable)
    ticket.request()
    print(ticket.result)

def getVariables(argv):
    inputVariable = {}
    inputVariable.update( { 'ticketAction' : config_vars.ticket_action_default } )
    inputVariable.update( { 'ticketType' : config_vars.ticket_type_default } )
    inputVariable.update( { 'ticketNumber' : config_vars.ticket_ticketNumber_default } )
    inputVariable.update( { 'ticketSubject' : config_vars.ticket_subject_default } )
    inputVariable.update( { 'ticketDescription' : config_vars.ticket_description_default } )
    inputVariable.update( { 'ticketHost' : config_vars.ticket_host_default } )
    inputVariable.update( { 'ticketCsvFile' : None } )
    inputVariable.update( { 'ticketGroup' : None } )
    inputVariable.update( { 'ticketClient' : None } )
    inputVariable.update( { 'ticketCategory' : None } )
    inputVariable.update( { 'ticketSubcategory' : None } )
    inputVariable.update( { 'ticketProject' : None } )
    inputVariable.update( { 'ticketPriority' : None } )
    inputVariable.update( { 'debug' : 'no' } )
    inputVariable.update( { 'simulate' : 'no' } )

    try:
        opts, args = getopt.getopt(argv,"hDZt:T:n:s:d:H:c:g:C:S:P:p:G:")
    except getopt.GetoptError:
        showHelp()
        sys.exit()
    for opt, arg in opts:

        if opt == '-h':
            showHelp()
            sys.exit()

        elif opt in ("-t"):
            inputVariable.update( { 'ticketAction' : arg } )

        elif opt in ("-T"):
            inputVariable.update( { 'ticketType' : arg } )

        elif opt in ("-n"):
            inputVariable.update( { 'ticketNumber' : arg } )

        elif opt in ("-s"):
            inputVariable.update( { 'ticketSubject' : arg } )

        elif opt in ("-d"):
            inputVariable.update( { 'ticketDescription' : arg } )

        elif opt in ("-H"):
            inputVariable.update( { 'ticketHost' : arg } )

        elif opt in ("-c"):
            inputVariable.update( { 'ticketCsvFile' : arg } )

        elif opt in ("-g"):
            inputVariable.update( { 'ticketGroup' : arg } )

        elif opt in ("-C"):
            inputVariable.update( { 'ticketClient' : arg } )

        elif opt in ("-S"):
            inputVariable.update( { 'ticketSubcategory' : arg } )

        elif opt in ("-G"):
            inputVariable.update( { 'ticketCategory' : arg } )

        elif opt in ("-p"):
            inputVariable.update( { 'ticketProject' : arg } )

        elif opt in ("-P"):
            inputVariable.update( { 'ticketPriority' : arg } )

        elif opt == '-D':
            inputVariable.update( { 'debug' : 'yes' } )

        elif opt == '-Z':
            inputVariable.update( { 'simulate' : 'yes' } )


    return inputVariable

def showHelp():
    menu = '-----help menu ---- \n'
    menu += '-h this help menu \n'
    menu += '-T <type of Ticket> I(Trouble Ticket), M(Mudanca #default) or S(Service)\n'
    menu += '-t <type> O(open #default) or U(Update) F or C(Finish)\n'
    menu += '-n <number of ticket> (not applied on open)\n'
    menu += '-s <subject> \n'
    menu += '-d <description> \n'
    menu += '-H <host> \n'
    menu += '-c file <import CSV file>, <other file> \n'
    menu += '-g <Group to open Ticket (not required)> \n'
    menu += '-C <Cliente to open Ticket (not required)> \n'
    menu += '-G <Category Ticket (not required)> \n'
    menu += '-S <Subcategory Ticket (not required)> \n'
    menu += '-P Priority \n'
    menu += '-D Debug \n'
    menu += '-Z Simulate Send \n'
    print (menu)

if __name__ == "__main__":
   main(sys.argv[1:])
