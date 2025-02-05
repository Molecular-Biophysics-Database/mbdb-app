# `common`

This folder contains shared packages - packages that
are used by multiple models/uis in the app.

## usage
This folder is automatically installed to the running repository
when `./nrp build` or `./nrp develop` is called. You can then import
the modules found in common into your models/uis as follows:

```python
from common import my_module
```

## Folder Overview

- `alembic` - Contains tools for database migrations 
- `fixtures` - Contains vocabularies and the configuration to load them
- `requests` - Contains MBDB custom requests
- `workflows` - Contains MBDB custom workflows (requests and states associated with records)
- `services` - Contains MBDB custom services 

More information is available inside each folder 

##  Modules overview 

### `fixed_record_values.py`

Tools and configurations that are being called to set the fixed values of the
metadata when a record is initialised.

### `vocabulary_permissions.py`

Setting the permission of each vocabulary, where it needs to be explicitly defined 
who can create/add new vocabulary items.  

### `vocabulary_getters.py`

The tools that enables online searching of certain vocabularies.
Note that these all relies on 
[oarepo-vocabularies](https://github.com/oarepo/oarepo-vocabularies)
where more information can be found.

#### affiliations 

Search tool: `RORService`<br> 
API: ROR REST API v1<br>
API Documentation: https://ror.readme.io/docs/rest-api<br>
Rate limit: 2000 per 5 minutes 

#### chemicals

Search tool: `PubChemService`<br> 
API: PubChem PUG REST<br>
API Documentation: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest<br>
Rate limit: 5 per second<br>
Notes:
  - This API is slow
  - returns 404 when no chemicals are found that matches the query 
  - Documentation is poor 

#### grants 

Search tool: `OpenAireService`<br>
API: OpenAIRE projects REST API<br>
API Documentation: https://graph.openaire.eu/docs/apis/search-api/projects<br>
Rate limit: 60 per hour 

#### organisms 

Search tool: `NCBIService`<br>
API: NCBI REST API v2<br>
API Documentation: https://www.ncbi.nlm.nih.gov/datasets/docs/v2/api/rest-api/<br>
Rate limit: 3 per second 

## `doi_generation.py` 

The tools that enables translation of MBDB metadata to DataCite DOI metadata 
was.

The core class is `DataCiteMappingMBDB` which is being called by oarepo-doi
whenever doi related operations are needed.

All the functions outside `DataCiteMappingMBDB` serve as converters from
the MBDB data model to DataCite fields.

## `release.sh`

This script is used for initialisation of the Invenio/Oarepo instance, 
including creation of roles within MBDB.