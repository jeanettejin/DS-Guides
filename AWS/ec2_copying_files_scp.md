# Copying Files With scp

* Local to Remote:
    
    ```bash
  scp -i key.pem /Users/jeanettejin/local_path/obj.pkl ubuntu@ec2-3-95-59-156.compute-1.amazonaws.com:/home/jeanettejin/remote_path/
  
    ```
  
* Remote to Local:
    ```bash
    scp -i key.pem ubuntu@ec2-3-95-59-156.compute-1.amazonaws.com:/home/jeanettejin/remote_path/obj.pkl /Users/jeanettejin/local_path/
    ```