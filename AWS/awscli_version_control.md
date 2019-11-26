# Version Control

If you have version control turned on and you need to go back to a previous version of a file you can do the following:

1. Get all version info for all object in bucket
    
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
