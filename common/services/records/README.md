# records


## permissions.py

This defines that base permission of all records (and dafts) within the MBDB.

## search_options.py

This extends the basic search functionality with the advanced search parameter
interpretation.

Note that the frontend is not incorporated yet as it requires
React 18, which is incompatible with the current invenio requirements (React 16).

## params

Where the parameter interpreter of the advanced search can be found.

## service.py

This ensures that a workflow will be attached to each record.

The current implementation is that a record will by default get
the `individual` workflow unless the record belongs to a community
in which case it will get the `community` workflow
(see [workflow](../../workflows)).

Note that communities currently are not used.