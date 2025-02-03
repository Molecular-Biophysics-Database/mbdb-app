# requests 

Custom MBDB request should be placed here. Currently, two custom requests are 
used: 

 - publish accepted draft
 - submit draft 

## registering requests

In order for the request to be used in a workflow, it needs to be registered 
in [pyproject.toml](../../pyproject.toml) inside the section:
```toml
[project.entry-points."invenio_requests.types"]
```

## Request implementations 

### publish_accepted_draft.py

Defines the publish draft request. 

Customization of the publish request is done to allow customising the 
terms that the user agrees to when publishing the record. 

It also removes the (oarepo default) option to add a version name as this currently 
is not implemented, and validation rules for the name also has not been 
specified.

### submit_draft.py

Defines the submit request.

It serves only to initiate validation the record, and as trigger that 
can be used to change the state of the record (see [workflows](../workflows))
