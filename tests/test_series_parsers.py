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


fp = pathlib.Path(__file__).parent.absolute()


def load(filename):
    with fp.joinpath(filename).open('rb') as bf:
        bites = bf.read()
    return parse(bites)
