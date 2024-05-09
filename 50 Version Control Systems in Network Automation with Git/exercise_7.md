## Problem Statement: GitLab Integration with Ansible Tower
Automate lab setup by pushing existing Ansible files to GitLab, then execute them from Ansible Tower for streamlined processes and version control.

## Steps

1. **Push existing code into gitlab:**
   - Push the existing Ansible playbook, ansible.cfg, and inventory.ini files to the GitLab repository.

2. **Inventory Creation in Ansible Automation Platform (AAP):**
   - Develop a comprehensive inventory within AAP, detailing all lab environment hosts and groups for efficient resource management.

3. **Creation of GitLab Credentials in AAP:**
   - Establish GitLab credentials within AAP to securely access the GitLab repository, enabling version control and collaboration for automation scripts.

4. **Creation of Server Credentials in AAP:**
   - Configure server credentials within AAP to facilitate secure access to lab resources, ensuring seamless execution of automation tasks.

5. **Project Creation with GitLab as Source Control:**
   - Create a dedicated project within AAP, leveraging GitLab as the source control system to store and manage Ansible playbooks and templates.

6. **Template Creation and Scheduled Execution:**
   - Develop an Ansible template within the AAP project, automating lab infrastructure setup and configuration.
   - Schedule the template to run at regular intervals, ensuring routine maintenance and updates every 7 days for optimal performance and reliability.


### Solution
## Steps

### 1. Push existing code into gitlab:

- Change directory to "backup_configurations".
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


### 2. Inventory Creation in Ansible Automation Platform (AAP):
- Log in to Ansible Automation Platform (AAP) dashboard using credentials

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/7a97eb2e-acbb-455e-8eb5-5bce6e4de33e)

- Navigate to the "Inventory" section under Resources.
- Click on "Add" and enter "eve_inventory" as the name and select organization as default.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/ca2c021b-f443-45ad-a3fa-566c8fdc53e3)

- Under groups add a new group "dc_group" and the extra variables

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/353d5b65-f1b5-4d5f-8b0d-34d0b3190192)

- Next add a host "arista" to the inventory.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/42f2f85f-b5c4-4660-9edb-65d604344b39)

- Add one more host "csr" like below

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/80421cc1-c6aa-41e3-8e96-3e0f1223aa09)

- Save the inventory configuration.

### 3. Creation of GitLab Credentials in AAP:

   - Navigate to the "Credentials" section in AAP.
   - Click on "Add Credentials" and select "Source control" as the credential type.
   - Provide the required GitLab credentials(username and password).
   - Save the credential configuration.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/170c6e6c-c28b-4a67-92c2-a0b0e37daede)

   - GitLab credentials are configured within AAP, allowing seamless access to the GitLab repository.

### 4. Creation of Server Credentials in AAP:

  - Navigate to the "Credentials" section in AAP.
  - Click on "Add Credentials" and select "Machine" as the credential type.
  - Provide the necessary server credentials(username and password).
  - Save the credential configuration.
  
  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/d4eea390-c8fd-4409-97d8-a00001cd1a70)

  - Server credentials are configured within AAP, enabling secure access to lab resources during automation tasks.

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
