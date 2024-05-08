# Exercise-2 Setting Up GitLab for Remote Repositories

This guide will help you set up GitLab for managing remote repositories, including creating a sample project, configuring Git, and setting up SSH keys for secure authentication.

## Creating a Sample Project

1. Visit [GitLab](https://gitlab.com/users/sign_in) in your browser and sign in with your credentials.

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/38eb5716-3d7e-483a-9258-d73c702ace60)

2. On the left sidebar, select **Create new (+)** and then **New project/repository**.
   
   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/f7871d9d-d521-43c8-96ff-9f3bc840cd10)

3. Enter `git-nw-automation` as the Project name. The project slug (URL) will be generated automatically.

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/1a1e68f8-dcd4-40ff-95e4-bf7494c27948)

4. Ensure **Initialize repository with a README** is selected. You can fill in the other fields as desired.
5. Click **Create project**.

## Configuring Git

### Set User Name and Email

Open a terminal (Git Bash on Windows) and configure your user name and email address. This information is associated with your commits.

```bash
git config --global user.name "Your Name"
git config --global user.email your_email@example.com
```
![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/ff35f020-4d8a-4d2c-a027-cd516471cae7)

### Set Default Editor (Optional)

You can set your preferred text editor for Git. For example, to set Vim as the default editor:

```bash
git config --global core.editor "vi"
```

### View Configuration

To verify your configuration settings, you can use:

```bash
git config --list
```

![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/20a63428-a8fc-4856-a44d-ad1b3bcb069b)


## Setting up SSH Keys for Secure Authentication

### Generate SSH Key

Open a terminal and generate an SSH key pair using the ssh-keygen command. Specify the email you used for your GitLab account.

```bash
ssh-keygen -t rsa -b 4096 -C your_email@example.com
```
![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/9aa9bbb1-9403-4ff4-9b8a-e85af9e0ce62)


### Add SSH Key to GitLab

1. Sign in to GitLab.
2. On the left sidebar, select your avatar.
3. Select **Edit profile**.
4. On the left sidebar, select **SSH Keys**.
5. Select **Add new key**.
6. In the Key box, paste the contents of your public key.
7. In the Title box, type a description, like Work Laptop or Home Workstation.
8. Select **Add key**.

![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/45d5e76c-85dc-40b5-a949-1c2d24cacc34)


By following the instructions outlined here, you've successfully created a sample project, configured Git with your user information and preferences, and set up SSH keys for secure authentication. With these setup steps completed, you're now ready to start collaborating on projects and managing your code effectively using GitLab. 
