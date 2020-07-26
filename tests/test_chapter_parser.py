import unittest
from tests import urls
import requests
from mplus import parse, HEADER


class ChapterTests(unittest.TestCase):
    def get(self, url):
        r = requests.get(url, headers={'SESSION-TOKEN': HEADER})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers['Content-Type'], 'application/octet-stream')
        return parse(r.content)

    def get_chapter_view(self, response_obj):
        self.assertTrue(hasattr(response_obj, 'success'))
        self.assertFalse(hasattr(response_obj, 'error'))
        self.assertTrue(hasattr(response_obj.success, 'manga_viewer'))
        return response_obj.success.manga_viewer

    def test_hw_1(self):
        hw_1 = self.get(urls.HW_1)
        manga_viewer = self.get_chapter_view(hw_1)
        self.assertEqual('Hell Warden Higuma', manga_viewer.title_name)
        self.assertEqual('#001', manga_viewer.chapter_name)
        self.assertEqual(57, len(manga_viewer.pages))
        self.assertTrue(hasattr(manga_viewer.pages[14], 'manga_page'))
        self.assertTrue(hasattr(manga_viewer.pages[56], 'last_page'))
        self.assertTrue(hasattr(manga_viewer.pages[55], 'advertisement'))
        self.assertFalse(hasattr(manga_viewer, 'is_vertical_only'))

    def test_bc_23(self):
        bc_23 = self.get(urls.BC_23)
        manga_viewer = self.get_chapter_view(bc_23)
        self.assertEqual('Beast Children', manga_viewer.title_name)
        self.assertEqual('#023', manga_viewer.chapter_name)
        self.assertEqual(21, len(manga_viewer.pages))
        self.assertTrue(hasattr(manga_viewer.pages[12], 'manga_page'))
        self.assertTrue(hasattr(manga_viewer.pages[19], 'advertisement'))
        self.assertTrue(hasattr(manga_viewer.pages[20], 'last_page'))
        last_page = manga_viewer.pages[20].last_page
        self.assertEqual('#024', last_page.next_chapter.name)
        self.assertEqual(5, len(last_page.top_comments))