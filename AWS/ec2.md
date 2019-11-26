# EC2 For Data Science

This guide will show you how to do a few things. If you are running into an error
and you can't figure out what is wrong, stop looking for the quick fix answer and 
patiently read and figure out what is going on.
1. [SSH into ec2 instance](https://github.com/jeanettejin/HelpfulGuides/AWS/ec2#SSH into ec2 instance)
2. [Creating a Sudo User]
3. [Making SSH Key for Github]
4. [Running Something in Screen Session]


### Prerequisites
* Make sure you have a private key file, which I will refer to as `key.pem` and that 
it is here: `.ssh/`. Assuming you are the top level, you can check by running the
following in your teminal:

```bash
ls .ssh/
```

* Make sure that you have the correct permissions on your key file. You can do this 
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

