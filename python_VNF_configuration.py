root@ubuntu:/home/ubuntu/AutomationScripts/PythonScripts# cat python_flavor.py
#################REVISION HISTORY##############
#Version    ReleaseDate         Description
#1.0         30/03/2015            Initial Release
###############################################

import sys
import re
import os

import xml.etree.ElementTree as ET
from xml.dom.minidom import parse
import xml.dom.minidom
import lxml.etree
from novaclient.v1_1 import client as nova_client
#partnername=sys.argv[1]
print ("Length", len(sys.argv))

print("partnername", partnername)

#ten = os.getenv('OS_TENANT_ID')
#print ten

'''tenant_name= sys.argv[1]'''
#tenant_name="admin"
'''username= sys.argv[1]'''
'''password=partnername+"_123"'''
#username="admin"
#password="905865cf54e8322888ebcde23a0e0d1f47c0f356"

username=partnername #'admin'
password=partnername+"_123" #'905865cf54e8322888ebcde23a0e0d1f47c0f356'
tenant_name=partnername #   'admin'
auth_url=os.getenv('OS_AUTH_URL')
newTenantid=os.getenv('OS_TENANT_ID')

#username='sample'
#password='sample_123'
#tenant_name='sample'
#auth_url='https://10.17.10.50:5000/v2.0'

'''PROVIDING CREDENTIALS FOR NOVA CLIENT '''
novaclient = nova_client.Client(auth_url=auth_url,
                              username=username,
                              api_key=password,
                              project_id=tenant_name,
                              insecure=True)

filevar = sys.argv[2]
print("filevar", filevar)

#newTenantid = "c96444f26ae94453b5e22693664848ea"
#filevar = sys.argv[2]
xmlpath = lxml.etree.parse(filevar)
count = int(xmlpath.xpath('count(//vdus)'))
tree = ET.parse(filevar)
root = tree.getroot()


cpulist = []
memlist = []
storagelist = []
flavorSpec = 0

#this function checks if extra specs are required


def extraSpec(vdusflavor):
    flavorSpec = 0
    hugePageFlag = 0
    pageSize = "small"
    print  "extra spec called"
    cpu = vdusflavor.find('cpu/num_cpu').text
    hugepage = vdusflavor.find('memory/HugePagesNeeded').text
    cpucnt = int(cpu)
    cpucnt = cpucnt + 1
    print cpucnt
    for numa in vdusflavor.findall('cpu'):
       print numa.tag
       for numcpu in range(1,cpucnt):
          print numa[numcpu].text
          if numa[numcpu].text == "core":
             flavorSpec = 1
             print "brea",flavorSpec
             break
    if hugepage == 'yes':
       hugePageFlag = 1
       print "yes hugepage selected is yes"
#       pageSize = vdusflavor.find('memory/page_size').text
#       if pageSize == None:
#          pageSzie = 'small'
    return (flavorSpec,hugePageFlag,pageSize)

c = range(count)

def flav1(cpulist,memlist,storagelist,c):
    print "eneterd  flavor1 name";
    for cpu1,mem1,store1,counter,vdusflavor in zip(cpulist,memlist,storagelist,c,root.findall('vdus')):
        try:
    #       partnername = vdusflavor.find('vnfname').text
            print "vdus =",counter," ",vdusflavor.find('cpu/num_cpu').text
            print "partner name ",partnername
            flavor = vdusflavor.find('flavor')
            if flavor.text == "create":
                print "flavor tag found wiith create"
                flavortag = vdusflavor.find('flavor')
                print "fine here"
                vdusflavor.remove(flavortag)
                print "fine here"
                ff(cpu1,mem1,store1,counter,partnername,vdusflavor)
        except:
            print "exception in creating",sys.exc_info()[0]

def create_new_Flavor(cpu1,mem1,store1,partnername,fcnt,vdusflavor):
    print "cpu1 ",cpu1,"mem1",mem1,"store1",store1,"partnername",partnername
    flavo = novaclient.flavors.create(str(partnername)+'v'+str(fcnt),int(mem1),int(cpu1),int(store1),'auto',0,0,1.0,False)#name,ramvcpus,disk,flavorid,
#    novaclient.flavor_access.add_tenant_access(flavo.id,admintenant_id)
    novaclient.flavor_access.add_tenant_access(flavo.id,newTenantid)
    print "name given to new flavor ",str(partnername)+'v'+str(fcnt)
    flavorName = str(partnername)+'v'+str(fcnt)
    print "making call to extraSpec from try block after creating favlor"
    flavorSpec,hugePageFlag,pageSize = extraSpec(vdusflavor)
    print "the flavor spec in except block ",flavorSpec
    if flavorSpec:
        #flavor_name=novaclient.flavors.find(ram=int(mem1),disk=int(store1),vcpus=int(cpu1))
        print "this flavr spec is set to dedicated",flavorSpec
        novaclient.flavors.find(name=flavorName).set_keys({"hw:cpu_policy":"dedicated"})

    if hugePageFlag:
        print "inside the huge flavor stuff", flavorName
        novaclient.flavors.find(name=flavorName).set_keys({"hw:mem_page_size":pageSize})
#    pdb.set_trace()
#    novaclient.flavor_access.add_tenant_access(flavo.id,newTenantid)
    #pdb.set_trace()
    strcv = str(partnername)+'v'+str(fcnt)
    print strcv
    flavortagcreate = ET.SubElement(vdusflavor,'flavor')
    print "...1"
    flavortagcreate.text = strcv
    flavortag = ET.ElementTree(root)
    flavortag.write(filevar)
    print "...2"
    #    namesf = flavor.text
    print "written flavor name ",strcv

def ff(cpu1,mem1,store1,counter,partnername,vdusflavor):
    flvlist = novaclient.flavors.list();
    fcnt = 0
    print "inside ff now the partner name is ",partnername," look for ",partnername+'*'
    for flist in flvlist:
        f = re.match(str(partnername)+'v*',flist.name)
        if f:
            print "match found so increment"
            fcnt = fcnt + 1
    print "the iterat",fcnt
    print "name given to new flavor before create",str(partnername)+'v'+str(fcnt)
    try:
        #pdb.set_trace()
        #flavor_name=novaclient.flavors.find(ram=int(mem1),disk=int(store1),vcpus=int(cpu1))
        create_new_Flavor(cpu1,mem1,store1,partnername,fcnt,vdusflavor)
    except:
        '''NEW FLAVOR CREATION'''
        print "inside except"
        print "exception in creating",sys.exc_info()[0]


for elem in root.findall('vdus'):
#    for flavor in elem.findall('flavor'):
#        elem.remove(flavor)
    #artnername = elem.find('vnfname').text
    cpu = elem.find('cpu/num_cpu').text
    cpuint = int(cpu)
    mem = elem.find('memory/min-RAM-Required').text
    store = elem.find('storage/block/boot-size-gb').text
    #print "one at a time ",store
    cpulist.append(cpu)
    memlist.append(mem)
    storagelist.append(store)

flav1(cpulist,memlist,storagelist,c)








