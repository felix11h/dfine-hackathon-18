import pandas as pd


df = pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False, encoding='ISO-8859-1')

import xml.etree.ElementTree as ET
tree = ET.parse('dzg/static.xml')

with open('dzg/static.xml') as fd:    
    xx = xmltodict.parse(fd.read(), encoding='latin1')

    

tree.findall("./")
tree.findall("./{http://schemas.xmlsoap.org/soap/envelope/}Body")
tree.findall(".//{http://schemas.xmlsoap.org/soap/envelope/}Body")
tree.findall(".//{http://schemas.xmlsoap.org/soap/envelope/}Body/")
tree.findall(".//{http://datex2.eu/schema/2/2_0}period")


import xml.etree.ElemetTree
from xml.dom import minidom
xmldoc = minidom.parse('static.xml')
il = xmldoc.getElementsByTagName('referentIdentifier')
il
len(_)
il = xmldoc.getElementsByTagName('startPointOfLinearElement')
len(_)
len(il)
il[0].attributes['referentIdentifier']
print(il[0])
il.attributes
x=il[0]
x
x.getAttribute('referentIdentifier')
x.getAttribute('referentIdentifier')
import pandas as pd
pd.read_csv('dzg/FFM_DEZ_180701.csv')
pd.read_csv('dzg/FFM_DEZ_180701.csv')
cd ..
pd.read_csv('dzg/FFM_DEZ_180701.csv')
pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False)
pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False, header=None)
pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False, encoding='utf-8')
pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False, encoding='ISO-8859-1')
df = pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False, encoding='ISO-8859-1')
df
df.head()
df = pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False, encoding='ISO-8859-1', sep='\t')
df.head()
%hist
df.head()
x = df['ElemUID']
len(x)
x[0]
y = np.unique(x)
import numpy as np
y = np.unique(x)
len(y)
y[0]
x[0]
y[0]
xmldoc.w
df[0]
df.head()
df.keys()
df['ElemName']
import xmltodict
import xmltodict
xx = xmltodict('dzg/FFM_DEZ_180701.csv')
with open('dzg/FFM_DEZ_180701.csv') as fd:
    xx = xmltodict.parse(fd.read())
with open('dzg/FFM_DEZ_180701.csv') as fd:
    xx = xmltodict.parse(fd.read(), encoding=''ISO-8859-1')
with open('dzg/FFM_DEZ_180701.csv') as fd:
    xx = xmltodict.parse(fd.read(), encoding='ISO-8859-1')
with open('dzg/FFM_DEZ_180701.csv') as fd:
    xx = xmltodict.parse(fd.read(), encoding='latin1')
import lxml
import xml.etree.ElementTree as ET
tree = ET.parse('dzg/FFM_DEZ_180701.csv')
tree = ET.parse('dzg/static.xml')
with open('dzg/static.xml') as fd:
    
    xx = xmltodict.parse(fd.read(), encoding='latin1')
%hist
tree.get_root()
tree.getroot()
for pp in root.iter('measurementSiteIdentification'):
    print(pp)
root = tree.getroot()
for pp in root.iter('measurementSiteIdentification'):
    print(pp)
tree.findall("./..@[name='measurementSiteIdentification'")
tree.findall("./..[@name='measurementSiteIdentification'")
tree
tree.findall(".")
tree.findall("[measurementSiteIdentification]")
tree.findall("[period]")
tree.findall(".//[period]")
tree.findall(".//")
tree.findall(".//[period]")
tree.findall(".//..[period]")
tree.findall(".//period")
tree.findall(".//[tag=period]")
tree.findall(".//[@attrib=60.]")
xx
with open('dzg/static.xml') as fd:
    xx = xmltodict.parse(fd.read(), encoding='latin1')
xx
tree.findall(".")
tree.findall('{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
tree.findall('./{http://schemas.xmlsoap.org/soap/envelope/}Envelope')
tree.findall(".//[1]")
tree.findall("./")
tree.findall("./{http://schemas.xmlsoap.org/soap/envelope/}Body")
tree.findall(".//{http://schemas.xmlsoap.org/soap/envelope/}Body")
tree.findall(".//{http://schemas.xmlsoap.org/soap/envelope/}Body/")
tree.findall(".//{http://datex2.eu/schema/2/2_0}period")
%hist
tree.findall(".//{http://datex2.eu/schema/2/2_0}period")
tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteRecord")
tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteLocation")
lx = tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteLocation")
lx[0]
lx[0]['{http://datex2.eu/schema/2/2_0}externalReferencing']
lx[0][0]
lx[0][0][0]
lx[0][0][0].value()
lx[0][0][0].value.text
lx[0][0][0]..text
lx[0][0][0].text
exLocs = [x[0][0][0].text for in lx]
exLocs = [x[0][0][0].text for x in lx]
lx = tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteLocation")
lx = tree.findall(".//[@name={http://datex2.eu/schema/2/2_0}measurementSiteLocation/")
lx = tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteIdentification")
lx
lx = tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteIdentification/..[@name={http://datex2.eu/schema/2/2_0}measurementSiteRecord]")
lx = tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteIdentification/..[@name='{http://datex2.eu/schema/2/2_0}measurementSiteRecord']")
lx
lx = tree.findall(".//{http://datex2.eu/schema/2/2_0}mmeasurementSiteRecord")
lx
lx = tree.findall(".//{http://datex2.eu/schema/2/2_0}measurementSiteRecord")
lx
len(lx)
for x in lx:
    x.findall('{http://datex2.eu/schema/2/2_0}measurementSiteLocation')
for x in lx:
    x.findall('./{http://datex2.eu/schema/2/2_0}measurementSiteLocation')
lx
x = lx[0]
x
x[0]
x.findall('{http://datex2.eu/schema/2/2_0}measurementSiteNumberOfLanes')
for x in lx:
    x.findall('{http://datex2.eu/schema/2/2_0}measurementSiteLocation')
for x in lx:
    x.findall('{http://datex2.eu/schema/2/2_0}measurementSiteIdentification')
%hist
