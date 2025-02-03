# workflows 

## Creating roles

Roles are created and assigned by invoking

```bash
source .venv/bin/activate
invenio roles create <role>
invenio roles add <user-email-address> <role>
```
The following roles are currently being used with the MBDB (see
[release.sh](../release.sh)):
- reviewer
- editor
- administrator

Definition of which permission these roles have is completely determined  
workflows, the above commands only create and add people to the roles.

## custom_generators.py

The custom (permission) generators used by the MBDB can be found here.

## individual_workflow.py
This is currently the only workflow that is being used by the MBDB.
Hence, all records generated are so-called individual records.

`IndividualWorkflowPermissions` sets the permissions for individual records, 
i.e., records that are that does not belong to a community.

`IndividualWorkflowRequests` defines which request applies to individual records
and the state of the record before, during, and after a request has been made.

## community_workflow.py
This workflow is currently not being used by records and requires reviewing
before it should be used! 

`CommunityWorkflowPermissions` sets the permissions for community records.

`CommunityWorkflowRequests` defines which request applies to community records
and the state of the record before, during, and after a request has been made.