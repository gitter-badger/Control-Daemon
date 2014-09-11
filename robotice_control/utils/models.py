# -*- coding: utf-8 -*-
from django.db import models

from django.forms.models import model_to_dict

from yaml import safe_dump, load


class RoboticeModelMixin(object):

    @property
    def to_dict(self):
        return model_to_dict(self)

    @property
    def to_yaml(self):
        result = {}
        try:
            _dict = self.to_dict
            result = safe_dump(_dict)
        except Exception, e:
            if _dict:
                for key,value in _dict.iteritems():
                    if isinstance(key, dict) or isinstance(value, dicz):
                        # TODO
                        continue
                    result[key] = value

        if isinstance(result, dict):
            return safe_dump(result)

        return result

    def data_to_yaml(self, data):
        """return data in yaml
        """

        return safe_dump(data)