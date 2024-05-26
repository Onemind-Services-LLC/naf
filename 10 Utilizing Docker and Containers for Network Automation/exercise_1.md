In the last exercise, we installed the Remote SSH plugin, allowing us to access the development server via the terminal.

## Exercise: Install Docker on Development Server?

Now, let's install Docker in our development environment, which we'll use in the upcoming exercises. Follow these commands:

1. Remove existing Docker packages:
   ```sh
   for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
   ```
   ![alt text](image.png)

2. Add Docker's official GPG key and update:
   ```sh
   sudo apt-get update
   ```
   ![alt text](image-1.png)

3. Install necessary packages:
   ```sh
   sudo apt-get install ca-certificates curl
   ```
   ![alt text](image-2.png)

4. Set up directory:
   ```sh
   sudo install -m 0755 -d /etc/apt/keyrings
   ```
   ![alt text](image-3.png)

5. Download Docker's GPG key:
   ```sh
   sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
   ```
   ![alt text](image-4.png)

6. Set permissions:
   ```sh
   sudo chmod a+r /etc/apt/keyrings/docker.asc
   ```
   ![alt text](image-5.png)

7. Add Docker repository to Apt sources:
   ```sh
   echo \
     "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
     $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
     sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   ```
   ![alt text](image-6.png)

8. Update repositories:
   ```sh
   sudo apt-get update
   ```
   ![alt text](image-7.png)

9. Install Docker:
   ```sh
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```
   ![alt text](image-8.png)
   ![alt text](image-9.png)

10. Verify Docker installation by running a hello-world container:
    ```sh
    sudo docker run hello-world
    ```
    ![alt text](image-10.png)

11. Run Docker as a non-root user by adding your user to the docker group:
    ```sh
    sudo usermod -aG docker $USER
    ```
    ![alt text](image-11.png)
    ```sh
    newgrp docker
    ```
    ![alt text](image-12.png)

12. Verify that you can run Docker as a non-root user:
    ```sh
    docker run hello-world
    ```
    ![alt text](image-13.png)

13. Reboot the VM:
    ```sh
    cml@cml:~/docker_build$ sudo reboot
    [sudo] password for cml: cml
    ```
14. Wait for a few seconds and reconnect to the same VM again via VSCODE.
