#!/usr/bin/python
# -*- coding: utf-8 -*-

from builtins import super

import falcon
from sqlalchemy.orm.exc import NoResultFound
import messages

from db.models import Favour
from resources.base_resources import DAMCoreResource


class ResourceGetFavours(DAMCoreResource):
    def on_get(self, req, resp, *args, **kwargs):
        super(ResourceGetFavours, self).on_get(req, resp, *args, **kwargs)

        response_favours = list()

        aux_favours = self.db_session.query(Favour)

        for current_favour in aux_favours:
            # D'aquesta manera podeu també filtrar els atributs a cada item de la llista
            # response_favours.append(current_favour.to_json_model(id="id", name="name"))

            # D'aquesta manera retornarà tot el vostre model json
            response_favours.append(current_favour.json_model)

        resp.media = response_favours
        resp.status = falcon.HTTP_200
