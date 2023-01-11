import pytest
from gradescope_utils import *
import unittest

class TestP2(unittest.TestCase):
    self.pclient = PokeClient()
    self.pokemon = pclient.get_pokemon_list()
    
    @weight(1)
    def test_index(self, client):
        resp = client.get("/")
        self.assertEqual(resp.status_code, 200)
        for p in pokemon[:151]:
            s = "<a href=\"/pokemon/" + p + "\">"
            self.assertEqual(s in resp.data, True)

   @weight(1)
    def test_links(self, client):
        passed = True   
        for p in pokemon:
            r = client.get("/pokemon/" + p)
            if r.status_code != 200:
                passed = False
                break

        self.assertEqual(passed, True)







