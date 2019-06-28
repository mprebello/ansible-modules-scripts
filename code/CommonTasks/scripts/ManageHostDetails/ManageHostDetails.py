#!/usr/bin/python
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import csv, re, shutil
import config_vars_host_details

class ManageHostDetails(object):
    def __init__(self,host):
        self.__host = host
        self.__filecsv = config_vars_host_details.host_details_filecsv
        self.__warp_hostname = config_vars_host_details.host_details_warp_hostname
        self.__warp_project =  config_vars_host_details.host_details_warp_project
        self.__warp_descserver =  config_vars_host_details.host_details_warp_descserver
        self.__warp_group =  config_vars_host_details.host_details_warp_group
        self.__warp_mail =  config_vars_host_details.host_details_warp_mail
        self.__warp_deadline =  config_vars_host_details.host_details_warp_deadline
        self.__warp_client =  config_vars_host_details.host_details_warp_client
        self.__report_client =  config_vars_host_details.host_details_report_client
        self.__report_hostname = self.__host
        self.__report_ip =  config_vars_host_details.host_details_report_ip
        self.__capture_in_file()

    def __capture_in_file(self):
        ticketVariables = None
        csv_file = csv.DictReader(open(self.__filecsv, "rb"), delimiter=";")
        for row in csv_file:
            if row['server'] == self.__host:
                self.__warp_hostname = row['warphostname']
                self.__warp_project = row['warpproject']
                self.__warp_descserver =  row['descserver']
                self.__warp_group = row['warpgroup']
                self.__warp_mail = row['warpmail']
                self.__warp_deadline = row['warpdeadline']
                self.__warp_client = row['warpclient']
                self.__report_client = row['reportclient']
                self.__report_hostname = row['reporthostname']
                self.__report_ip = row['reportip']

    @property
    def warp_deadline(self):
        return self.__warp_deadline

    @property
    def warp_project(self):
        return self.__warp_project

    @property
    def warp_descserver(self):
        return self.__warp_descserver

    @property
    def warp_hostname(self):
        return self.__warp_hostname

    @property
    def warp_project(self):
        return self.__warp_project

    @property
    def warp_group(self):
        return self.__warp_group

    @property
    def warp_mail(self):
        return self.__warp_mail

    @property
    def warp_client(self):
        return self.__warp_client

    @property
    def report_client(self):
        return self.__report_client

    @property
    def report_hostname(self):
        return self.__report_hostname

    @property
    def report_ip(self):
        return self.__report_ip
