import unittest
import json
from datetime import datetime
from SI507project5_code import *

#test files exist
#test file contents
#test cache exists

class Prob1(unittest.TestCase):
    def setUp(self):
        self.post_data = open("ind_post_data.csv", 'r')
        self.agg_data = open ("post_tags_data.csv", 'r')
        self.post_data_contents = open("ind_post_data.csv", 'r')
        self.agg_data_contents = open ("post_tags_data.csv", 'r')
        self.cache = open("tumblr_cache_contents.json", 'r')
        self.creds_f = open("tumblr_creds.json", 'r')
        self.creds = json.load(self.creds_f)
        self.posts = post_data

    def test_files(self):
        self.assertTrue(self.post_data.read())
        self.assertTrue(self.agg_data.read())

    def test_file_contents (self):
        self.assertTrue(int(self.post_data_contents.readlines()[1].split(',')[1])>0)
        self.assertTrue(int(self.agg_data_contents.readlines()[1].split(',')[1])>0)

    def test_cache_exists(self):
        self.assertTrue(self.cache)

    def test_cache_time(self):
        self.assertFalse(has_cache_expired(self.creds["TUMBLR"]['timestamp'], self.creds["TUMBLR"]['expire_in_days']))

    def test_post_class(self):
        for e in self.posts:
            self.assertTrue(e.id)
            self.assertTrue(e.engagements <= 50)

    def tearDown(self):
        self.post_data.close()
        self.agg_data.close()
        self.post_data_contents.close()
        self.agg_data_contents.close()
        self.cache.close()
        self.creds_f.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)
