# Scripts
##Various Python Scripts


###directory_xml_rip

Python script to walk through all xml files in a directory
and extract the content from a user selected xml element and writes
it into a text file.

Input: A python raw string which is the full path to the directory of xml
files and a string containing the regular expression which matches the
desired element content

Output: A text file of the content which the regular expression
extracted from the xml files, where each line is an element's
content

Example Usage:    
path = r'C:\Users\cb12041\Desktop\Back up\all_XML'    
reg_ex = '\<Units>(.+)\</Units>'    
directory_xml_rip(path, reg_ex)    

