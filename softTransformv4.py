#!/usr/bin/python
# -*- coding: utf-8 -*-
# 
#   FILE: softTransform.py
#   DATE: 9.7.17
#   Author: Euan Cochrane
#

#This is a program written in Python3 that will start from a list of Yale University Library (YUL) barcodes and then pull out some fields from the JSON returned by the Voyager API to feed into YUL bot for Wikidata uploading. 


from __future__ import unicode_literals  
import sys
import os
import urllib.request
import xml
from xml import etree
import xml.etree.ElementTree as ET
import glob
import csv
allRows = []
barcodeBibs = {}
sourceCSV = str(sys.argv[1])
outCSV = str(sys.argv[2])
     
with open(sourceCSV, "r") as scsvInput:
    with open(outCSV, "w") as scsvOutput:
       
        csvWriteFile = csv.writer(scsvOutput, lineterminator='\n')
        csvFile = csv.reader(scsvInput)
        allRows = []
        #print(csvFile)
        counter = 0
        for row in csvFile:
            if counter == 0:
              row.append("title")
              row.append("oclc number")
            
            bibID = row[2]  
            print("procesing: " + bibID)
            MARCURL = "http://deleon.library.yale.edu:9090/VoySearch/GetBibMarc?bibid=" + str(bibID)
            try:
                MARCXML = urllib.request.urlopen(MARCURL)
                parsedMARCXML = ET.parse(MARCXML)
                MARCTitle = parsedMARCXML.findall(".//*[@tag='245']/{http://www.loc.gov/MARC21/slim}subfield[@code='a']")
                for title in MARCTitle:
        
                    row.append(title.text)
        
                
                OCLCNum = parsedMARCXML.findall(".//*[@tag='079']/{http://www.loc.gov/MARC21/slim}subfield[@code='a']")
                for oclc in OCLCNum:
                    if oclc.text[:3] == "ocm":
                        pass
                        print("oclc num = " + oclc.text)
                        print("clean oclc num = " + oclc.text[3:])
                        row.append(oclc.text[3:])
            except IOError:
                pass
            counter = counter + 1
            allRows.append(row)    
        
        csvWriteFile.writerows(allRows)
        scsvInput.close()
        scsvOutput.close()
