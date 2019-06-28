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
import shutil

class ManageCsv(object):
    def __init__(self, file):
        self.__file = file
        self.__status = self.__validate()

    def createInitFile(self, header):
        self.__header = header
        filecsv=open(self.__file, 'wt')
        writecsv = csv.writer(filecsv)
        writecsv.writerow( self.__header )
        filecsv.close()

    def continueFile(self, line):
        if self.__status:
            filecsv=open(self.__file, 'a')
            writecsv = csv.writer(filecsv)
            writecsv.writerow( line )
            filecsv.close()
        else:
            return False

    def keepOnlyLastLine(self, tableToFilter):
        if self.__status:
            table_csv = self.__convertCsvToTable()
            header = self.__captureHeader(table_csv)
            body_filtered = self.__filterBody(table_csv, tableToFilter)
            self.__copyReportToLog()
            self.__recreateMyFile(header, body_filtered)
        else:
            return False

    def __recreateMyFile(self, header, body_filtered):
        self.createInitFile(header)
        all_lines = []
        for row in body_filtered:
        	line = []
        	for head in header:
        		line.append(row[head])

        	self.continueFile(line)

    def __captureHeader(self, table_csv):
        file_csv=open(self.__file, 'rb')
        table_list = list(file_csv)
        table_header = table_list[0].strip().split(',')
        file_csv.close()
        return table_header

    def __convertCsvToTable(self):
        file_csv=open(self.__file, 'rb')
        table_csv = list(csv.DictReader(file_csv))
        file_csv.close()
        return table_csv

    def __filterBody(self, table_csv, tableToFilter):
        tables = []
        for row in table_csv:
            if row[tableToFilter] not in tables:
                tables.append(row[tableToFilter])

        new_table_csv = []
        for unit in tables:
            for row in table_csv:
                if row[tableToFilter] == unit:
                    line = row

            new_table_csv.append(line)

        return new_table_csv

    def __validate(self):
        answer = False
        if self.__verifyIfExist(self.__file):
            if self.__validateCsv(self.__file):
                answer = True

        return answer

    def __validateCsv(self, file):
        ctype = mimetypes.guess_type(file)
        if ctype[0] == 'text/csv':
            return True
        else:
            return False

    def __verifyIfExist(self, file):
        result = os.path.isfile(file)
        return result

    def __copyReportToLog(self):
        shutil.copyfile(self.__file, '{}.log'.format(self.__file))

    @property
    def status(self):
        return self.__status
