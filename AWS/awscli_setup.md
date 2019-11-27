
# AWSCLI SETUP

You will need your access key id and your secret key for this section

1. [Install the AWS CLI Using Bundled Installer (from your top level)](https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html)  
  
      * If MacOS
      
    ```bash
    curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
    unzip awscli-bundle.zip
    sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
    ```
    
      * If Ubuntu (AWS ec2)
        
    ```bash
    sudo apt-get update
    sudo apt-get install awscli
    ```

2. Configure

    ```bash
   aws configure
    ```
    
    You will be prompted
    
    ```bash
    aws configure
    AWS Access Key ID [None]: YOUR ACCESS KEY HERE
    AWS Secret Access Key [None]: YOUR SECRET ACCESS KEY HERE
    Default region name [None]: [Enter]
    Default output format [None]: [Enter]
    ```
3. See that it all worked with

    ```bash
    aws s3 ls 
    ```