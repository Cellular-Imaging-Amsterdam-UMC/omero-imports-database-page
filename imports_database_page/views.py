#!/usr/bin/env python
# -*- coding: utf-8 -*-
from omeroweb.webclient.decorators import login_required, render_response
import logging
import jwt
import time
import os

logger = logging.getLogger(__name__)

@login_required()
@render_response()
def imports_database_page(request, conn=None, **kwargs):
    metabase_site_url = os.environ.get('METABASE_SITE_URL')
    metabase_secret_key = os.environ.get('METABASE_SECRET_KEY')

    # Get the current user's information
    current_user = conn.getUser()
    username = current_user.getName()
    user_id = current_user.getId()

    payload = {
        "resource": {"dashboard": 2},
        "params": {
            "user": user_id,
        },
        "exp": int(time.time()) + (10 * 60)  # 10 minute expiration
    }
    token = jwt.encode(payload, metabase_secret_key, algorithm="HS256")

    context = {
        'metabase_site_url': metabase_site_url,
        'metabase_token': token,
        'template': 'importsdatabase/webclient_plugins/imports_database_page.html',
        'username': username,
        'user_id': user_id
    }
    return context

@login_required()
@render_response()
def imports_webclient_templates(request, base_template, **kwargs):
    """ Simply return the named template for imports database. """
    template_name = f'importsdatabase/webgateway/{base_template}.html'
    return {'template': template_name}
