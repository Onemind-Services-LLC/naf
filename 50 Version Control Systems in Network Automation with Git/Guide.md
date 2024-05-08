# Git Installation and Setup

## Installing Git on Linux:

1. **Update Package Lists:** Open a terminal and update the package lists of your Linux distribution using:
   ```bash
   sudo apt update
   ```


2. **Install Git:** Use the package manager to install Git. For Ubuntu/Debian based systems, you can do this with:
   ```bash
   sudo apt install git
   ```
   For other distributions, the command might be different (e.g., yum for CentOS, dnf for Fedora).

3. **Verify Installation:** After installation, verify that Git has been installed successfully by running:
   ```bash
   git --version
   ```
   This should display the installed Git version.

## Installing Git on Windows:

1. **Download Git Installer:** Go to the [official Git website](https://git-scm.com/) and download the Git installer for Windows.

2. **Run Installer:** Once the download is complete, run the installer and follow the installation wizard steps.
   - Choose installation options as per your preference (e.g., adjusting PATH environment, choosing editor, etc.).
   - Use default settings if you're unsure.

3. **Complete Installation:** Once the installation is complete, Git should be ready to use.

## Configuring Git:

1. **Set User Name and Email:** Open a terminal (Git Bash on Windows) and configure your user name and email address. This information is associated with your commits.
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your_email@example.com"
   ```

2. **Set Default Editor (Optional):** You can set your preferred text editor for Git. For example, to set Vim as the default editor:
   ```bash
   git config --global core.editor "vim"
   ```

3. **View Configuration:** To verify your configuration settings, you can use:
   ```bash
   git config --list
   ```

## Setting up SSH keys for secure authentication:

1. **Generate SSH Key:** Open a terminal and generate an SSH key pair using the `ssh-keygen` command. Specify the email you used for your Git account.
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

2. **Follow Prompts:** You'll be prompted to choose a location for the SSH key pair and to optionally set a passphrase.

3. **Add SSH Key to Git Account:** Copy the contents of the public key (`~/.ssh/id_rsa.pub`) and add it to your Git hosting service (e.g., GitHub, GitLab) in the SSH keys settings.

These steps should get you set up with Git, both on Linux and Windows, and configure it for secure authentication using SSH keys.


# Lab 2: Git Fundamentals and Collaborative Development

## Git Fundamentals:

### Initializing a Git repository:

To initialize a Git repository in your project directory, use the following command:
```bash
git init
```

### Adding files to the staging area:

To add files to the staging area for the next commit, use:
```bash
git add <file1> <file2> ...
```

### Committing changes to the repository:

Commit your changes with a meaningful message using:
```bash
git commit -m "Your commit message"
```

### Viewing commit history:

To view the commit history, you can use:
```bash
git log
```

## Collaborative Development with Git:

### Cloning a remote repository:

To clone a remote repository to your local machine, use:
```bash
git clone <remote_repository_URL>
```

### Pushing changes to a remote repository:

After making changes and committing locally, push them to the remote repository using:
```bash
git push origin master
```
(Replace `origin` with your remote's name, and `master` with the branch you are pushing to)

### Pulling changes from a remote repository:

To fetch and merge changes from the remote repository to your local repository, use:
```bash
git pull origin master
```
(Replace `origin` with your remote's name, and `master` with the branch you are pulling from)

### Resolving merge conflicts:

If there are merge conflicts when pulling changes, Git will indicate them. Manually resolve conflicts in the affected files, then add and commit the changes to complete the merge.

# Lab 3: Exploring Remote Repositories with GitHub/GitLab

## Creating a repository on GitHub/GitLab:

1. **GitHub:**
   - Log in to your GitHub account.
   - Click on the "+" icon in the top-right corner and select "New repository".
   - Fill in the repository name, description, and other details.
   - Choose visibility options (public/private).
   - Click on "Create repository".

2. **GitLab:**
   - Log in to your GitLab account.
   - Navigate to the dashboard and click on "New project".
   - Fill in the project name, description, and other details.
   - Choose visibility options (public/private/internal).
   - Click on "Create project".

## Cloning a remote repository locally:

To clone a remote repository to your local machine, use the following command:
```bash
git clone <repository_URL>
```

## Forking a repository:

1. **GitHub:**
   - Navigate to the repository you want to fork.
   - Click on the "Fork" button in the top-right corner.
   - Choose where to fork the repository (your account or an organization).

2. **GitLab:**
   - Navigate to the repository you want to fork.
   - Click on the "Fork" button on the top-right corner.
   - Choose where to fork the repository (your account or a group).

## Creating and managing branches:

### Creating a new branch:

To create a new branch in your local repository, use:
```bash
git checkout -b <branch_name>
```

### Switching branches:

To switch between branches, use:
```bash
git checkout <branch_name>
```

### Listing branches:

To list all branches in your repository, use:
```bash
git branch
```

### Deleting branches:

To delete a branch, use:
```bash
git branch -d <branch_name>
```
(Use `-D` instead of `-d` to force delete a branch)

## Lab 4 & 5:
# Router Configuration Management with Git

This guide outlines how to manage router configurations using Git for version control and automation.

## 1. Starting a Git Repository:

- Choose a Git hosting platform like GitHub or GitLab.
- Create a new repository specifically for router setups.
- Ensure appropriate access controls to limit visibility and changes.

## 2. Saving Router Backups:

- Determine backup methods such as SSH or FTP for routers.
- Implement scripts or tools to automate backup procedures.
- Store backups securely in designated folders on your computer.

## 3. Starting Git:

- Navigate to the folder containing your router backups.
- Initialize a new Git repository with `git init`.
- Add router files to the repository staging area with `git add .`.
- Commit the changes with a descriptive message using `git commit -m "First router settings"`.

## 4. Connecting to a Remote Repository:

- Specify the remote repository URL with `git remote add origin <remote_repository_URL>`.
- Push your local changes to the remote repository with `git push -u origin master`.

## 5. Updating Configurations Automatically:

- Utilize configuration management tools like Ansible or Puppet for automated router setup changes.
- Configure these tools to fetch router setups from Git repositories and apply them to routers.
- Implement regular checks for changes and updates to keep configurations up to date.

## 6. Undoing Changes:

- Use Git to revert to a previous setup if issues arise.
- Review commit history with `git log` to identify the desired setup.
- Reset router configurations to a specific commit using `git reset --hard <commit_SHA>`.

## 7. Keeping Baseline Setups:

- Maintain a separate folder in Git for baseline setups.
- Document changes made over time to monitor network evolution.
- Ensure clear labeling to distinguish between different setups easily.

By following these steps, you can effectively manage and track router configurations using Git, ensuring consistency, automation, and version control in your network infrastructure.

