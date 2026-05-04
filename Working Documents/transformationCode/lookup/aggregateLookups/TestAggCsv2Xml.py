import csv
import xml.etree.ElementTree as ET

langList = ['en', 'es']
mrtList = []

with open('TestMRTLists.csv', newline='') as mrtfile:
    reader = csv.DictReader(mrtfile)
    for row in reader:
        mrtList.append((row['Source'],row['Regex'],row['Case']))

for mrt in mrtList:
    with open('TestAggregatePatternsTermLists.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        root = ET.Element("items")
        root.set('regex', mrt[1])
        root.set('case', mrt[2])
        for row in reader:
            if row['lookup_file'] == mrt[0]:
                for lang in langList:
                    item = ET.SubElement(root, 'item')
                    item.set('id', row['id'])
                    item.set('xml:lang', lang)
                    item.text = row['Term:'+lang].removesuffix('@'+lang)
        ET.indent(root)
        tree = ET.ElementTree(root)
        tree.write('test'+mrt[0], encoding="utf-8")
