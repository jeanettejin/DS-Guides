# AWSCLI

1. [AWSCLI SETUP](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/awscli.md#awscli)
2. [Useful Commands](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/awscli.md#useful-commands)
3. [Version Control](https://github.com/jeanettejin/HelpfulGuides/blob/master/AWS/awscli.md#version-control)

Note: all commands should be executed in the top level of command line

## AWSCLI SETUP

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

## Useful commands:


|  Description | Command  | 
|---|---|
|  listing buckets/contents | aws s3 ls bucketname/ | 
|  copying a file s3 -> local | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) s3://bucket/remote/path/obj.pkl  local/path/obj.pkl |  
|  copying a file local -> s3 | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) local/path/obj.pkl s3://bucket/remote/path/obj.pkl  |
|  copying a directory s3 -> local | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) s3://bucket/remote/path/folder_name/ local/path/folder_name --recursive |  
|  copying a directory local -> s3 | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) local/path/folder_name s3://bucket/remote/path/folder_name/ --recursive |
| removing an individual file | aws s3 [rm](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html) s3://bucket/path/obj.pkl |
| removing all contents within a folder | aws s3 [rm](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html) s3://bucket/path/folder/ --recursive |
| Removing all contents within a folder except files that end with .py | aws s3 [rm](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html) s3://bucket/path/folder/ --recursive --exclude *.py|
|moving an object in s3| aws s3 [mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) s3://bucket/currentpath/obj.pkl s3://bucket/desiredpath/obj.pkl |
|moving a folder in s3| aws s3 [mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) s3://bucket/currentpath/folder/ s3://bucket/desiredpath/folder/ --recursive |



## Version Control

If you have version control turned on and you need to go back to a previous version of a file you can do the following:

1. Get all versions for
    
    ```bash
    aws s3api list-object-versions --bucket bucket_name
    ```
   where `bucket_name` is the bucket that the object is in.
   
   Here is an example of a snippet of the output for `obj.pkl`. Its address is `s3://bucket_name/path/obj.pkl`. If you have a really
   long output, just control+F and use the file's name to find its versioning information.
   
   ```bash
   {
            "ETag": "\"f886c41dbfa8e8169d02a5ab6fcd5fa4\"",
            "Size": 38755540,
            "StorageClass": "STANDARD",
            "Key": "path/obj.pkl",
            "VersionId": "1dherse9Sv2oCMH8ylwaHBuP8XQJ2mSK",
            "IsLatest": true,
            "LastModified": "2019-07-09T19:14:12.000Z",
            "Owner": {
                "DisplayName": "jeanettejin",
                "ID": "e05f1f60f515d0e3289c3a70c6d9299fda7b6346f9c7a9c06caa9a3c344e34b5"
            }
        },
    {
        "ETag": "\"e11b5c6f067f22a80d7edbde2e44d3c0\"",
        "Size": 38843000,
        "StorageClass": "STANDARD",
        "Key": "path/obj.pkl",
        "VersionId": "y_1TE06F4dksnnrVaPllzqFicSos7IRE",
        "IsLatest": false,
        "LastModified": "2019-06-09T19:17:28.000Z",
        "Owner": {
            "DisplayName": "jeanettejin",
            "ID": "e05f1f60f515d0e3289c3a70c6d9299fda7b6346f9c7a9c06caa9a3c344e34b5"
        }
   ```
2. Find the version id for the version you want. In my case it would be 
`y_1TE06F4dksnnrVaPllzqFicSos7IRE`

3. Get object locally
    ```bash
   aws s3api get-object --bucket bucket_name --key path/obj.pkl --version-id y_1TE06F4dksnnrVaPllzqFicSos7IRE obj.pkl 
   ```
