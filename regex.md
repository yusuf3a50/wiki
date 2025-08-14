# Regular Expressions:

## In VSCode:
### Remove data values from a JSON object
#### Strings:
Search for : "string_value" and then replace it with : "something else"

search for:`:\s"([^"]*)"`

replace with: `: "string"`

#### Numbers
Search for ': number_value' and then replace it with ': 0'

search for:`:\s(\d+)`

replace with: `: 0`

#### Lists
eg.

``` json
"ownership": [
    "7fb11147-d519-512c-adeb-58166de441ab",
    "7fb11147-d519-512c-adeb-58166de441ab"
  ],
```

Search for ": ["string_value" and then replace it with ": ["something else"
Search for ", "string_value" and then replace it with ", "something else"

##### step 1
search for:`:\s\[\n\s*["]([^"]*)["],\n`

replace with: `: [\n  "string",\n `

##### step 2
search for:`["],\n\s*["]([^"]*)["]\n`

replace with: `",\n "string"\n`

##### step 3
reformat the document to correct any indentation issues caused by any whitespace removal

##### breakdown of regex used:
- `\s` single whitespace
- `\s*` whitespace for any number of characters
- `\n` newline character
- `["']` anything that is a double quote OR a single quote
- `[^"]` anything that is NOT a double quote
- `([^"]*)` anything that is NOT a double quote for ANY number of characters
- `\[` a square bracket (because this needs escaping)
- `\d{3,}` 3 or more digits
- `[0-9a-fA-F]{16}` 16 hexadecimal digits
- `|` OR
- `(?=":\s"[^-]")(?=":\s"[^1-9]*")` AND (needs elaborating on!)