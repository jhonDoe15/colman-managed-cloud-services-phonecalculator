
# Backend

set the following environment variables:
```
PGDATABASE = 'yourdbname'

PGUSER = 'yourdbloginuser'

PGPASSWORD = 'yourdbloginpassword'

PGHOST = 'yourdbaddress'
```
these variables will be picked up by the application and help it connect to the provided database

load the data from the 'initial-data-to-load-folder' in the .sql file

install the necessary dependencies with `pip install -r back/requirements.txt`

run the flask application with `flask run`


application verified with Python3.10



# Client

install dependencies with `cd client && npm i`

option to build and run in webserver with `npm run build`, place the build results in `/usr/share/nginx/html/` 
replace the native nginx.conf file in `/etc/nginx/` with the one in the client folder