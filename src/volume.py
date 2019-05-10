#!/usr/bin/python3

import config
import pychromecast
import socket

def isValidIp(ipAddress):
    try:
        socket.inet_aton(ipAddress)
        return True
    except:
        return False

class Volume:
    def __init__(self, groupName):
        try:
            self.devices = config.VOLUMES[groupName]
        except:
            raise ValueError('Couldn\'t not find group volumes with name: ' + groupName)

    def apply(self):
        for chromecastIpOrName, volumePercent in self.devices.items():
            if isValidIp(chromecastIpOrName):
                self.setVolumeOnIpAddress(chromecastIpOrName, volumePercent)

        chromecasts = pychromecast.get_chromecasts()
        print(self.devices)
        for cc in chromecasts:
            if not cc.device.friendly_name in self.devices:
                print('Ignoring '+cc.device.friendly_name)
                continue
            print('Set '+cc.device.friendly_name+' at volume '+str(self.devices[cc.device.friendly_name])+' on ip '+cc.host)
            cc.wait()
            cc.set_volume(self.devices[cc.device.friendly_name])

    def setVolumeOnIpAddress(self, chromecastIpOrName, volumePercent):
        device = pychromecast.Chromecast(host=chromecastIpOrName)
        print('Set '+chromecastIpOrName+' at volume '+str(volumePercent))
        device.wait()
        device.set_volume(volumePercent)
