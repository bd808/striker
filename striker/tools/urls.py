# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Wikimedia Foundation and contributors.
# All Rights Reserved.
#
# This file is part of Striker.
#
# Striker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Striker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Striker.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import urls


urlpatterns = [
    urls.url(r'^$', 'striker.tools.views.index', name='index'),
    urls.url(
        r'^(?P<tool>[_a-z][-0-9_a-z]*)$',
        'striker.tools.views.tool',
        name='tool'
    ),
    urls.url(
        r'^(?P<tool>[_a-z][-0-9_a-z]*)/create/repo$',
        'striker.tools.views.repo_create',
        name='repo_create'
    ),
    urls.url(
        r'^(?P<tool>[_a-z][-0-9_a-z]*)/edit/repo/(?P<name>[a-z0-9-]+)$',
        'striker.tools.views.repo_edit',
        name='repo_edit'
    ),
]
