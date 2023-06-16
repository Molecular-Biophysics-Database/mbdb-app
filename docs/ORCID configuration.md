# How to set up ORCID authentication?

### Reference material

Invenio already prepared a code support for the authentication via ORCID - [ORCID Authentication client](https://github.com/inveniosoftware/invenio-oauthclient/blob/master/invenio_oauthclient/contrib/orcid). It also contains a brief steps how to make ORCID authentication work (the first docstring). This is a main reference material for this guide.

### ORCID account

1. We need to get an ORCID's client ID and a client secret. In order to do that, we need to [create an account](https://orcid.org/register). After the successful registration, head to developers tools (under your profile name).

2. Fill out the form and register your application. Redirect URI should be in the form `CFG_SITE_URL/oauth/authorized/orcid/` e.g. when your server runs locally on the port 5000 then the redirect URI is `https://localhost:5000/oauth/authorized/orcid/`.

3. Copy the generated client ID and secret.

> Friendly reminder: Do not share this with anyone.

### Invenio configuration

In the `sites/mdbd-site/invenio.cfg`

1. Import the ORCID client

```py
from invenio_oauthclient.contrib import orcid
```

2. Add ORCID's external provider (the `OAUTHCLIENT_REMOTE_APPS` variable is already present in the configuration file)

```py
OAUTHCLIENT_REMOTE_APPS = {
    "orcid": orcid.REMOTE_APP
}
```

3. Add the credentials and fill them with your client ID and secret from the previous step.

```py
ORCID_APP_CREDENTIALS = dict(
   consumer_key="Client ID",
   consumer_secret="Client secret",
)
```