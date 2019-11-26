# EC2 For Data Science

1. [SSH into ec2 instance](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#ssh-into-ec2-instance)
2. [Creating a Sudo User](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#creating-a-sudo-user)
3. [Getting to Your User](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#getting-to-your-user)
3. [Making SSH Key for Github](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#making-ssh-key-in-github)
4. [Running Something in Screen Session](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#running-something-in-screen-session)


### Prerequisites
1. Make sure you have a private key file, which I will refer to as `key.pem` and that 
it is here: `.ssh/`. Assuming you are the top level, you can check by running the
following in your teminal:

    ```bash
    ls .ssh/
    ```

2.  Make sure to set the correct permissions on your key file. You can do this 
by running
    ```bash
    chmod 400 .ssh/quizr.pem
    ```


## [SSH into ec2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

This is the basic format:

```bash
ssh -i key.pem user@remote.host
```

For ubuntu it tends to look something like this:

```bash
ssh -i key.pem ubuntu@ec2-198-51-100-1.compute-1.amazonaws.com
```

## Creating a Sudo User

If you are using your work instance, chances are you need to create your own sudo user.
Think about sharing your computer with a family. You might have a user for your mom, dad
sister, brother, and yourself, and you can all store your files in a separate place. Having multiple
users is really just for organization, so you can think about this in the same way. You need
to be a sudo user because you need to execute commands as root user. 

Below you will see me create a sudo user for account name `jeanettejin`

Assuming that you have already [ssh-ed into your instance](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#ssh-into-ec2-instance)

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

## Getting to Your User

Now that you know how to ssh into your instance and you have created a super user, going
forward, this is what the steps look like to get to your user.
1. [SSH into instance](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#ssh-into-ec2-instance)

2. Go to your user account as sudo user

   ```bash
   sudo su jeanettejin
   ```
   
   Your prompt should look something like:
   
   ```bash
   jeanettejin@ip-172-31-30-30:/home/ubuntu$ 
   ```

3. Execute
   ```bash 
    jeanettejin@ip-172-31-30-30:/home/ubuntu$ cd ~/
    jeanettejin@ip-172-31-30-30
   ```
    Now you are in your user account
    
    
## Making SSH Key in Github

[SSH into your instance](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#ssh-into-ec2-instance)
and become [sudo user](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2.md#getting-to-your-user)

1. Generate key
    ```bash
    jeanettejin@ip-172-31-30-30: ssh-keygen -t rsa -b 4096 -C "your github's email"
    ```
2. You will be given a series of prompts where you should just press Enter for all of them

   ```bash
    > Enter a file in which to save the key (/Users/you/.ssh/id_rsa): [Press Enter]
    > Enter passphrase (empty for no passphrase): [Press Enter]
    > Enter same passphrase again: [Press Enter]
   ```
   
3. Run the below command and copy the output to your clipboard

   ```bash
    cat .ssh/id_rsa.pub
   ```
   
4. Add the SSH Key to Github Account
    * Sign into Github and in the upper-right corner of any page, click your profile photo, then click Settings
    * In the user settings sidebar, click SSH and GPG Keys
    * Click New SSH key or Add SSH key 
    * In the "Title" field, add a descriptive label for the new key. For example, 'SimpleBet AWS 1"
    * Click "Add SSH Key" 
    * Copy and paste the output into the box for your SSH key
    * Hit Add SSH key

5. Clone your repo

   ```bash 
   git clone https://github.com/jeanettejin/HelpfulGuides.git
   ```
   
## Running Something in Screen Session

[What is a screen session?](https://linoxide.com/linux-command/15-examples-screen-command-linux-terminal/)
> The screen is a terminal multiplexer. Using this, you can run any number of console-based-applications, interactive command shells, course-based applications, etc. You can use screen to keep running program after you accidentally close the terminal, or even after you log out and later resume right wherever you are.
>
> When screen is called, it creates a single window with a shell in it (or the specified command) and then gets out of your way so that you can use the program as you normally would. Then, at any time, you can create new (full-screen) windows with other programs in them (including more shells), kill the current window, view a list of the active windows, copy text between windows, switch between windows, etc.

>


1. Start a Screen Session

   ```bash 
   screen -S name_of_screen 
   ```
   Note that if you get the following error
   ```bash
    Cannot open your terminal '/dev/pts/0' - please check.
   ```
   Excute
   ```bash
   script /dev/null
   ```

2. Run whatever you want to run

   ```bash
   python3 -m path.to.your.script.py
   ```

3. Detach from screen and allow script to keep running with the shortcut Ctrl + A, D

4. Reopen screen session with

   ```bash 
   screen -r name_of_screen
   ```
   
This is an awesome resource: [screen_cheatsheet](https://gist.github.com/jctosta/af918e1618682638aa82)