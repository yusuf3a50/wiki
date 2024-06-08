### Troubleshooting

There is a [bug in node 18](https://github.com/npm/cli/issues/4163) which seems specific to linux. `yarn install` or `npm install` will return some `ECONNREFUSED` errors and wont download packages over IPv6. As a workaround, temporarily disable IPv6 on your system (IKR!) by following these instructions:

Backup your `sysctl.conf` file before making changes:
`sudo cp /etc/sysctl.conf /etc/sysctl.conf_backup`

Add the following line to `sysctl.conf` file:

`net.ipv6.conf.all.disable_ipv6 = 1` 

To apply the changes immediately, run the following command:
`sudo sysctl -p`