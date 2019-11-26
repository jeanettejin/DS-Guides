
# Getting to Your User

Now that you know how to ssh into your instance and you have created a super user, going
forward, this is what the steps look like to get to your user.
1. [SSH into instance](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2_ssh.md)

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
    