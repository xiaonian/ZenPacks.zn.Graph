
import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

import json
from Products.ZenModel.ZentinelPortal import ZentinelPortal

def getCPUJSON(self, ip):
    """
    This is a webservice test!
    """
    device = self.dmd.Devices.findDevice(ip)
    dps = device.getRRDDataPoints()
    cpu_dp = ''
    for dp in dps:
        if dp.hasAlias('cpu__pct'):
            cpu_dp = dp   
            break
    if cpu_dp:
        for alias in cpu_dp.aliases():
            if 'cpu__pct' == alias.id:
                break
        rpn = alias.formula
        val = device.getRRDValue(dsname=cpu_dp.id, extraRpn=rpn)
        result = {"used":val}
    else:
        result = {"used":0}
    return json.dumps(result)
    
ZentinelPortal.getCPUJSON = getCPUJSON
