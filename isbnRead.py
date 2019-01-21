# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="117.50.43.176", port=22, username="haishu", password="Hlw..2018")
