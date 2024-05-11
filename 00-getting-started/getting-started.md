To complete all the steps, follow these instructions:

1. Log in to the RPD server using the details provided in the table.
2. Open VS Code in the RDP environment.
   ![alt text](image.png)
3. Navigate to the Extensions view and search for "remote-ssh".
   ![alt text](image-2.png)
4. Click on "Install" to install the Remote - SSH extension.
   ![alt text](image-3.png)
5. Now, you'll see the Remote Explorer icon.
   ![alt text](image-4.png)
6. Click on it and then click on the settings icon (to open the SSH config file).
   ![alt text](image-5.png)
7. Open the SSH configuration file (usually located at C:\User\user1\\.ssh\config on my machine).
   ![alt text](image-6.png)
8. Paste the following content into your config file. Replace "172.16.14.200" with your Dev server IP and "*cml*" with your username.
    ```
    Host Dev_server
      HostName 172.16.14.200
      User cml
    ```
   It should look like the image below.
   
   ![alt text](image-18.png)
9. Click on "Refresh" to update the SSH server list.  
   ![alt text](image-15.png)
10. If everything is correct, you should see "Dev_server" in the SSH server list.  
    ![alt text](image-16.png)
11. Click on "Connect in Current Window".  
      ![alt text](image-17.png)
12. Select "Linux", click "Yes", and then enter the password from the details table.
   ![alt text](image-14.png)
    ![alt text](image-11.png)
13. In the menu, click on "Terminal" and then "New Terminal".
    ![alt text](image-12.png)
14. Now you'll see a new terminal window like the one in the image below.
    ![alt text](image-13.png)