# Regular Expressions:

## In VSCode:
### Remove data values from a JSON object
#### Strings:
Search for : "string_value" and then replace it with : "something else"

search for:`:\s"([^"]*)"`

repace with: `: "string"`

#### Numbers
Search for ': number_value' and then replace it with ': 0'

search for:`:\s(\d+)`

repace with: `: 0`