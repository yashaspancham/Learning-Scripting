#!/bin/bash

scp -i delete_later_ec2.pem \
 -o ConnectTimeout=20 \
 -o BatchMode=yes \
 -o StrictHostKeyChecking=no \
 -o UserKnownHostsFile=/dev/null \
 backup.tar.gz ec2-user@3.108.53.182:/tmp/