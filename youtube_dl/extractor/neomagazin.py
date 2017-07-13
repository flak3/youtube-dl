# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class NeoMagazinIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?neo-magazin-royale\.de/zdi/artikel/(?P<id>[^/?]+)/(.*).html'
    _TEST = {
        'url': 'http://www.neo-magazin-royale.de/zdi/artikel/137606/neo-magazin-royale-vom-22-06-2017.html',
        'md5': 'c2cd59aa16bcfafbc1db9c906f602a18',
        'info_dict': {
            'id': 'neo-magazin-royale-mit-jan-boehmermann-vom-22-juni-2017-100',
            'title': 'NEO MAGAZIN ROYALE mit Jan Böhmermann vom 22. Juni 2017',
            'ext': 'mp4',
            'upload_date': '20170622',
            'description': 'md5:43b3dc0c1027bf8aae732ac4415c6179',
            'timestamp': 1498162500
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        title = self._meta_regex('description')

        zdf_id = self._search_regex(r'(?s)data-sophoraid=(["\'])(?P<id>.*?)\1', webpage, 'player id', group='id')

        return {
            '_type': 'url',
            'id': video_id,
            'title': title,
            'url': 'https://www.zdf.de/comedy/neo-magazin-mit-jan-boehmermann/%s.html' % zdf_id,
            'ie_type': 'ZDF'
        }
