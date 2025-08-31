# Firefox security improvements

[This article](https://andrewmarder.net/firefox/) is a good general guide

### Search engine reverts to google after firefox update

lots of articles about how to revert BACK to google search as default, but not the other way round!

### about:config

[This site](https://support.mozilla.org/en-US/questions/1226063) suggests adding
`browser.search.reset.enabled:` and setting it to `false`

### Managing cookies: auto-delete some, auto-keep some and use containerisation

To configure Cookie AutoDelete to keep some cookies in some Containers and delete others, follow these instructions:

1. Be sure that Containers are enabled and Cookie AutoDelete extension is installed

2. **Open Firefox**: Launch your Firefox browser.

3. **Access Cookie AutoDelete Preferences**:
   - Click on the menu icon in the toolbar.
   - Click on 'Add-ons and themes'
   - On 'Cookie Autodelete' open options by selecting the three dots
   - Select 'Preferences'

4. **Navigate to the 'List of Expressions' Section**:
   - In the settings menu, look for the section labeled "List of Expressions" or similar.

5. **Add a New Expression**:
   - In the text field box you can add an expression (eg. `*.google.com`)
   - You can use regular expressions here if you like. [See documentation about this field here](https://github.com/Cookie-AutoDelete/Cookie-AutoDelete/wiki/Documentation#enter-expression
   )
   - Under `Current Container Selected:` select the container you wish to modify (eg. `Work`)
   - Press the required button: `+Greylist` or `+Whitelist` depending on the required treatment of the cookies with domain matching your expression 
   - In the "Domain Expression" field, you can further modify the domain expressions here

6. **Repeat as Necessary**:
   - If you want to add more domains to keep/delete cookies for, repeat the process for each domain.

7. **Test Your Configuration**: 
   - Open a website in the `firefox-container-8 (Work)` container and check if the cookies are retained after closing the tab.


