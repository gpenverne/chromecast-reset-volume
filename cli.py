#!/usr/bin/python3

from volume import Volume
import sys

volumeManagement = Volume(sys.argv[1] if len(sys.argv) > 1 else 'default')
volumeManagement.apply()
