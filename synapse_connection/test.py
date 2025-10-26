import xml.etree.ElementTree as ET


def check_stld_closed(xml_data):
    root = ET.fromstring(xml_data)

    closing_date = root.attrib.get("closingDate", "")
    closing_time = root.attrib.get("closingTime", "")

    print(f"{closing_date}, {closing_time}")

    if not closing_date.strip() or not closing_time.strip():
        #print("STLD is not closed yet")
        return None 
    else:
        # print(f"Closing Date: {closing_date}, Closing Time: {closing_time}")
        return "Closed"
    
xml_data = '''<TLD logVersion="1.0-20090415" storeId="1830049" businessDate="20250628" swVersion="NP6.1.0.MR0QR0B22607"
    checkPoint="0" end="true" productionStatus="online" hasMoreContent="false" dataComplete="true"
    openingDate="20250628" openingTime="00:12:40" closingDate="20250629" closingTime="00:13:52"/>'''

status = check_stld_closed(xml_data)
if status:
    print("STLD Status:", status)
else:
    print("STLD is not yet closed.")