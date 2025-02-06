# files

## Metadata extraction

This merely configures the extractors for the various models. The actual
processors can be found in
[mbdb-parsing](https://github.com/Molecular-Biophysics-Database/mbdb-parsing).

### synchronous_file_processing.py

This defined the components used to make file processing (extraction) a
synchronous task rather than an asynchronous task.

### base_extractor.py

This defines the baseclass that should be used in order to configure file
extractors for all models.

### mst_metadata_extraction.py

This configures the processors of the MST specific extractor.