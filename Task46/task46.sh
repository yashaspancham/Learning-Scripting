#!/bin/bash

json='{"server": {"id": "aws-123", "status": "running", "network": {"ip": "10.0.0.5", "type": "private"}}}'


echo $json | jq -r .server.network.ip