# SQLtools
SQLTools is a set of VS Code extensions that connect to, query, and display results from a SQL database manager

I use mariadb so install this first

To install SQLtools follow [this howto](https://vscode-sqltools.mteixeira.dev/en/home)

- Open VS Code
- Click the Extensions view (in the left bar), then search for @tag:sqltools-driver. This lists all the drivers available for SQLTools.
- Install the driver for your database. This also installs the core SQLTools extension
- Click the SQLTools icon (in the left bar)
- Create a connection to your database. To do this, hover over CONNECTIONS in the SQLTools pane. Click the “Add New Connection” icon and choose the driver and enter the connection parameters.

You can then open and query it from within VS Code.

### Tips on useage:
- To change which database you are connected to, go to Connections > Right click on your connection > Edit connection > Database: fill in your database name here.
    Then any future commands you 'Run on Active Connection' will default to using the correct database