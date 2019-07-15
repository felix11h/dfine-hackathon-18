import pandas as pd


df = pd.read_csv('dzg/FFM_DEZ_180701.csv', error_bad_lines=False, encoding='ISO-8859-1')

import xml.etree.ElementTree as ET
tree = ET.parse('dzg/static.xml')

with open('dzg/static.xml') as fd:    
    xx = xmltodict.parse(fd.read(), encoding='latin1')

    

