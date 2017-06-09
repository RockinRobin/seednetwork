seednetwork
===========
The Seed Exchange of the Heritage and Landrace Grain Network.

This is a Django site. To make it easier to deploy without changing settings.py, use the following environment variables

```shell
SEEDNETWORK_SECRETKEY
SEEDNETWORK_EMAIL_HOST
SEEDNETWORK_EMAIL_PORT
SEEDNETWORK_EMAIL_HOST_USER
SEEDNETWORK_EMAIL_HOST_PASSWORD
SEEDNETWORK_DEFAULT_FROM_EMAIL
```

The site is set up for ```Debug=False```, but for local development, use

```shell
export SEEDNETWORK_DEBUG=True
```

This site uses [dj_database_url](https://crate.io/packages/dj-database-url/) for DB configuration, so set ```DATABASE_URL``` using its syntax. A sample mysql URL is

```shell
export DATABASE_URL='mysql://user:pwd@host:port/database'
```

Heroku Deploy Instructions
--------------------------
There is some helpful information at the original wiki

https://github.com/hackforwesternmass/seednetwork/wiki/Hosting-on-Heroku

History of the seedbank 
--------------------------------------

This exchange is derived from the Hilltown Seed Saving Network which was created during a hack for Western Massachusetts hackathon. We are grateful for their hard work.

Currently this site is optimized for grains, check out our fork for seeds. In the future we hope to unify the models.
