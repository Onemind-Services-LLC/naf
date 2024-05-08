# Exercise-3 Exploring Remote Repositories with GitHub/GitLab

In this lab exercise, you will learn how to clone a remote repository, create a new branch, make changes, commit them, and push them back to the remote repository.

## Cloning the Remote Repository

1. Copy the clone URL of the remote repository: `git@gitlab.com:test1430118/git-nw-automation.git`.

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/2c2f89bf-1888-4195-bc8f-d169b2c6f607)

2. Execute the following command in your terminal:
   ```bash
   git clone git@gitlab.com:test1430118/git-nw-automation.git
   ```

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/ed4c39a0-ca77-4020-8b8e-702cba099013)

3. Change directory to the cloned repository:
   ```bash
   cd git-nw-automation/
   ```

## Creating a New Branch

1. By default, you've cloned the default branch for the repository. Check the name of the default branch:
   ```bash
   git branch
   ```

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/6f465864-e575-4d66-8a2b-38f57b4cec4a)

2. To create a new branch in your local repository, use:
   ```bash
   git checkout -b example-tutorial-branch
   ```

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/d9039e1c-be31-49a1-90b0-39a159ff49d3)


## Making Changes

1. Change directory to the working directory.
   ```bash
   cd git-nw-automation/
   ```
2. Create a new file in the working directory using the following command:
   ```bash
   touch lab.txt
   ```
3. Check the status of your repository:
   ```bash
   git status
   ```

   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/5f4b0653-4aeb-47a1-8fcc-b4397896d20c)


## Adding Changes to Staging Area

To add files to the staging area for the next commit, use:
   ```bash
   git add lab.txt
   ```

## Committing Changes

Commit your changes with a meaningful message using:
   ```bash
   git commit -m "First commit"
   ```
   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/7fc3897c-f8a0-4883-bac3-bbb5db549a30)

## Viewing Commit History

To view the commit history, you can use:
   ```bash
   git log
   ```
   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/58264582-489c-4b4a-9d5b-fe08416419c7)


## Pushing Changes to Remote Repository

After making changes and committing locally, push them to the remote repository using:
   ```bash
   git push origin example-tutorial-branch
   ```
   ![image](https://github.com/Onemind-Services-LLC/naf/assets/132569101/625e1efc-84b6-4250-af23-2aeb0606bee3)

This concludes the lab exercise. You have successfully cloned a repository, created a new branch, made changes, committed them, and pushed them back to the remote repository.
