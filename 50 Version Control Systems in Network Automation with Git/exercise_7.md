## Problem Statement: Automating Lab Infrastructure Setup with Ansible and GitLab Integration

## Steps

1. **Inventory Creation in Ansible Automation Platform (AAP):**
   - Develop a comprehensive inventory within AAP, detailing all lab environment hosts and groups for efficient resource management.

2. **Creation of GitLab Credentials in AAP:**
   - Establish GitLab credentials within AAP to securely access the GitLab repository, enabling version control and collaboration for automation scripts.

3. **Creation of Server Credentials in AAP:**
   - Configure server credentials within AAP to facilitate secure access to lab resources, ensuring seamless execution of automation tasks.

4. **Project Creation with GitLab as Source Control:**
   - Create a dedicated project within AAP, leveraging GitLab as the source control system to store and manage Ansible playbooks and templates.

5. **Template Creation and Scheduled Execution:**
   - Develop an Ansible template within the AAP project, automating lab infrastructure setup and configuration.
   - Schedule the template to run at regular intervals, ensuring routine maintenance and updates every 7 days for optimal performance and reliability.


### Solution
## Steps

### 1. Inventory Creation in Ansible Automation Platform (AAP):
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

### 2. Creation of GitLab Credentials in AAP:

   - Navigate to the "Credentials" section in AAP.
   - Click on "Add Credentials" and select "Source control" as the credential type.
   - Provide the required GitLab credentials(username and password).
   - Save the credential configuration.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/170c6e6c-c28b-4a67-92c2-a0b0e37daede)

   - GitLab credentials are configured within AAP, allowing seamless access to the GitLab repository.

### 3. Creation of Server Credentials in AAP:

  - Navigate to the "Credentials" section in AAP.
  - Click on "Add Credentials" and select "Machine" as the credential type.
  - Provide the necessary server credentials(username and password).
  - Save the credential configuration.
  
  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/d4eea390-c8fd-4409-97d8-a00001cd1a70)

  - Server credentials are configured within AAP, enabling secure access to lab resources during automation tasks.

### 4. Project Creation with GitLab as Source Control:

  - Navigate to the "Projects" section in AAP.
  - Click on "Create Project" and specify config-backup as the name.
  - Choose Git as the source control type and add the source control url and branch
  - Link the project to the previously configured GitLab credentials.
  - Save the project configuration.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/5e8a66eb-3d3c-4f8d-8720-569863530775)

  - A project is created within AAP, utilizing GitLab as the source control system for storing and managing automation scripts.

### 5. Template Creation and Scheduled Execution:

  - Create a template with "router-backup-conf" as the name.
  - Select eve-inventory and backup-config for inventory and the project.
  - Select playbook.yaml as the playbook.
  - Link the previously configured server-creds.
  - Click create template

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/5ae74808-a621-4a74-abbf-b776c7f641e1)

  - Schedule the playbook as shown below.

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/23ecf6c9-016f-465a-92bc-261807443db6)

  - An Ansible template is developed within the AAP project, automating lab infrastructure setup and configuration.

### 6. Template Execution:
  - Launch the template from templates section.
    
   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/5a56c379-cb8c-4a39-9806-bb216e50952d)

  - Check the status of the job

  ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/41438900-88dc-4599-8845-43909182003c)

  
