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
      Rule('/miku', endpoint='miku'),
    ]),
  ]

all_views = {
  'main/index': 'main.views.index',
  'main/miku': 'main.views.miku',
}
