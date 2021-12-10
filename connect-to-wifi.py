import os

class Finder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        command = "sudo iwlist wlp2s0 scan | grep ESSID"
        result = os.popen(command.format(self.server_name))
        print(type(result))
        result = list(result)

        if "Device or resource busy" in result:
            return None
        else:
            for item in result:
                x = item.strip().split("\n")
                new_list = [s.replace("ESSID:", "") for s in x]
                print("Successfully get ssids{}".format(str(new_list)))

        self.connection()

    def connection(self):
        try:
            os.system("nmcli d wifi connect {} password {}".format(self.server_name,
                                                                            self.password))
        except:
            print(Exception)
            raise
        else:
            return True


if __name__ == "__main__":
    # Server_name is a case insensitive string, and/or regex pattern which demonstrates
    # the name of targeted WIFI device or a unique part of it.
    server_name = "put your ssid here"
    password = "put your pass of ssid here"
    interface_name = "wlp2s0"  # i. e wlp2s0
    F = Finder(server_name=server_name,
               password=password,
               interface=interface_name)
    F.run()
