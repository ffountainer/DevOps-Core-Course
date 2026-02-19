import pulumi
import pulumi_yandex as yandex
import os

config = pulumi.Config()

zone = config.require("zone")
app_port = config.require_int("appPort")
ssh_user = config.require("sshUser")
ssh_key_path = config.require("sshPublicKeyPath")

with open(os.path.expanduser(ssh_key_path)) as f:
    public_key = f.read().strip()

network = yandex.VpcNetwork("network",
    name="network"
)

subnet = yandex.VpcSubnet("subnet",
    name="subnet1",
    zone=zone,
    network_id=network.id,
    v4_cidr_blocks=["192.168.10.0/24"]
)

security_group = yandex.VpcSecurityGroup("vm-sg",
    network_id=network.id,
    ingress=[
        {
            "protocol": "TCP",
            "description": "SSH",
            "port": 22,
            "v4_cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "TCP",
            "description": "HTTP",
            "port": 80,
            "v4_cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "TCP",
            "description": "App port",
            "port": app_port,
            "v4_cidr_blocks": ["0.0.0.0/0"],
        },
    ],
    egress=[
        {
            "protocol": "ANY",
            "description": "Allow all outgoing traffic",
            "v4_cidr_blocks": ["0.0.0.0/0"],
        }
    ]
)

disk = yandex.ComputeDisk("boot-disk",
    name="boot-disk",
    type="network-hdd",
    zone=zone,
    size=20,
    image_id="fd800c7s2p483i648ifv",
)

vm = yandex.ComputeInstance("vm",
    name="pulumi",
    zone=zone,
    resources={
        "cores": 2,
        "memory": 2,
    },
    boot_disk={
        "disk_id": disk.id,
    },
    network_interfaces=[{
        "subnet_id": subnet.id,
        "nat": True,
        "security_group_ids": [security_group.id],
    }],
    metadata={
        "ssh-keys": f"{ssh_user}:{public_key}",
    }
)

pulumi.export("internal_ip", vm.network_interfaces[0]["ip_address"])
pulumi.export("external_ip", vm.network_interfaces[0]["nat_ip_address"])
