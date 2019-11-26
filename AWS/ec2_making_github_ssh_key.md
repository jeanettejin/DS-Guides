    
# Making SSH Key in Github

[SSH into your instance](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2_ssh.md)
and become [sudo user](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/ec2_getting_to_user.md)

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
   