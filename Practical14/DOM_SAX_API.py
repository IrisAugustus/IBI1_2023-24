import xml.dom.minidom
import matplotlib.pyplot as plt
from datetime import datetime

#1. Using DOM to manipulate xml file
#record the time before DOM processing the file
start_time_DOM = datetime.now()
#open the file and read its content
file_path='E:/IBI1_2023-24/Practical14/go_obo.xml'
DOMTree = xml.dom.minidom.parse(file_path)
collection = DOMTree.documentElement
namespace = collection.getElementsByTagName('namespace')
#get the text in the required tag 'namespace'
namespace_text = namespace[0].firstChild.nodeValue
total={}
#record the frequency
for name in namespace:
    name_text = name.firstChild.nodeValue
    if name_text not in total:
        total[name_text] = 1
    else:
        total[name_text] += 1
print(total)
#record the time after DOM processing the file
end_time_DOM = datetime.now()
time_taken_DOM = end_time_DOM - start_time_DOM
print(f"Time taken to parse XML using DOM: {time_taken_DOM}")
#make the graph for the outcome
plt.figure(figsize=(10, 6)) 
bars = plt.bar(total.keys(), total.values(), width=0.5, color="pink")
plt.ylabel('frequencies(time)')
plt.title('the number of terms within each ontology')
plt.xticks(rotation=90) 
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
plt.tight_layout()
plt.show()
plt.clf()

#2. Using SAX to manipulate xml file
start_time_SAX = datetime.now()
import xml.sax
#set the parser which is going to read the file
parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
namelist=[]
total={}
#set the handler to be used to process information in the tags
class namespaceHandler (xml.sax.ContentHandler):
    #initialize the values
    def __init__(self):
        self.currentElement = ''
        self.namespace=''
    def startElement(self, tag, attrs):
        self.currentElement = tag

    def characters(self, content):
        if self.currentElement == 'namespace':
            self.namespace += content.strip()

    def endElement(self, tag):
        if tag == 'namespace':
            if self.namespace:  
                namelist.append(self.namespace)  
                self.namespace = ''  

handler = namespaceHandler()
parser.setContentHandler(handler)
parser.parse('E:/IBI1_2023-24/Practical14/go_obo.xml')
end_time_SAX = datetime.now()
time_taken_SAX = end_time_SAX - start_time_SAX
#open the file and read its content
print(f"Time taken to parse XML using SAX: {time_taken_SAX}")

for name in namelist:
    if name not in total:
        total[name] = 1
    else:
        total[name] += 1
print(total)
#make the graph for the outcome
bars = plt.bar(total.keys(), total.values(), width=0.5, color="pink")
plt.ylabel('frequencies(time)')
plt.title('the number of terms within each ontology')
plt.xticks(rotation=90) 
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
plt.tight_layout()
plt.show()
plt.clf()

#Time taken to parse XML using DOM: 0:00:05.501629
#Time taken to parse XML using SAX: 0:00:01.066373
#SAX is quicker to complete its task