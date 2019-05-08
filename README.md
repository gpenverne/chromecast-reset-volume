# Simply reset volums on chromecasts

## Install
```bash
make install
```

## Configuration
Open the ``config.py`` file, you will see:
```python
VOLUMES = {
    'default': {
       'la télé': 20.00,
       'cuisine': 20.00,
       'étagère': 20.00
    }
}
```

Each object in ``VOLUMES`` corresponds to a preset of several volumes.
Each key in a preset is the name of a chromecast, with volume percent to set as value.
You can put ip address instead of the chromecast name to avoid zeroconf scan time (in few words: it will be faster).

## Usage
```bash
$ make apply
```

## Multi volums groups
```bash
$ python3 reset-volume.py "groupName"
```
