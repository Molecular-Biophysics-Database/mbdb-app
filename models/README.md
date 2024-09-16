# models 

This contains the data model definitions and settings.

## Model files 

### `<model-name>.yaml`

This contains the model specific setting, dependencies, and defines endpoints.

### `<model-name>-metadata.yaml`

The top level model definition. This is a generated file, and it shouldn't be 
changed manually. Instead, changes to this file should be made by following the 
steps outlined in [mbdb-model]. 

### `<model-name>-definitions.yaml`

This file contains the method specific definitions (the metadata item `method_specific_parameteres`),

This is a generated file, and it shouldn't be changed manually. Instead, changes to this file should be made by following the 
steps outlined in [mbdb-model]. 

## Special files 

### `settings.yaml` 
Settings used by all models including searching and relations

### `files.yaml`

The metadata items of uploaded files (found under the key `"metadata"`) 
 
This is a generated file, and it shouldn't be changed manually. 
Instead, changes to this file should be made by following the 
steps outlined in [mbdb-model].

### `general_parameters-definitions.yaml`

Contains the metadata item `"general_parameters"`, which is shared among all models,
and definitions used by in more than one method specific model.

This is a generated file, and it shouldn't be changed manually. 
Instead, changes to this file should be made by following the 
steps outlined in [mbdb-model].

[mbdb-model]: https://github.com/Molecular-Biophysics-Database/mbdb-app