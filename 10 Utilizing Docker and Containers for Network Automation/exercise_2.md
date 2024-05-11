In the last exercise, we set up the Remote SSH plugin to access the development server through the terminal.

### Exercise-1: Building a Docker Image with Dependencies

In the last task, we set up a tool called Remote SSH so we can connect to the development server through the terminal.

Now, we're going to make a special package of software that has everything we need for our development work. 

First, let's make a folder where we'll do this. Type this command:

```sh
cd ~
mkdir docker_build
```

Then, go into that folder:

```sh
cd docker_build
```

![alt text](image-14.png)

Next, let's open a program called VS Code in this folder:

```sh
code .
```

This will open a new window with VS Code.

![alt text](image-15.png)

Now, we're going to make a file called a Dockerfile. This file tells the computer what to put in our special package. 

Make sure the file is named exactly `Dockerfile`.

![alt text](image-17.png)

Inside this file, write down these lines:


```dockerfile
FROM python:3
# Install Ansible and Netmiko
RUN apt update
RUN apt install iputils-ping -y
RUN apt install git -y
RUN pip install rich ansible netmiko pexpect pandas
CMD ["bash"]
```

Your file should look like this:

![alt text](image-23.png)

Now, let's open a new terminal window in VS Code:

![alt text](image-19.png)

In this terminal, type this command to make our special package:

```sh
docker image build -t ansible_lab .
```

![alt text](image-20.png)

Finally, let's check if our package was made correctly. Type this command:

```sh
docker image ls
```

You should see a package named `ansible_lab` in the list.

![alt text](image-21.png)

That's it! We've successfully made our special package using the Dockerfile.