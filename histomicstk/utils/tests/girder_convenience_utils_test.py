# -*- coding: utf-8 -*-
import unittest
from histomicstk.utils.girder_convenience_utils import connect_to_api, \
    update_permissions_for_annotation

# %%===========================================================================
# Constants & prep work

APIURL = 'http://candygram.neurology.emory.edu:8080/api/v1/'
APIKEY = 'kri19nTIGOkWH01TbzRqfohaaDWb6kPecRqGmemb'

# %%===========================================================================


class GirderConvenienceTest(unittest.TestCase):
    """Test utilities for interaction with girder."""

    def test_connect_to_api(self):
        """Test get_image_from_htk_response."""
        gc = connect_to_api(APIURL, apikey=APIKEY)
        self.assertEqual(gc.urlBase, APIURL)

    def test_update_permissions_for_annotation(self):
        annid = "5e2a2d77ddda5f83986d135d"
        resp = update_permissions_for_annotation(
            gc=connect_to_api(APIURL, interactive=True),
            annotation_id=annid,
            users_to_add=[
                {'login': 'kheffah',
                    'level': 2, 'id': '59bc677892ca9a0017c2e855'},
                {'login': 'testing',
                    'level': 0, 'id': '5d588370bd4404c6b1f28933'},
            ],
            replace_original_users=True
        )
        self.assertListEqual(
            resp['access']['users'],
            [{'flags': [], 'id': '59bc677892ca9a0017c2e855', 'level': 2},
             {'flags': [], 'id': '5d588370bd4404c6b1f28933', 'level': 0}]
        )


# %%===========================================================================


if __name__ == '__main__':
    unittest.main()
