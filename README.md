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

## Usage
```bash
$ make apply
```

## Multi volums groups
```bash
$ python3 reset-volume.py "groupName"
```
