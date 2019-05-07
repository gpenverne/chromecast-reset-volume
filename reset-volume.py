#!/usr/bin/python3

import config
import sys
import pychromecast

class Volume:
    def __init__(self, groupName):
        try:
            self.devices = config.VOLUMES[groupName]
        except:
            raise ValueError('Couldn\'t not find group volumes with name: ' + groupName)

    def apply(self):
        chromecasts = pychromecast.get_chromecasts()
        for cc in chromecasts:
            if not hasattr(self.devices, cc.device.friendly_name):
                print('Ignoring '+cc.device.friendly_name)
                continue
            print('Set '+cc.device.friendly_name+' at volume '+self.devices[cc.device.friendly_name])
            cc.set_volume(self.devices[cc.device.friendly_name])

volumeManagement = Volume(sys.argv[1] if len(sys.argv) > 2 else 'default')
volumeManagement.apply()
