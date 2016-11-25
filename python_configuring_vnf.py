#################REVISION HISTORY##############
#Version    ReleaseDate         Description
#1.0         30/03/2015            Initial Release
###############################################

#!/usr/bin/python
from keystoneclient.v2_0 import client as ksclient
from novaclient.v1_1 import client as nova_client
import sys
import os
import time

def get_nova_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    d['insecure'] = True
    return d
def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    d['insecure'] = True
    return d

#creds = get_keystone_creds()
#keystone = ksclient.Client(**creds)
#print( "auth",keystone.auth_token)
creds = get_nova_creds()
nova = nova_client.Client(**creds)
print(nova.servers.list())

print ("Building Instance")

#if not nova.keypairs.findall(name="mykey"):
#    with open(os.path.expanduser('~/.ssh/id_rsa.pub')) as fpubkey:
#        nova.keypairs.create(name="mykey", public_key=fpubkey.read())
image = nova.images.find(name="Cirros")
flavor = nova.flavors.find(name="cirros-flavor")
network = nova.networks.find(label="PrivateN/wF5")
nics = network.id
print(nics)

instance = nova.servers.create(name="Automation_test_F5", image=image, flavor=flavor,nics = [{'net-id':network.id}])

# Poll at 5 second intervals, until the status is no longer 'BUILD'

status = instance.status
while status == "BUILD":
    time.sleep(5)

    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status
print("status: %s" % status)
