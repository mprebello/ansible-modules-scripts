#!/usr/bin/python
# -*- coding: utf-8 -*-
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import csv, re, os
import mimetypes
import userful_config
from prettytable import PrettyTable
from prettytable import from_csv

class ConvertCsv(object):
    def __init__(self, file):
        self.__file_to_convert = file
        self.__file_to_convert_splited = self.__splitByComma(self.__file_to_convert)
        self.__rules_validate_color = userful_config.rules_validate_color
        self.__final_message = ''

    def __convertCsvToHtml(self, csv_stripped):
        if self.__validateCsv(csv_stripped):
            csv_to_html = self.__convertCsvintoTable(csv_stripped)
            return csv_to_html
        else:
            answer = 'File {} Not Csv'.format(csv_stripped)
            return answer

    def __validateCsv(self, csv_stripped):
        ctype = mimetypes.guess_type(csv_stripped)[0]
        if ctype == 'text/csv':
            return True
        else:
            return False

    def __analisysField(self, line):
        default_value = ''
        for rule in self.__rules_validate_color:
            field = rule[0]
            regex = rule[1]
            value = 'bgcolor={}'.format(rule[2])
            if field in line:
                if re.findall(regex, line[field]):
                    return value

        return default_value

    def __splitByComma(self, variable):
        if variable == None:
            variable_splited = None
        else:
            variable_splited = re.split(',', variable)

        return variable_splited

    def convertCsvToHtml(self):
        if self.__file_to_convert_splited != None:
            for csv in self.__file_to_convert_splited:
                csv_stripped = csv.strip()
                if self.__verifyIfExist(csv_stripped):
                    converted_csv_answer = self.__convertCsvToHtml(csv_stripped)
                    #self.__final_message += '<br>'
                    #self.__final_message += 'file {}'.format(os.path.basename(csv_stripped))
                    self.__final_message += '<br>'
                    self.__final_message += converted_csv_answer

        return self.__final_message

    def convertCsvToWarp(self):
        if self.__file_to_convert_splited != None:
            for csv in self.__file_to_convert_splited:
                csv_stripped = csv.strip()
                if self.__verifyIfExist(csv_stripped):
                    converted_csv_answer = self.__convertCsvToWarp(csv_stripped)
                    self.__final_message += '<br>'
                    self.__final_message += converted_csv_answer

        return self.__final_message

    def __convertCsvToWarp(self, file):
        with open(file, 'rb') as f:
            reader = from_csv(f)

        table_converted = re.sub('\n', '<br>', str(reader))
        table_converted_with_tab = re.sub(' ', '&nbsp;', table_converted)
        return table_converted_with_tab

    def __verifyIfExist(self, file):
        result = os.path.isfile(file)
        return result

    def __convertCsvintoTable(self, file):
        filecsv=open(file, 'rb')
        tablecsv = csv.DictReader(filecsv)
        head = tablecsv.fieldnames
        tableconverted = list(tablecsv)

        body='<table cellspacing=\'0\' border=\'1\'><tr bgcolor=Black>'
        for line in head:
            body+='<td valign=\'top\' ><font color=\'white\'><b>{}</b></font></td>'.format(line)

        body+='</tr>'

        failcolor='#ff3300'
        okcolor='#ebfafa'
        partialcolor='#ffb84d'
        nonecolor='#ffff4d'
        bg_color=''

        for line in tableconverted:
            bg_color = self.__analisysField(line)
            body+='<tr {} >'.format(bg_color)
            for i in head:
                body+='<td valign=\'top\'>{}</td>'.format(line[i])
            body+='</tr>'

        body+='</table>'
        return body
