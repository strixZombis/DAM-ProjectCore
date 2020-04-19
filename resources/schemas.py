#!/usr/bin/python
# -*- coding: utf-8 -*-

SchemaUserToken = {
    "type": "object",
    "properties": {
        "token": {"type": "string"},
    },
    "required": ["token"]
}

SchemaRegisterUser = {
    "type": "object",
    "properties": {
        "username": {"type": "string"},
        "password": {"type": "string"},
        "email": {"type": "string"},
        "name": {"type": "string"},
        "surname": {"type": "string"},
        "genere": {"type": "string"},
        "rol": {"type": "string"},
        "position": {"type": "string"},
        "phone": {"type": "string"},
        "photo":{"type": "string"},
        "matchname":{"type": "string"},
        "timeplay":{"type": "string"},
        "prefsmash":{"type": "string"},
        "club":{"type": "string"},
        "license":{"type": "string"}

    },
    "required": ["username", "password", "email","genere","rol"]
}
