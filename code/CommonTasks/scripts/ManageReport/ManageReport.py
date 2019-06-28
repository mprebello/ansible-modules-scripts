#!/usr/bin/python
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import csv, re, sys, os
import report_config_vars

sys.path.append(report_config_vars.python_manage_host_detail_folder)
from ManageHostDetails import ManageHostDetails

sys.path.append(report_config_vars.python_useful_folder)
from ManageCsv import ManageCsv

class ManageReport(object):
    def __init__(self,inputVariable):
        self.__report_debug = inputVariable['debug']
        self.__report_file = inputVariable['reportFile']
        self.__report_host = inputVariable['reportHost']
        self.__report_status = inputVariable['reportStatus']
        self.__report_action = inputVariable['reportAction']
        self.__report_details = inputVariable['reportDetails']
        self.__report_details_list = self.__converToList(self.__report_details, ';')
        self.__report_fields = inputVariable['reportFields']
        self.__report_fields_list = self.__converToList(self.__report_fields, ',')
        #self.__report_import_file = inputVariable['reportImportFile']
        self.__host_details = ManageHostDetails(self.__report_host)
        self.__host_line = [ self.__host_details.report_client, self.__host_details.report_hostname, self.__host_details.report_ip ]
        self.__host_fields = inputVariable['reportFieldsHost']
        self.__host_fields_list = self.__converToList(self.__host_fields, ',')

    def apply(self):
        csv = ManageCsv(self.__report_file)
        if self.__report_action == 'I':
            header = self.__host_fields_list + self.__report_fields_list
            csv.createInitFile(header)

        elif csv.status is True:
            if self.__report_action == 'C':
                line = self.__host_line + self.__report_details_list
                csv.continueFile(line)

            elif self.__report_action == 'F':
                fieldToFilter = 'Host'
                csv.keepOnlyLastLine(fieldToFilter)

            else:
                self.__finishProgram('error to read file')
                return False
        else:
            self.__finishProgram('File is not Init')
            return False

    def __finishProgram(self,message):
        print(message)
        quit(-1)
        return False

    def __converToList(self, mylist, element):
        result = [x.strip() for x in mylist.split(element)]
        return result

    @property
    def result(self):
        return self.__response
