#!/usr/bin/python
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import csv, re, requests, sys, os
import config_vars

sys.path.append(config_vars.python_manage_host_detail_folder)
from ManageHostDetails import ManageHostDetails

sys.path.append(config_vars.python_useful_folder)
from ConvertCsv import ConvertCsv

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class ManageTicket(object):
    def __init__(self,inputVariable):
        self.__ticket_debug = inputVariable['debug']
        self.__ticket_simulate = inputVariable['simulate']
        self.__ticket_subject = inputVariable['ticketSubject']
        self.__ticket_host = inputVariable['ticketHost']
        self.__ticket_type = inputVariable['ticketType']
        self.__ticket_action = inputVariable['ticketAction']
        self.__ticket_number = inputVariable['ticketNumber']
        self.__ticket_csv_file = inputVariable['ticketCsvFile']
        self.__ticket_web_destination_change = config_vars.ticket_dest_change
        self.__ticket_web_destination_incident = config_vars.ticket_dest_incident
        self.__ticket_group = inputVariable['ticketGroup']
        self.__ticket_client = inputVariable['ticketClient']
        self.__ticket_subcategory = inputVariable['ticketSubcategory']
        self.__ticket_category = inputVariable['ticketCategory']
        self.__ticket_project = inputVariable['ticketProject']
        self.__ticket_priority = inputVariable['ticketPriority']
        self.__ticket_alert_id = None
        self.__message_adds = ''
        self.__defineWebRequest()
        self.__host_details = ManageHostDetails(self.__ticket_host)
        self.__defineVariables()
        self.__ticket_description =  inputVariable['ticketDescription']
        self.__description = ''
        self.__generateDescription()

    def __defineWebRequest(self):
        if self.__ticket_type == 'M':
            self.__ticket_web_destination = self.__ticket_web_destination_change

        elif self.__ticket_type == 'I':
            self.__ticket_web_destination = self.__ticket_web_destination_incident

        elif self.__ticket_type == 'S':
            self.__ticket_web_destination = self.__ticket_web_destination_incident

        else:
            print('error')
            exit(-1)

    def __generateDescription(self):
        self.__description += self.__ticket_description
        if self.__ticket_csv_file != None:
            csv_to_warp = ConvertCsv(self.__ticket_csv_file)
            self.__description += csv_to_warp.convertCsvToWarp()

    def __defineVariables(self):
        if  self.__ticket_group == None:
            self.__ticket_group = self.__host_details.warp_group

        if  self.__ticket_client == None:
            self.__ticket_client = self.__host_details.warp_client

    def request(self):
        if self.__ticket_type == 'M':
            inputResponse = {
                'TICKET': (None, self.__ticket_type),
                'titulo': (None, self.__ticket_subject[0:49]),
                'email_contato': (None, self.__host_details.warp_mail),
                'argushost': (None, self.__host_details.warp_hostname),
                'prazo': (None, self.__host_details.warp_deadline),
                'grupo': (None, self.__ticket_group),
                'cliente': (None, self.__ticket_client),
                'descricao': (None, self.__description),
            }
        else:
            inputResponse = {
                'TICKET': (None, self.__ticket_type),
                'ACTION': (None, self.__ticket_action),
                'CLIENT_NAME': (None, self.__ticket_client),
                'GROUP': (None, self.__ticket_group),
                'SUMMARY': (None, self.__ticket_subject[0:49]),
                'DESCRIPTION': (None, self.__description),
                'CONFIGURATION_ITEM': (None, self.__host_details.warp_hostname),
                'EMAIL': (None, self.__host_details.warp_mail),
            }

            if self.__ticket_alert_id != None:
                inputResponse.update({'ALERT_ID': (None, self.__ticket_alert_id)})

            if self.__ticket_priority != None:
                inputResponse.update({'PRIORITY': (None, self.__ticket_priority)})

            if self.__ticket_project != None:
                inputResponse.update({'PROJECT': (None, self.__ticket_project)})

            if self.__ticket_category != None:
                inputResponse.update({'CATEGORY': (None, self.__ticket_category)})

            if self.__ticket_subcategory != None:
                inputResponse.update({'SUBCATEGORY': (None, self.__ticket_subcategory)})

        if self.__ticket_debug == 'yes':
            print('connect on : {}\n variables:{}'.format(self.__ticket_web_destination, inputResponse))

        if self.__ticket_simulate == 'no':
            self.__manageWarpTicket(inputResponse)
        else:
            quit()

    def __manageWarpTicket(self,inputResponse):
        try:
            response = requests.post(self.__ticket_web_destination, files=inputResponse, verify=False)
        except requests.ConnectionError:
            response = 'error'

        self.__validateResponse(response)

    def __validateResponse(self,response):
        self.__response_raw=response
        self.__response='error'
        if  isinstance(response, requests.models.Response):
            if response.status_code == 200 and response.content != '' and 'Ocorreu um erro' not in response.content:
                self.__response=response.content.strip()

    @property
    def result(self):
        return self.__response

    @property
    def result_raw(self):
        return self.__response_raw
