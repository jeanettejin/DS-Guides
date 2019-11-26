
# Creating a Sudo User

If you are using your work instance, chances are you need to create your own sudo user.
Think about sharing your computer with a family. You might have a user for your mom, dad
sister, brother, and yourself, and you can all store your files in a separate place. Having multiple
users is really just for organization, so you can think about this in the same way. You need
to be a sudo user because you need to execute commands as root user. 

Below you will see me create a sudo user for account name `jeanettejin`

Assuming that you have already [ssh-ed into your instance](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2_ssh.md)

1. Become root user
    ```bash 
    ubuntu@ip-172-31-30-30:~$ sudo su root
    root@ip-172-31-30-30:/home/ubuntu#
    ```

2. Now create a sudo user that identifies you by executing  
(replace "username" with your username):

    ```bash
    adduser jeanettejin
    ```
      
3. Respond to Prompts
    ```bash
    root@ip-172-31-30-30:/home/ubuntu# adduser jeanettejin
    Adding user `jeanettejin' ...
    Adding new group `jeanettejin' (1006) ...
    Adding new user `jeanettejin' (1006) with group 'jeanettejin' ...
    Creating home directory `/home/jeanettejin' ...
    Copying files from `/etc/skel' ...
    Enter new UNIX password: **type password**
    Retype new UNIX password: **same password**
    passwd: password updated successfully
    Changing the user information for username
    Enter the new value, or press ENTER for the default
        Full Name []: [Enter]
        Room Number []:  [Enter]
        Work Phone []: [Enter]
        Home Phone []: [Enter]
        Other []: [Enter]
    Is the information correct? [Y/n] Y
    root@ip-172-31-30-30:/home/ubuntu#
    
   ```

    * If you accidently just copy and pasted that whole thing and you don't want your user to be my name
    you can do 
        ```bash
        userdel jeanettejin
        ```
      
4. Now add the user to the sudo group 

   ```bash
   usermod -aG sudo jeanettejin
   ```
   
5. Switch to the newly created user

   ```bash
   sudo su jeanettejin 
   ```
   
6. Check that all is well

     ```bash
      whoami
      > jeanettejin
    ```