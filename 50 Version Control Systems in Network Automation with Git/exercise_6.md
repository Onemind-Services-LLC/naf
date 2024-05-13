## Problem Statement: 
### GitLab Integration with Ansible Tower
Let's utilize Ansible Tower to execute all the tasks we completed in the previous exercise and initiate the playbook through Ansible Tower.

## Steps


- first login to ansible tower details of the tower you can found in the first lab.
![alt text](image-35.png)

#### Creation of GitLab Credentials in AAP:

   - Navigate to the "Credentials" section in AAP.

   ![alt text](image-37.png)

   - Click on "Add Credentials" and select "Source control" as the credential type.
   ![alt text](image-36.png)
   - Provide the required GitLab credentials(username and password).
   - Save the credential configuration.
   ![alt text](image-38.png)

  - GitLab credentials are configured within AAP, allowing seamless access to the GitLab repository.


#### Inventory Creation in Ansible Automation Platform (AAP):
- Navigate to the "Inventory" section under Resources.

![alt text](image-39.png)

- Click on "Add" and enter "eve_inventory" as the name and select organization as default.
  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/ca2c021b-f443-45ad-a3fa-566c8fdc53e3)

- Next add a host "vyos1-site2" to the inventory.
  - go to hosts in eve_inventory
  ![alt text](image-40.png)
  - click on add fil the below details
  ```yaml
    ---
    ansible_host: 172.16.14.215
    ansible_network_os: vyos
  ```
  ![alt text](image-41.png)
  - click on save
  - lets add one more host go to hosts again
  
  ![alt text](image-42.png)
  - click on add and fill the below details

- Next add a host "vyos2-site2" to the inventory.
  ```yaml
    ---
    ansible_host: 172.16.14.216
    ansible_network_os: vyos
  ```
  ![alt text](image-43.png)
- click on save and now you can see we have 2 devices in our inventory
![alt text](image-44.png)


#### now lets create creds for these routers that we are going to use in our inventory















































- create a project in gitlab
![alt text](image-33.png)

- open the repo in web ide
![alt text](image-34.png)

































- create the files that we created in last lab (playbook.yaml, ansible.cfg)
  ```bash
  cd backup_configurations
  ```
- Move playbook.yml into backup_configurations

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/1db60960-f284-4c99-abdf-664be472d125)

- Use the command `git add` to add files to the repository.
   ```bash
   git add .
   ```

- Commit the files using the command
   ```bash
   git commit -m "Adding playbook.yaml
   ```
  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/67e0c22c-059b-43a6-b0e7-68be6bb43f53)

- Push changes to the repository

   ```bash
   git push origin master
   ```
   When prompted pass the username and password

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/96065772-806f-46cd-8c39-8a0ce72de6ea)




### 5. Project Creation with GitLab as Source Control:

  - Navigate to the "Projects" section in AAP.
  - Click on "Create Project" and specify config-backup as the name.
  - Choose Git as the source control type and add the source control url and branch
  - Link the project to the previously configured GitLab credentials.
  - Save the project configuration.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/5e8a66eb-3d3c-4f8d-8720-569863530775)

  - A project is created within AAP, utilizing GitLab as the source control system for storing and managing automation scripts.

### 6. Template Creation and Scheduled Execution:

  - Create a template with "router-backup-conf" as the name.
  - Select eve-inventory and backup-config for inventory and the project.
  - Select playbook.yaml as the playbook.
  - Link the previously configured server-creds.
  - Click create template

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/5ae74808-a621-4a74-abbf-b776c7f641e1)

  - Schedule the playbook as shown below.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/23ecf6c9-016f-465a-92bc-261807443db6)

  - An Ansible template is developed within the AAP project, automating lab infrastructure setup and configuration.

### 7. Template Execution:
  - Launch the template from templates section.
    
   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/5a56c379-cb8c-4a39-9806-bb216e50952d)

  - Check the status of the job

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/41438900-88dc-4599-8845-43909182003c)

In this lab, we successfully automated the process of backing up configurations and integrating Ansibke with Git for version control using GitLab.
