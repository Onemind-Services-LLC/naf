##  Exercise:
### Problem Statement:

runner Configurations

#### Solution

- open Cmd 
![alt text](image.png)
- login to runner
    ```
    ssh -l cml 172.16.14.201
    ```
    ![alt text](image-2.png)

- run the below command to install runner
    ![alt text](image-4.png)


- install the runner using below command
    ```sh
    sudo apt-get install gitlab-runner
    ```
    ![alt text](image-5.png)

- now our runner machine is ready now we have to configure it for that go to gitlab and login using user name and password that is provide in the table for exercise one.
    ![alt text](image-6.png)
- click on admin area
    ![alt text](image-7.png)

- click on runner
    ![alt text](image-8.png)

- you can find the runner details here
 ![alt text](image-9.png)

- now go to terminal there we have already ssh the runner machine and run the below command
    ```sh
    gitlab-runner register --name automation_lab --url "http://172.16.14.202/" --registration-token C-rzEaUyaTQFGVtDJPoP --executor shell --non-interactive

    ```
    ![alt text](image-10.png)

- we can see the list of configured runner using below command
    ```sh
    gitlab-runner list
    ```
    ![alt text](image-11.png)

- when u regresh the runner configuration page in gitlab you can see the list of runner that we configured just now
![alt text](image-12.png)

- you can see the runner is shared and locked lets change it as of now for that click on edit
![alt text](image-13.png)

- make sure your configuration should like below  image
![alt text](image-14.png)

- now we can see the *runner currently online is 0* 
![alt text](image-15.png)

- let's start the runner for that go to terminal there runner is already ssh and run the below command

```sh
# Install and run as service
sudo gitlab-runner install --user=gitlab-runner --working-directory=/home/gitlab-runner
sudo gitlab-runner restart
gitlab-runner run
```
make sure u should run `gitlab-runner run` as non root user.

![alt text](image-18.png)
![alt text](image-17.png)
![alt text](image-19.png)

- lets create a git repo with anyname that u want i am using `cicd_automation_lab` as repo name
![alt text](image-20.png)
- click on web ide
![alt text](image-21.png)
- create folder and file structure like below
![alt text](image-23.png)
