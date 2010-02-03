# -*- coding: utf-8 -*-
# main.views

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""

from kay.utils import render_to_response
from google.appengine.api import images
import home_image
from werkzeug import Response
# Create your views here.

def index(request):
  return render_to_response('main/index.html', {'message': 'Hello'})

HomeImage = home_image.HomeImage(54,54,
                                 home_image.Spec(4,0),
                                 home_image.Spec(4,0))

def miku(request):
  data = request.files['image'].stream.read()
  img =  HomeImage.split(images.Image(data))[0]
  png = img.execute_transforms(output_encoding=images.PNG)
  r = Response()
  r.content_type = 'image/png'
  r.data = png
  return r
