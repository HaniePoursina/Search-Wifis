# Search and Connect to WiFis

this repo includes some diffrent python files to search and connect to wifis around.

## connect-to-wifi.py file:

This file contains a class with two function run and connection, the command used to search for wifis is:

```bash
sudo iwlist wlp2s0 scan | grep ESSID
```

the command to connect to specefic wifi is:
```bash
nmcli d wifi connect <Name_of_WIFI> password <Pass_of_WIFI>
```















## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
