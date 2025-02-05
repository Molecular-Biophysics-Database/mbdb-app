# files

## Metadata extraction

This merely configures the extractors for the various models. The actual
processors can be found in 
[mbdb-parsing](https://github.com/Molecular-Biophysics-Database/mbdb-parsing).

### synchronous_file_processing.py

This defined the components used to make file processing (extraction) a 
synchronous task rather than an asynchronous task  

### base_extractor.py

This defines the baseclass that should be used in order to configure file 
extractors for all models.

### mst_metadata_extraction.py

This configures the processors of the MST specific extractor. 
The current implementation is that a record will by default get 
the `individual` workflow unless the record belongs to a community
in which case it will get the `community` workflow 
(see [workflow](../../workflows)).

Note that communities currently are not used.