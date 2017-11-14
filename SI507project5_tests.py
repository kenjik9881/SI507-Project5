import unittest
from SI507project5_code import *


class Testing98Degrees_Part1(unittest.TestCase):
    def setUp(self):
        self.tumblr_post_search_baseurl = "https://api.tumblr.com/v2/tagged"
        self.tumblr_post_params = {'tag': "98 Degrees", 'limit': 10}
        self.tumblr_tagresult = get_data_from_api(self.tumblr_post_search_baseurl,"Tumblr", self.tumblr_post_params)
        self.tumblr_response_list1 = self.tumblr_tagresult['response']
        self.tumblr_response_rows = [(arow['blog_name'],arow['post_url'], arow['tags'], arow['liked']) for arow in self.tumblr_response_list1]

    def test_limit_results(self):
        self.assertEqual(len(self.tumblr_response_list1), 10)

    def test_tags(self):
        self.oneresult = self.tumblr_response_rows[0][2]
        self.assertIn('98 Degrees'.lower(), self.oneresult)

    def test_tuples(self):
        for row in self.tumblr_response_rows:
            self.assertEqual(type(row), tuple)
    def tearDown(self):
        pass

class Testing98Degrees_Part2(unittest.TestCase):
    def setUp(self):
        self.tumblr_audio_search_baseurl = "https://api.tumblr.com/v2/blog/thesongsyouusedtolove.tumblr.com/posts/audio"
        self.tumblr_params = {'tag': "98 Degrees", 'limit': 10}

        self.tumblr_audioresult = get_data_from_api(self.tumblr_audio_search_baseurl,"Tumblr", self.tumblr_params) # Default expire_in_days
        self.tumblr_response_list2 = self.tumblr_audioresult['response']['posts']
        # pprint.pprint(tumblr_response_list2)
        self.song_tuples = []
        for apost in self.tumblr_response_list2:
            track_name = apost['track_name']
            num_plays = apost['plays']
            post_url = apost['post_url']
            self.song_tuples.append((track_name, num_plays,post_url))

    def test_are_tuples(self):
        for elem in self.song_tuples:
            self.assertEqual(type(elem), tuple)
            self.assertEqual(len(elem), 3)

    def test_content_of_tuple(self):
        self.assertEqual(self.song_tuples[0][0], 'I Do (Cherish You)')
        self.assertEqual(self.song_tuples[0][1], 599)
        self.assertEqual(self.song_tuples[0][2], 'http://thesongsyouusedtolove.tumblr.com/post/52888456391/98-degrees-i-do-cherish-you-1999')

    def tearDown(self):
        pass








if __name__ == "__main__":
    unittest.main(verbosity=2)
