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

This ensures that a workflow will be attached to each record is