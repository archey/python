#!/usr/bin/env python

from passlib.hosts import host_context

#generate new salt and hash password
hash = host_context.crypt("secrets")

print hash


