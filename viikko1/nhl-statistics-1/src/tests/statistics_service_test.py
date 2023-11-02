import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_haku_toimii(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")

    def test_haku_palauttaa_tyhjan_vaaralla_nimella(self):
        self.assertIsNone(self.stats.search("Nothing"))

    def test_team_palauttaa_oikein_EDM(self):
        tiimi = self.stats.team("EDM")
        self.assertEqual(len(tiimi), 3)
        self.assertEqual(tiimi[0].name, "Semenko")
        self.assertEqual(tiimi[1].name, "Kurri")
        self.assertEqual(tiimi[2].name, "Gretzky")
        
    def test_top_3_palauttaa_kolme(self):
        top3 = self.stats.top(3)
        self.assertEqual(len(top3), 3)
    
    def test_top_1_palauttaa_oikein(self):
        top1 = self.stats.top(1)
        self.assertEqual(len(top1), 1)
        self.assertEqual(top1[0].name, "Gretzky")