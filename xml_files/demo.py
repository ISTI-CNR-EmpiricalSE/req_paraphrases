from xml.dom import minidom

# parse xml file
file = minidom.parse('demo.xml')

# grab all <record> tags
records = file.getElementsByTagName("record")

print("Name------>Phone")

for record in records:
    # access <name> and <phone> node of every record
    name = record.getElementsByTagName("name")
    phone = record.getElementsByTagName("phone")

    # access data of name and phone
    print(name[0].firstChild.data, end="----->")
    print(phone[0].firstChild.data)