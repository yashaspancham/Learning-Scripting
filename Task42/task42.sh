#!/bin/bash

scp -i key.pem backup.tar.gz ec2-user@EC2_IP:/home/ec2-user/
