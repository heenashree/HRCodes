import xml.etree.ElementTree as ET
tree = ET.parse('abc.xml')
root = tree.getroot()
print (root)
print("Hello")
root = ET.fromstring(country_data_as_string)