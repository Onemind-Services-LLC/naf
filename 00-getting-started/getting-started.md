### Please refer to the table below for your upcoming lab exercises.
| Device name  | Device Group |      IP       | username | password | network_os |
|--------------|--------------|---------------|----------|----------|------------|
| nexus-site1  |      ny      | 172.16.14.210 |   admin  | admin    |   nxos     |
| vmx1-site1   |      ny      | 172.16.14.211 |   root   | Juniper  |   junos    |
| pa-site1     |      ny      | 172.16.14.212 |   admin  | Test12345|   panos    |
| pa-site2     |      sf      | 172.16.14.213 |   admin  | Test12345|   panos    |
| arista1-site2|      sf      | 172.16.14.214 |   admin  | password |   eos      |
| vyos1-site1  |      sf      | 172.16.14.215 |   vyos   | vyos     |   vyos     |
| vyos2-site2  |      sf      | 172.16.14.216 |   vyos   | vyos     |   vyos     |

| Device name  |              |      IP       | username | password |            |
|--------------|--------------|---------------|----------|----------|------------|
| dev_server   |              | 172.16.14.200 |   cml    |   cml    |            |
| runner       |              | 172.16.14.201 |   cml    |   cml    |            |
| gitlab UI    |              | 172.16.14.202 | ansible  | cisco!23 |            |
| ansible tower|              | 172.16.14.203 |   admin  | ansible  |            |

## Please refer to the lab topology below for your upcoming lab exercises.

![alt text](assets\image-20.png)

# Instructions for setting up VSCODE
To complete all the steps, follow these instructions:

1. Log in to the RDP server using the details provided in the table.  

2. Open VS Code in the RDP environment.  
   ![alt text](assets\image.png)

3. Navigate to the Extensions view and search for "remote-ssh".  
   ![alt text](assets\image-2.png)

4. Click on "Install" to install the Remote - SSH extension.  
   ![alt text](assets\image-3.png)

5. Now, you'll see the Remote Explorer icon.  
   ![alt text](assets\image-4.png)

6. Click on it and then click on the settings icon (to open the SSH config file).  
   ![alt text](assets\image-5.png)

7. Open the SSH configuration file (usually located at C:\User\user1\\.ssh\config on my machine).  
   ![alt text](assets\image-6.png)

8. Paste the following content into your config file. Replace "172.16.14.200" with your Dev server IP and "*cml*" with your username.  
    ```
    Host Dev_server
      HostName 172.16.14.200
      User cml
    ```
   It should look like the image below.

   ![alt text](assets\image-18.png)

9. Click on "Refresh" to update the SSH server list.  
   ![alt text](assets\image-15.png)

10. If everything is correct, you should see "Dev_server" in the SSH server list.  
    ![alt text](assets\image-16.png)

11. Click on "Connect in Current Window".  
    ![alt text](assets\image-17.png)

12. Select "Linux", click "Yes", and then enter the password from the details table.
    ![alt text](assets\image-14.png)  
    ![alt text](assets\image-11.png)

13. In the menu, click on "Terminal" and then "New Terminal".  
    ![alt text](assets\image-12.png)

14. Now you'll see a new terminal window like the one in the image below.
    ![alt text](assets\image-13.png)

15. Click on settings  
    ![alt text](assets\02863b5c-adc8-4cbb-a5ac-25c9ddab5161.png)

16. Change auto save settings from off to "onFocusChange" which will enable autofile save
    ![alt text](assets\960527bc-55a3-4f49-a5fa-4050e119b459.png)


# Instructions for setting up VSCODE using ZeroTier
1. Connect to ZeroTier client based on the platform you are running

- On macOS and Windows, find the ZeroTier app in your menu bar. Launch the ZeroTier One app bundle if it's not already running. Click the ⏁ icon on your menu bar and select 'Join New Network'. 

![alt text](assets\image-19.png)

- Type or paste in your network ID and hit 'Join Network'

- From the Command Line

```text
zerotier-cli join ################

with ############### being the 16-digit network ID of the network you wish to join.
```
2. Once ZeroTier is connected, follow instructions from above, they all remain same
