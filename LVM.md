#How to shrink root and increase swap space:

scan for logical volumes
`lvs`

activate volumegroups
`vgchange -ay`

reduce root logical volume TO 50GB
`lvreduce --resizefs -L 50G /dev/mapper/volumegroupname-root`


reduce root logical volume BY 5GB
`lvreduce --resizefs -L -5G /dev/mapper/volumegroupname-root`
WARNING: DO NOT RUN THIS COMMAND WITHOUT RESIZEFS
    the old way of doing this was in two steps, this new way is in one step

increase size of swap logical volume
`lvextend -l 100%FREE /dev/mapper/volumegroupname-swap_1`
alternatively you can specify a size by which you would like the logical volume to be grown

format swap logical volume to be entirely swap space
`mkswap /dev/mapper/volumegroupname-swap_1`

create new logical volumes
`lvcreate -L 100M -n golinux_vol vol_grp`
`lvcreate --size 100M --name golinux_vol vol_grp`
`lvcreate -l 100%FREE --name golinux_vol vol_grp`
