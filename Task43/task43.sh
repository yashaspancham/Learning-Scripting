#!/bin/bash


ssh -i delete_later_ec2.pem \
   -o ConnectTimeout=10 \
   -o BatchMode=yes \
    -o StrictHostKeyChecking=no \
   -o UserKnownHostsFile=/dev/null \
   ec2-user@3.108.53.182 "tar -xf /tmp/backup.tar.gz -C /tmp/"

if [[ $? -eq 0 ]]; then
    echo "Extraction successful."
fi
