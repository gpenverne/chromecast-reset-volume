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
       '123.123.123.123': 20.00,
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

## Specific preset
```bash
$ cli.py "groupName"
```


## Server
You can launch your presets using an api endpoint (perfect for ifttt and google assistant for example ;)

### Launch
```bash
$ server.py
```
### Config
Open the ``config.py`` file, you will see a ``SERVER_PORT``, you can customize as you want.

### Usage
Simply go to ``http://your-server-ip:your-port/default`` (where defaut is the name of a preset).
