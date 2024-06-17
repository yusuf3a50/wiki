#/etc/crypttab
# <target name>	<source device> <key file> <options>
#an example of what your target name might be would be:
#sudo cryptsetup luksOpen /dev/sda3 target_name

encrypted_volume_name UUID=12345678-abcd-abcd-abcd-123456789012 none luks,discard

#there must be a new line at the end of this file!!!!

