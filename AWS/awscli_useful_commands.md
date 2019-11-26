# Useful commands:


|  Description | Command  | 
|---|---|
|  listing buckets/contents | aws s3 ls bucketname/ | 
|  copying a file s3 -> local | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) s3://bucket/remote/path/obj.pkl  local/path/obj.pkl |  
|  copying a file local -> s3 | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) local/path/obj.pkl s3://bucket/remote/path/obj.pkl  |
|  copying a directory s3 -> local | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) s3://bucket/remote/path/folder_name/ local/path/folder_name --recursive |  
|  copying a directory local -> s3 | aws s3 [cp](https://docs.aws.amazon.com/cli/latest/reference/s3/cp.html) local/path/folder_name s3://bucket/remote/path/folder_name/ --recursive |
| removing an individual file | aws s3 [rm](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html) s3://bucket/path/obj.pkl |
| removing all contents within a folder | aws s3 [rm](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html) s3://bucket/path/folder/ --recursive |
| removing all contents within a folder except files that end with .py | aws s3 [rm](https://docs.aws.amazon.com/cli/latest/reference/s3/rm.html) s3://bucket/path/folder/ --recursive --exclude *.py|
|moving an object in s3| aws s3 [mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) s3://bucket/currentpath/obj.pkl s3://bucket/desiredpath/obj.pkl |
|moving a folder in s3| aws s3 [mv](https://docs.aws.amazon.com/cli/latest/reference/s3/mv.html) s3://bucket/currentpath/folder/ s3://bucket/desiredpath/folder/ --recursive |

