from twisted.internet import reactor
from fake_switches.switch_configuration import SwitchConfiguration, Port
from fake_switches.transports.ssh_service import SwitchSshService
from fake_switches.dell.dell_core import DellSwitchCore

class CustomSwitchConfiguration(SwitchConfiguration):
    def __init__(self, *args, **kwargs):
        super(CustomSwitchConfiguration, self).__init__(objects_overrides={"Port": CustomPort}, *args, **kwargs)


class CustomPort(Port):
    def __init__(self, name):
        self._access_vlan = None

        super(CustomPort, self).__init__(name)

    @property
    def access_vlan(self):
        return self._access_vlan

    @access_vlan.setter
    def access_vlan(self, value):
        if self._access_vlan != value:
            self._access_vlan = value
            print("This could add vlan to eth0")


if __name__ == '__main__':
    ssh_service = SwitchSshService(
        ip="127.0.0.1",
        port=11001,
        switch_core=DellSwitchCore(CustomSwitchConfiguration("127.0.0.1", 
                                                             "NEXT-TEST", 
                                                             ports=[
                                                                 CustomPort("Eth1/1"),
                                                                 CustomPort("Eth1/2"),
                                                                 CustomPort("Eth1/3"),
                                                                 CustomPort("Eth1/4"),
                                                                 CustomPort("Eth1/5"),
                                                                 CustomPort("Eth1/6"),
                                                                 CustomPort("Eth1/7"),
                                                                 CustomPort("Eth1/8"),
                                                                 CustomPort("Eth1/9"),
                                                                 CustomPort("Eth1/10"),
                                                                 CustomPort("Eth1/11"),
                                                                 CustomPort("Eth1/12"),
                                                                 CustomPort("Eth1/13"),
                                                                 CustomPort("Eth1/14"),
                                                                 CustomPort("Eth1/15"),
                                                                 CustomPort("Eth1/16"),
                                                                 CustomPort("Eth1/17"),
                                                                 CustomPort("Eth1/18"),
                                                                 CustomPort("Eth1/19"),
                                                                 CustomPort("Eth1/20"),
                                                                 CustomPort("Eth1/21"),
                                                                 CustomPort("Eth1/22"),
                                                                 CustomPort("Eth1/23"),
                                                                 CustomPort("Eth1/24"),
                                                                 CustomPort("Eth1/25"),
                                                                 CustomPort("Eth1/26"),
                                                                 CustomPort("Eth1/27"),
                                                                 CustomPort("Eth1/28"),
                                                                 CustomPort("Eth1/29"),
                                                                 CustomPort("Eth1/30"),
                                                                 CustomPort("Eth1/31"),
                                                                 CustomPort("Eth1/32"),
                                                                 CustomPort("mgmt0"),
                                                                 CustomPort("Lo0"),
                                                             ])))
    ssh_service.hook_to_reactor(reactor)
    reactor.run()