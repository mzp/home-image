# -*- coding: utf-8 -*-
# main.urls


from werkzeug.routing import (
  Map, Rule, Submount,
  EndpointPrefix, RuleTemplate,
)

def make_rules():
  return [
    EndpointPrefix('main/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'main/index': 'main.views.index',
}
