#!/usr/bin/python
# -*- coding: utf-8 -*-
#====================================================================
# Manage Ticket Script
# Date: 2018/04/16
# Author: Marcel Rebello
# mail: marcel.rebello@br.unisys.com
# ====================================================================
import csv, re
import mimetypes
import config_vars

class ConvertCsvToHtml(object):
    def __init__(self, file):
        self.__file_to_convert = file
        self.__rules_validate_color = config_vars.rules_validate_color

    def convertCsv(self):
        if self.__validateCsv():
            csv_to_html = self.__convertCsvintoTable()
            return csv_to_html
        else:
            answer = 'File {} Not Csv'.format(self.__file_to_convert)
            return answer

    def __validateCsv(self):
        ctype = mimetypes.guess_type(self.__file_to_convert)[0]
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


    def __convertCsvintoTable(self):
        filecsv=open(self.__file_to_convert, 'rb')
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
