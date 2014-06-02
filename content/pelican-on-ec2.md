title: Hosting a Pelican blog on EC2
tags: ec2, pelican
summary: Let's experiment with different ways of deploying websites!

This blog is hosted on the totally rad GitHub pages platform, but for my web analytics class, I need to mirror it on a server that I have full access to so that I can play around with server-side logging and all that jazz. I couldn't find any good tutorials about pushing a pelican blog to your own remote server, but some experimentation proved it to be rather simple, so here it is for classmates/posterity. I will assume general familiarity with AWS and `.pem` files, etc.

Launch an Amazon EC2 instance with the default Amazon Linux AMI (micro instance). Most of this can be done from the command line (see some of my previous posts for some examples), but we'll stick with the console GUI. Just follow the red boxes.

![ec2-1]({filename}/images/ec2-1.png)

![ec2-2]({filename}/images/ec2-2.png)

Before you launch it, add an `HTTP` security rule. The port will default to 80. This allows anyone to access the site once the webserver is running.

![ec2-3]({filename}/images/ec2-3.png)

![ec2-4]({filename}/images/ec2-4.png)

Give the instance an elastic IP address by clicking "Elastic IPs" on the console sidebar. Click "Allocate New Address" and then right click the resulting address and click "Associate Address" (the instance field should automatically populate when you click in it). Make note of your elastic IP (mine is `54.201.31.202`).

![ec2-5]({filename}/images/ec2-5.png)

SSH into your new instance, substituting your own IP and `.pem` file of course:

```sh
ssh -i /PATH/TO/*.pem ec2-user@54.201.31.202
```

Once on your server:

```sh
sudo yum update
sudo yum install httpd                          # install webserver
sudo chown -R ec2-user:ec2-user /var/www/html   # chown future location of our website files
sudo service httpd start                        # start webserver
exit
```

Modify these lines in your local `Makefile` (again with your own `.pem` & IP):

```sh
SSH_HOST=54.201.31.202
SSH_USER=ec2-user
SSH_TARGET_DIR=/var/www/html

ssh_upload: publish
	scp -i ~/PATH/TO/*.pem -P $(SSH_PORT) -r $(OUTPUTDIR)/* $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)
```

Now, `make ssh_upload` will act just like `make github` does, except it will push to your EC2 server instead of your `gh-pages` branch. After you do this the first time, you should be able to access your website at the elastic IP address. For example, this website is now (temporarily) accessible at both spencerboucher.com *and* [54.201.31.202](http://54.201.31.202/). The advantage here is that now we have full access to the web server for using logstash and the like.

