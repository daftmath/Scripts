__author__ = 'daftmath@gmail.com'
import os
import os.path
import re

# Python script to walk through all xml files in a directory
# and extract the content from a user selected xml element and write
# it into a text file.

# Input: A python raw string which is the full path to the directory of xml
# files and a string containing the regular expression which matches the
# desired element content

# Output: A text file of the content which the regular expression
# extracted from the xml files, where each line is an element's
# content

# Example Usage:
# path = r'C:\Users\cb12041\Desktop\Back up\all_XML'
# reg_ex = '<Units>(.+)</Units>'
# directory_xml_rip(path, reg_ex)


####################################################################
# Set the path containing xml files for all the plant services
path = r'C:\Users\cb12041\Desktop\Back up\all_XML'
reg_ex = '<Units>(.+)</Units>'
####################################################################

# walking through xml files and using regex to grab units
def directory_xml_rip(path, reg_ex):
    content = []
    for root, _, files in os.walk(path):
        for f in files:
            xml_file = open(path + '\\' + f, 'r')
            test = xml_file.read()
            store = re.findall(reg_ex, test)
            content.extend(store)

    # Removes duplicate items from list
    units = list(set(content))

    # Write units to a text file
    txt_file = open('Content.txt', 'w')
    for item in units:
        txt_file.write("%s\n" % item)

directory_xml_rip(path, reg_ex)
