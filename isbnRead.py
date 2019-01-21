# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.0.99", port=22, username="root", password="rootroot")