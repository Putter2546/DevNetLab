from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.56.105",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )

'''
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability) 
'''

# netconf_reply = m.get_config(source="running")
# print(netconf_reply)

# ---------------- filter + get_config() ----------------------------
# netconf_filter = """
# <filter>
#     <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
# </filter>
# """
# netconf_reply = m.get_config(source="running", filter=netconf_filter)

# ---------------- hostname + edit_config() ----------------------------
# netconf_hostname = """
# <config>
#   <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
#      <hostname>WISHMELUCKY</hostname>
#   </native>
# </config>
# """
# netconf_reply = m.edit_config(target="running", config=netconf_hostname)


# ---------------- addloopback + edit_config() ----------------------------
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>My first NETCONF loopback</description>
    <ip>
     <address>
      <primary>
       <address>10.1.1.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)


print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


