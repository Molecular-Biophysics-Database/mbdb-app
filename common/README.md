# `common` 

This folder contains shared packages - packages that
are used by multiple models/uis in the app.

## usage 
This folder is automatically installed to the running repository
when `./nrp build` or `./nrp develop` is called. You can then import
the modules in your models/uis as follows:

```python
from common import my_module
```
## Overview of the tools 

- `fixtures` - Contains vocabularies and configuration for loading them (`catalogue.yaml`)
- `requests` - Contains MBDB custom requests
- `workflows` - Contains MBDB custom workflows
- `services` - Contains MBDB custom services 
- `fixed_record_values.py` - Tools used for records initialisation.
- `vocabulary_permissions.py` - The custom vocabulary permissions used by MBDB.
- `vocabulary_getters.py` - The online search mechanisms for vocabularies 
- `doi_generation.py` - translation of MBDB metadata to DataCite DOI metadata
