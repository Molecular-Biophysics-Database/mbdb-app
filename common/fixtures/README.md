# fixtures

Fixture items that should be loaded whenever a new instance of MBDB is created 
should be placed here. Currently, this only includes vocabularies, so
fixtures is synonymous with vocabularies  

## Configuring the loader (catalogue.yaml)

In order for the fixture to be picked up by `invenio oarepo fixtures load`,
it needs to be registered in `catalogue.yaml`, and there needs
to be at least one example item to load.

## Structure

Vocabularies are concepts defined by invenio which has been extended by oarepo. 

The basic structure of a vocabulary is given below: 

```yaml
id: !!str
title: !!map
  en: !!str
props: !!map
  !!str: !!str
      ...
```
Note that `id` and `title` are mandatory, but `props` (and its children)
is optional.

If a different structure is needed (e.g. non-string data types) this 
needs to be defined and configured as custom fields, see
[Using Custom Fields](#using-custom-fields) below how to accomplish this.

## Configuration

All configuration refers to elements in [invenio.cfg](../../invenio.cfg).

### Basic (mandatory for all vocabularies )

Inside the configuration dict `INVENIO_VOCABULARY_TYPE_METADATE`,
a minimum configuration is type followed by a name and 
description. 

Example basic configuration:
```python
INVENIO_VOCABULARY_TYPE_METADATE = {
    "chemicals": {  # vocabulary of chemicals
        "name": {"en": "Chemicals"},
        "description": {"en": "Based on the Pubchem database"},
    }
}
```

### Enable external searching

Enabling external searching requires two things:
 1. Create an `AuthorityProvider` (see [vocabulary getters](../README.md#vocabulary_getterspy))  
 2. Specify the `"authority"` in the vocabulary config inside
    `INVENIO_VOCABULARY_TYPE_METADATE` 

Example basic configuration + external searching:
```python

from common.vocabulary_getters import (
    PubChemService,
)

INVENIO_VOCABULARY_TYPE_METADATE = {
    "chemicals": {  # vocabulary of chemicals
        "name": {"en": "Chemicals"},
        "description": {"en": "Based on the Pubchem database"},
        "authority": PubChemService,
    }
}
```
### Using custom fields

Using another the structure than the basic vocabulary structure can be 
accomplished using custom fields. 

It's important to note that introducing custom fields means introducing them in
 **all** vocabularies, so use them sparingly and avoid introducing name conflicts! 
Furthermore, custom fields cannot be made mandatory from the perspective of 
validation as that would imply all vocabularies would need to contain them.  

Example basic configuration + external searching + custom fields:
```python

from common.vocabulary_getters import (
    PubChemService,
)

INVENIO_VOCABULARY_TYPE_METADATE = {
    "chemicals": {  # vocabulary of chemicals
        "name": {"en": "Chemicals"},
        "description": {"en": "Based on the Pubchem database"},
        "authority": PubChemService,
    }
}

from oarepo_ui.services.custom_fields import ComplexCF
from invenio_records_resources.services.custom_fields.number import DoubleCF
from invenio_records_resources.services.custom_fields.text import KeywordCF

VOCABULARIES_CF = [
    ComplexCF("molecular_weight", [DoubleCF("value"), KeywordCF("unit")]),
    KeywordCF("chemical_formula"),
    KeywordCF("additional_identifiers", multiple=True),
]
```
