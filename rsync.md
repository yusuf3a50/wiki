#### upload some files to a server over SSH:

`rsync -e "ssh -p PORTNUMBER -i ~/.ssh/ssh_key" -avr /source/file/location/ user@www.example.com:~/target/file/location`

#### useful flags:

archive - keep source and target files identical, even the permissions
`-a`

verbose
`-v`

recursive
`-r`

update the files in the target location
`-u`

display progress of file transfer
`--progress`

for large file file transfers, this allows you to kill the transfer and then continue it later where you left of, saving you some time and bandwidth:
`--partial`