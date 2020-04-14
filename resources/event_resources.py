import falcon
from sqlalchemy.orm.exc import NoResultFound

import messages
from db.models import Event
from resources.base_resources import DAMCoreResource


class ResourceGetEvents(DAMCoreResource):
    def on_get(self, req, resp, *args, **kwargs):
        super(ResourceGetEvents, self).on_get(req, resp, *args, **kwargs)


        response_events = list()

        aux_events = self.db_session.query(Event)

        if aux_events is not None:
            for current_event in aux_events.all():
                response_events.append(current_event.json_model)

        resp.media = response_events
        resp.status = falcon.HTTP_200


class ResourceGetEvent(DAMCoreResource):
    def on_get(self, req, resp, *args, **kwargs):
        super(ResourceGetEvent, self).on_get(req, resp, *args, **kwargs)

        if "id" in kwargs:
            try:
                response_event = self.db_session.query(Event).filter(Event.id == kwargs["id"]).one()

                resp.media = response_event.json_model
                resp.status = falcon.HTTP_200
            except NoResultFound:
                raise falcon.HTTPBadRequest(description=messages.event_doesnt_exist)
        else:
            raise falcon.HTTPMissingParam("id")