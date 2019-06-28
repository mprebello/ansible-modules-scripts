#!/usr/bin/python
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import sys, getopt
from ManageReport import ManageReport
import report_config_vars

def main(argv):
    inputVariable=getVariables(argv)
    csv = ManageReport(inputVariable)
    csv.apply()

def getVariables(argv):
    inputVariable = {}
    inputVariable.update( { 'reportFile' : report_config_vars.report_name_default } )
    inputVariable.update( { 'reportAction' : report_config_vars.report_action_default } )
    inputVariable.update( { 'reportHost' : report_config_vars.report_host_default } )
    inputVariable.update( { 'reportStatus' : report_config_vars.report_status_default } )
    inputVariable.update( { 'reportDetails' : report_config_vars.report_details_default } )
    inputVariable.update( { 'reportFields' : report_config_vars.report_field_default } )
    inputVariable.update( { 'reportFieldsHost' : report_config_vars.report_fieldhost_default } )
    inputVariable.update( { 'debug' : 'no' } )

    try:
        opts, args = getopt.getopt(argv,"hDA:N:H:S:T:F:")
    except getopt.GetoptError:
        showHelp()
        sys.exit(-1)
    for opt, arg in opts:

        if opt == '-h':
            showHelp()
            sys.exit()

        elif opt in ("-N"):
            inputVariable.update( { 'reportFile' : arg } )

        elif opt in ("-A"):
            inputVariable.update( { 'reportAction' : arg } )

        elif opt in ("-H"):
            inputVariable.update( { 'reportHost' : arg } )

        elif opt in ("-S"):
            inputVariable.update( { 'reportStatus' : arg } )

        elif opt in ("-T"):
            inputVariable.update( { 'reportDetails' : arg } )

        elif opt in ("-F"):
            inputVariable.update( { 'reportFields' : arg } )

        elif opt == '-D':
            inputVariable.update( { 'debug' : 'yes' } )

    return inputVariable

def showHelp():
    menu = '-----help menu ---- \n'
    menu += '-h this help menu \n'
    menu += '-A <Action I(INIT) C(CONTINUE) F(FINISH)>  \n'
    menu += '-N <Report>\n'
    menu += '-H <host> \n'
    menu += '-S <status> \n'
    menu += '-T <details> \n'
    print (menu)

if __name__ == "__main__":
   main(sys.argv[1:])
