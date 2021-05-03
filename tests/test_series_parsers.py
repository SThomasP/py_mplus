import unittest
from tests import urls
import requests
from py_mplus import parse, HEADER


class SeriesTests(unittest.TestCase):
    def get(self, url):
        r = requests.get(url, headers={'SESSION-TOKEN': HEADER})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/octet-stream')
        return parse(r.content)

    def get_details(self, response_obj):
        self.assertTrue(hasattr(response_obj, 'success'))
        self.assertFalse(hasattr(response_obj, 'error'))
        self.assertTrue(hasattr(response_obj.success, 'title_detail_view'))
        return response_obj.success.title_detail_view

    def test_soloist(self):
        soloist = self.get(urls.SOLOIST)
        details = self.get_details(soloist)
        self.assertTrue(hasattr(details, 'title'))
        title = details.title
        self.assertEqual("Soloist in A Cage", title.name)
        self.assertEqual("Shiro Moriya", title.author)
        self.assertFalse(hasattr(details, 'last_chapters'))
        self.assertTrue(hasattr(details, 'first_chapters'))
        self.assertLessEqual(10, len(details.first_chapters))

    def test_curtains(self):
        curtains = self.get(urls.CURTAINS)
        details = self.get_details(curtains)
        self.assertTrue(hasattr(details, 'title'))
        title = details.title
        self.assertEqual("Curtain's up, I'm off", title.name)
        self.assertEqual("Akitaka Imakoshi", title.author)
        self.assertTrue(details.is_simul_release)
        self.assertEqual('This title is completed.', details.non_appearance_info)
        self.assertLessEqual(1625, details.number_of_views)
        self.assertFalse(hasattr(details, 'last_chapters'))
        self.assertTrue(hasattr(details, 'first_chapters'))
        self.assertEqual(33, len(details.first_chapters))
        last_chapter = details.first_chapters[32]
        self.assertEqual(last_chapter.title_id, title.title_id)
        self.assertFalse(hasattr(last_chapter, 'is_vertical_only'))
        self.assertEqual('#026', last_chapter.name)
        self.assertEqual('Final Chapter: And So, Into Spring', last_chapter.subtitle)

    def test_hunterxhunter(self):
        hunters = self.get(urls.HUNTERS)
        details = self.get_details(hunters)
        self.assertTrue(hasattr(details, 'title'))
        title = details.title
        self.assertEqual("Hunter x Hunter", title.name)
        self.assertEqual("Yoshihiro Togashi", title.author)
        self.assertTrue(hasattr(details, 'banners'))
        self.assertEqual(1, len(details.banners))
        self.assertEqual(
            "https://www.viz.com/hunter-x-hunter?utm_source=MangaPlus&utm_campaign=HunterXHunterGN&utm_medium=referral&series=10015"
            , details.banners[0].action.url)
        self.assertTrue(details.is_simul_release)
        self.assertTrue(hasattr(details, 'last_chapters'))
        self.assertEqual(3, len(details.last_chapters))
        self.assertTrue(hasattr(details, 'first_chapters'))
        self.assertTrue(3, len(details.first_chapters))
