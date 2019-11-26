## Prerequisites
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


# [SSH into ec2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

This is the basic format:

```bash
ssh -i key.pem user@remote.host
```

For ubuntu it tends to look something like this:

```bash
ssh -i key.pem ubuntu@ec2-198-51-100-1.compute-1.amazonaws.com
```