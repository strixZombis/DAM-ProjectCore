#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging.config

import falcon

import messages
import middlewares
from resources import account_resources, common_resources, user_resources, favour_resources
from settings import configure_logging

# LOGGING
mylogger = logging.getLogger(__name__)
configure_logging()


# DEFAULT 404
# noinspection PyUnusedLocal
def handle_404(req, resp):
    resp.media = messages.resource_not_found
    resp.status = falcon.HTTP_404


# FALCON
app = application = falcon.API(
    middleware=[
        middlewares.DBSessionManager(),
        middlewares.Falconi18n()
    ]
)
application.add_route("/", common_resources.ResourceHome())

application.add_route("/account/profile", account_resources.ResourceAccountUserProfile())
application.add_route("/account/create_token", account_resources.ResourceCreateUserToken())
application.add_route("/account/delete_token", account_resources.ResourceDeleteUserToken())

application.add_route("/users/register", user_resources.ResourceRegisterUser())
application.add_route("/users/show/{username}", user_resources.ResourceGetUserProfile())

# Favours
application.add_route("/favours", favour_resources.ResourceGetFavours())

# TODO: Falta afegir que la petició requereixi token.

# TODO: Jo definiria un ENUM de categories, tindrieum molt més control i podreu fer filtres.

# TODO: PER PENSAR -> Quan voleu la llista definiu quins parametres necessiteu, normalment no caldràn tots...
# TODO: PER PENSAR ->  /favours/show/{id} -> aqui si retornar tota la informació del favour

# TODO: Els favors no haurien de tenir component geografic -> LAT/LON o millor poble/ciutat i provincia,
#  que pasa si m'interesa un favor però visc a Lleida, hem de treballar més el model de dades.



application.add_sink(handle_404, "")
