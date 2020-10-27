#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:26:49 2020

@author: adityanambiar
"""
import json

class Customer:
    
    # constructor for Customer object
    def __init__(self, name, ID, DOB, email, phone, status, address, zipcode):
        self.name = name
        self.ID = ID
        self.DOB = DOB
        self.email = email
        self.phone = phone
        self.status = status
        self.address = address
        self.zipcode = zipcode
    
    # function to return JSON object
    def returnJSON(self):
        variables = {
            "Name" : self.name,
            "Customer ID" : self.ID,
            "Date of Birth" : self.DOB,
            "Email" : self.email,
            "Phone Number" : self.phone,
            "Status" : self.status,
            "Address" : self.address,
            "Zipcode" : self.zipcode
            }
        
        json_return = json.dumps(variables)
        return json_return

