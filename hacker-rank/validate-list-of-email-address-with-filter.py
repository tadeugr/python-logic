#!/usr/bin/env python3

# validate-list-of-email-address-with-filter
# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import sys
import os
import math
import pprint
pp = pprint.PrettyPrinter(indent=4)
import re

def fun(s):
    s = s.rstrip()
    result = True

    split = s.split("@")
    if len(split) != 2: return False
    
    username = split[0]
    if not username: return False
    domain = split[1]

    host = domain.split(".")
    if len(host) != 2: return False

    website = host[0]
    extension = host[1]

    if len(extension) > 3: return False

    aux = username
    find = re.findall(r'\W+', aux)
    aux = ''.join(find)
    find = re.findall(r'[^-]', aux)
    aux = ''.join(find)
    if aux != '': return False

    aux = website
    find = re.findall(r'\D+', aux)
    aux = ''.join(find)
    find = re.findall(r'[^a-z]', aux)
    aux = ''.join(find)
    find = re.findall(r'[^A-Z]', aux)
    aux = ''.join(find)
    if aux != '': return False

    aux = extension
    find = re.findall(r'\D+', aux)
    aux = ''.join(find)
    find = re.findall(r'[^a-z]', aux)
    aux = ''.join(find)
    find = re.findall(r'[^A-Z]', aux)
    aux = ''.join(find)
    if aux != '': return False
    
    return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)