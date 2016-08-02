#!/usr/bin/env python3
# coding:utf-8
import string
import random
def vcode_creator(digit):
    vcode = ''
    for i in range(digit):
        vcode += random.choice(string.ascii_uppercase + string.digits)
    return vcode

def create_vcodes(vcLen,vcNum):
    data=''
    count = 1
    for count in range(vcNum):
#       digit=10
        count += 1
        data += 'VerificationCode no.'+str(count)+'  '+vcode_creator(vcLen)+'\n'
    return data
