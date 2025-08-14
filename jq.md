# `jq`

### A powerful commandline tool for manipulting JSON files

#### Example
To modify the phone_number value of the first element in the sims array for each object inside the devices array using jq, you can use the following command:

``` bash 
jq '.devices[] |= (.sims[0].phone_number = "+123456789")' input.json > output.json
```