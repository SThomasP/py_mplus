import unittest
import pathlib
from mplus import parse


class SeriesTests(unittest.TestCase):
    def test_soloist(self):
        soloist = load('soloist.bin')
        self.assertTrue(hasattr(soloist, 'success'))
        self.assertFalse(hasattr(soloist, 'error'))
        self.assertTrue(hasattr(soloist.success, 'title_detail_view'))
        details = soloist.success.title_detail_view
        self.assertTrue(hasattr(details, 'title'))
        title = details.title
        self.assertEqual(title.name, "Soloist in A Cage")
        self.assertEqual(title.author, "Shiro Moriya")
        self.assertEqual(title.title_id, 100047)
        self.assertFalse(hasattr(details, 'last_chapters'))
        self.assertTrue(hasattr(details, 'first_chapters'))
        self.assertEqual(len(details.first_chapters), 10)

    def test_hunterxhunter(self):
        hunters = load('hunterxhunter.bin')
        self.assertTrue(hasattr(hunters, 'success'))
        self.assertFalse(hasattr(hunters, 'error'))
        self.assertTrue(hasattr(hunters.success, 'title_detail_view'))
        details = hunters.success.title_detail_view
        self.assertTrue(hasattr(details, 'title'))
        title = details.title
        self.assertEqual(title.name, "Hunter x Hunter")
        self.assertEqual(title.author, "Yoshihiro Togashi")
        self.assertTrue(hasattr(details, 'banners'))
        self.assertEqual(len(details.banners), 1)
        self.assertEqual(details.banners[0].action.url,
                         "https://www.viz.com/hunter-x-hunter?utm_source=MangaPlus&utm_campaign=HunterXHunterGN&utm_medium=referral&series=10015")
        self.assertTrue(details.is_simul_release)
        self.assertEqual(details.number_of_views, 26715)


fp = pathlib.Path(__file__).parent.absolute()


def load(filename):
    with fp.joinpath(filename).open('rb') as bf:
        bites = bf.read()
    return parse(bites)
