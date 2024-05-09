##  Exercise:
### Problem Statement:

Set up a GitLab repository named `router_configurations`. Each file within this repository should correspond to the hostname of a router, containing the configurations for that specific router. Ensure that the configurations in the repository are synchronized with the actual configurations of the routers.

Implement a GitLab CI pipeline that triggers whenever a user commits changes to any router's configuration file in the GitLab repository. The pipeline should automatically update the configurations on the respective routers to reflect the changes made in the GitLab files.


#### Solution