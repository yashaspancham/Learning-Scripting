#!/bin/bash

last_pwd_change=$(chage -l developer | grep "Last password change" | cut -d: -f2)

echo "$last_pwd_change"