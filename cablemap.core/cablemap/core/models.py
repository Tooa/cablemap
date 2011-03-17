# -*- coding: utf-8 -*-
#
# Copyright (c) 2011 -- Lars Heuer <heuer[at]semagia.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#
#     * Neither the project name nor the names of the contributors may be 
#       used to endorse or promote products derived from this software 
#       without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
"""\
This module provides models to keep data about cables.

:author:       Lars Heuer (heuer[at]semagia.com)
:organization: Semagia - <http://www.semagia.com/>
:license:      BSD license
"""
from cablemap.core.constants import MALFORMED_CABLE_IDS

__all__ = ['Cable']

# Commonly used base URIs for Wikileaks Cablegate
# Formats: 
# * BASE/<year>/<month>/<reference-id>
# * BASE/<year>/<month>/<reference-id>.html
_WL_CABLE_BASE_URIS = (
                'http://wikileaks.ch/cable/',
                'http://cablegate.wikileaks.org/cable/',
                'http://213.251.145.96/cable/'
                )

# Source: <https://github.com/mitsuhiko/werkzeug/blob/master/werkzeug/utils.py#L30>
class cached_property(object):
    """\
    A decorator that converts a function into a lazy property.
    """
    _missing = object()

    def __init__(self, func, name=None, doc=None):
        self.__name__ = name or func.__name__
        self.__module__ = func.__module__
        self.__doc__ = doc or func.__doc__
        self.func = func

    def __get__(self, obj, type=None):
        if obj is None:
            return self
        value = obj.__dict__.get(self.__name__, cached_property._missing)
        if value is cached_property._missing:
            value = self.func(obj)
            obj.__dict__[self.__name__] = value
        return value


class _CableBase(object):
    """\
    Internal class
    """
    def __init__(self, reference_id):
        """\
        
        `reference_id`
            The reference identifier of the cable
        """
        if not reference_id:
            raise ValueError('The reference id must be provided')
        self.reference_id = unicode(reference_id) # Ensure Unicode
        self.origin = None
        self.header = None
        self.content = None
        self.created = None
        self.released = None
        self.partial = False

    @cached_property
    def wl_uris(self):
        """\
        Returns cable IRIs to WikiLeaks (mirrors).
        """
        def year_month(d):
            date, time = d.split()
            return date.split('-')[:2]
        if not self.created:
            raise ValueError('The "created" property must be provided')
        year, month = year_month(self.created)
        reference_id = self.reference_id
        if reference_id in MALFORMED_CABLE_IDS.values():
            for k, v in MALFORMED_CABLE_IDS.iteritems():
                if v == reference_id:
                    reference_id = k
                    break
        l = '%s/%s/%s' % (year, month, reference_id)
        html = l + '.html'
        wl_uris = []
        append = wl_uris.append
        for wl in _WL_CABLE_BASE_URIS:
            append(wl + l)
            append(wl + html)
        return wl_uris

    def __unicode__(self):
        return self.reference_id

    def to_dict(self):
        """\
        Returns a dict representation.
        """
        return dict(
                    identifier=self.reference_id,
                    tags=self.tags,
                    created=self.created,
                    released=self.released,
                    subject=self.subject,
                    origin=self.origin,
                    references=self.references,
                    recipients=self.recipients,
                    info=self.info_recipients,
                    partial=self.partial,
                    classification=self.classification,
                    summary=self.summary,
                    header=self.header,
                    body=self.content,
                    )

    @staticmethod
    def from_dict(dct):
        """\
        Returns a cable from a dict.

        `dct`
            A dict which must be compatible to the dict generated by `to_dict`
        """
        cable = _ModifiableCable(dct['identifier'])
        cable.tags = dct.get('tags', [])
        cable.created = dct.get('created')
        cable.released = dct.get('released')
        cable.subject = dct.get('subject')
        cable.origin = dct.get('origin')
        cable.references = dct.get('references', [])
        cable.recipients = dct.get('recipients', [])
        cable.info_recipients = dct.get('info', [])
        cable.partial = dct.get('partial', False)
        cable.classification = dct.get('classification')
        cable.summary = dct.get('summary')
        cable.header = dct.get('header')
        cable.content = dct.get('body')
        return cable


class _ModifiableCable(_CableBase):
    """\
    Holds data about a cable.
    
    An instance of this class should be treated as immutable outside of 
    ``cablemap.core``.

    >>> cable = Cable('something')
    >>> cable.reference_id
    u'something'
    >>> cable.wl_uris
    Traceback (most recent call last):
    ...
    ValueError: The "created" property must be provided
    >>> cable.created = '2011-07-12 12:12:00'
    >>> cable.wl_uris
    [u'http://wikileaks.ch/cable/2011/07/something', u'http://wikileaks.ch/cable/2011/07/something.html', u'http://cablegate.wikileaks.org/cable/2011/07/something', u'http://cablegate.wikileaks.org/cable/2011/07/something.html', u'http://213.251.145.96/cable/2011/07/something', u'http://213.251.145.96/cable/2011/07/something.html']
    >>> cable.summary is None
    True
    >>> d = cable.to_dict()
    >>> d['summary'] is None
    True
    >>> cable.summary = 'Summary'
    >>> d = cable.to_dict()
    >>> d['summary']
    'Summary'
    """
    def __init__(self, reference_id):
        super(_ModifiableCable, self).__init__(reference_id)
        self.transmission_id = None
        self.recipients = []
        self.info_recipients = []
        self.references = []
        self.subject = u''
        self.tags = []
        self.nondisclosure_deadline = None
        self.classification = []
        self.content_header = None
        self.content_body = None
        self.summary = None

def reader():
    from cablemap.core import reader
    return reader


class Cable(_CableBase):
    """\
    Holds data about a cable.
    """
    def __init__(self, reference_id):
        super(Cable, self).__init__(reference_id)

    #
    # Header properties
    #
    @cached_property
    def transmission_id(self):
        if self.partial:
            return None
        return reader().parse_transmission_id(self.header, self.reference_id)

    @cached_property
    def recipients(self):
        if self.partial:
            return ()
        return reader().parse_recipients(self.header, self.reference_id)

    @cached_property
    def info_recipients(self):
        return reader().parse_info_recipients(self.header, self.reference_id)

    #
    # Content properties
    #
    @cached_property
    def subject(self):
        return reader().parse_subject(self.content, self.reference_id)

    @cached_property
    def nondisclosure_deadline(self):
        return reader().parse_nondisclosure_deadline(self.content)

    @cached_property
    def parse_references(self):
        return reader().parse_references(self.content, self.created[:4], self.reference_id)

    @cached_property
    def tags(self):
        return reader().parse_tags(self.content, self.reference_id)

    @cached_property
    def summary(self):
        return reader().parse_summary(self.content, self.reference_id)

    @cached_property
    def content_header(self):
        return reader().header_body_from_content(self.content)[0]

    @cached_property
    def content_body(self):
        return reader().header_body_from_content(self.content)[1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
