import unittest
from Modules.text_analyze import *


class MyTestCase(unittest.TestCase):
    def test_numberOfWords(self):
        test = TextAnalyzer()
        with self.subTest():
            self.assertEqual(test.numberOfWords("../Temp/test1file.txt"), 1)
        with self.subTest():
            self.assertEqual(test.numberOfWords("../Temp/test1fileB.txt"), 40)

    def test_numberOfWordsWithSpace(self):
        test = TextAnalyzer()
        with self.subTest():
            self.assertEqual(test.numberOfAllCharacters("../Temp/test1file.txt"), 4)
        with self.subTest():
            self.assertEqual(test.numberOfAllCharacters("../Temp/test1fileB.txt"), 289)

    def test_numberOfSpecialCharacters(self):
        test = TextAnalyzer()
        with self.subTest():
            self.assertEqual(test.numberOfSpecialCharacters("../Temp/test1fileB.txt"), 8)
        with self.subTest():
            self.assertEqual(test.numberOfSpecialCharacters("../Temp/test2fileA.txt"), 16)

    def test_countEachWord(self):
        test = TextAnalyzer()
        D1 = {'ipsum': 2, 'dolor': 2, 'vitae': 2, 'curabitur': 2, 'ut': 2, 'lorem': 1, 'sit': 1, 'amet,': 1, 'consectetur': 1, 'adipiscing': 1, 'elit.': 1, 'proin': 1, 'cursus': 1, 'hendrerit': 1, 'pellentesque.': 1, 'aliquam': 1, 'commodo': 1, 'justo': 1, 'arcu': 1, 'mollis': 1, 'pulvinar.': 1, 'ac': 1, 'turpis': 1, 'risus.': 1, 'placerat': 1, 'ornare': 1, 'magna,': 1, 'a': 1, 'rhoncus': 1, 'molestie': 1, 'faucibus.': 1, 'phasellus': 1, 'suscipit': 1, 'urna': 1, 'finibus.': 1}
        D2 = {'sed': 39, 'in': 35, 'nec': 31, 'sit': 30, 'quis': 29, 'at': 28, 'vestibulum': 25, 'ut': 24, 'nulla': 24, 'eget': 24, 'et': 24, 'amet': 23, 'a': 23, 'eu': 23, 'id': 23, 'ac': 20, 'nunc': 19, 'vel': 19, 'mauris': 18, 'donec': 18, 'vitae': 17, 'cras': 16, 'tincidunt': 16, 'non': 14, 'mi': 14, 'metus': 14, 'lorem': 13, 'aliquam': 13, 'semper': 13, 'quisque': 13, 'etiam': 13, 'ipsum': 12, 'leo': 12, 'viverra': 12, 'porta': 12, 'sodales': 12, 'nam': 12, 'posuere': 12, 'luctus': 12, 'lectus': 12, 'morbi': 12, 'integer': 11, 'vulputate': 11, 'sem': 11, 'pellentesque': 11, 'augue': 11, 'facilisis': 11, 'fermentum': 11, 'interdum': 11, 'ante': 11, 'faucibus': 11, 'rhoncus': 11, 'praesent': 11, 'blandit': 11, 'dignissim': 11, 'velit': 10, 'egestas': 10, 'tempor': 10, 'maximus': 10, 'venenatis': 10, 'orci': 10, 'phasellus': 10, 'ligula': 10, 'ornare': 10, 'pretium': 10, 'volutpat': 10, 'iaculis': 9, 'neque': 9, 'auctor': 9, 'est': 9, 'pulvinar': 9, 'efficitur': 9, 'quam': 9, 'pharetra': 9, 'aenean': 9, 'bibendum': 9, 'ultrices': 9, 'tellus': 9, 'aliquet': 9, 'congue': 9, 'risus': 9, 'dolor': 8, 'consectetur': 8, 'rutrum': 8, 'suspendisse': 8, 'suscipit': 8, 'elementum': 8, 'ultricies': 8, 'accumsan': 8, 'felis.': 8, 'nibh': 8, 'eros': 8, 'ex': 8, 'vivamus': 8, 'erat': 8, 'risus.': 8, 'hendrerit': 8, 'placerat': 8, 'dictum': 8, 'sagittis': 8, 'cursus': 7, 'fringilla': 7, 'duis': 7, 'libero': 7, 'eleifend': 7, 'imperdiet': 7, 'consequat': 7, 'varius': 7, 'erat.': 7, 'gravida': 7, 'scelerisque': 7, 'elit': 7, 'felis': 7, 'urna': 7, 'amet,': 6, 'turpis': 6, 'lacus': 6, 'sollicitudin': 6, 'tempus': 6, 'vehicula': 6, 'commodo': 6, 'dapibus': 6, 'lobortis': 6, 'proin': 6, 'arcu.': 6, 'purus': 6, 'tristique': 6, 'elit.': 5, 'dui': 5, 'enim.': 5, 'nisl': 5, 'turpis.': 5, 'sapien.': 5, 'mollis': 5, 'dui,': 5, 'malesuada': 5, 'primis': 5, 'convallis': 5, 'justo.': 5, 'maecenas': 5, 'arcu': 5, 'molestie': 5, 'vitae,': 5, 'euismod': 5, 'massa': 5, 'ligula.': 5, 'nisi': 5, 'nullam': 5, 'enim': 5, 'mattis.': 5, 'condimentum': 5, 'tortor.': 5, 'finibus': 4, 'nisl,': 4, 'non,': 4, 'diam': 4, 'dictum.': 4, 'nisi.': 4, 'velit.': 4, 'mattis': 4, 'sapien': 4, 'odio': 4, 'urna,': 4, 'at.': 4, 'porttitor': 4, 'tortor,': 4, 'suscipit,': 4, 'libero.': 4, 'id,': 4, 'arcu,': 4, 'dui.': 4, 'tortor': 4, 'dolor.': 4, 'magna': 4, 'vel,': 4, 'metus.': 4, 'est,': 4, 'curabitur': 4, 'massa.': 4, 'ex,': 4, 'justo': 4, 'per': 4, 'adipiscing': 3, 'lacinia': 3, 'libero,': 3, 'ipsum.': 3, 'fermentum.': 3, 'nibh,': 3, 'ut,': 3, 'fusce': 3, 'vulputate.': 3, 'tincidunt.': 3, 'faucibus.': 3, 'augue.': 3, 'enim,': 3, 'tellus.': 3, 'cubilia': 3, 'curae;': 3, 'at,': 3, 'vel.': 3, 'augue,': 3, 'mollis.': 3, 'nulla.': 3, 'pharetra.': 3, 'lacinia.': 3, 'facilisi.': 3, 'nisl.': 3, 'urna.': 3, 'quis,': 3, 'purus,': 3, 'ac.': 3, 'maximus.': 3, 'quam.': 3, 'viverra.': 3, 'eros.': 3, 'euismod.': 3, 'laoreet.': 2, 'venenatis.': 2, 'potenti.': 2, 'magna,': 2, 'quis.': 2, 'malesuada.': 2, 'eros,': 2, 'ac,': 2, 'odio.': 2, 'aliquam.': 2, 'suscipit.': 2, 'laoreet': 2, 'congue.': 2, 'feugiat': 2, 'nunc.': 2, 'fames': 2, 'accumsan.': 2, 'egestas,': 2, 'diam,': 2, 'ante.': 2, 'lorem.': 2, 'natoque': 2, 'penatibus': 2, 'magnis': 2, 'dis': 2, 'parturient': 2, 'montes,': 2, 'nascetur': 2, 'ridiculus': 2, 'mus.': 2, 'felis,': 2, 'consectetur.': 2, 'posuere.': 2, 'condimentum.': 2, 'elit,': 2, 'leo,': 2, 'mauris,': 2, 'velit,': 2, 'a,': 2, 'magna.': 2, 'semper,': 2, 'sodales.': 2, 'efficitur,': 2, 'ornare,': 2, 'nec,': 2, 'elementum,': 2, 'purus.': 2, 'euismod,': 2, 'porttitor.': 2, 'est.': 2, 'quam,': 2, 'neque.': 2, 'ornare.': 2, 'lorem,': 2, 'hendrerit.': 2, 'pulvinar.': 2, 'placerat,': 2, 'rhoncus,': 2, 'sed,': 2, 'facilisis.': 2, 'pellentesque.': 2, 'nec.': 2, 'ullamcorper': 2, 'id.': 2, 'dapibus.': 2, 'sapien,': 2, 'feugiat.': 2, 'class': 2, 'aptent': 2, 'taciti': 2, 'sociosqu': 2, 'ad': 2, 'litora': 2, 'torquent': 2, 'conubia': 2, 'nostra,': 2, 'inceptos': 2, 'himenaeos.': 2, 'nibh.': 2, 'mauris.': 2, 'vehicula.': 2, 'gravida.': 2, 'nisi,': 2, 'finibus.': 1, 'viverra,': 1, 'cursus,': 1, 'vestibulum,': 1, 'convallis,': 1, 'dapibus,': 1, 'tempus.': 1, 'mollis,': 1, 'iaculis.': 1, 'accumsan,': 1, 'eu.': 1, 'molestie.': 1, 'sollicitudin.': 1, 'volutpat.': 1, 'rhoncus.': 1, 'pretium.': 1, 'dolor,': 1, 'tempus,': 1, 'dictum,': 1, 'hac': 1, 'habitasse': 1, 'platea': 1, 'dictumst.': 1, 'commodo,': 1, 'lacus.': 1, 'laoreet,': 1, 'non.': 1, 'leo.': 1, 'lobortis.': 1, 'ullamcorper.': 1, 'rutrum.': 1, 'finibus,': 1, 'elementum.': 1, 'tincidunt,': 1, 'lobortis,': 1, 'semper.': 1, 'gravida,': 1, 'blandit,': 1, 'maximus,': 1, 'lacus,': 1, 'condimentum,': 1, 'eleifend.': 1, 'faucibus,': 1, 'ipsum,': 1, 'eget.': 1, 'et,': 1, 'mi,': 1, 'vitae.': 1, 'nunc,': 1, 'amet.': 1, 'imperdiet.': 1, 'hendrerit,': 1, 'consectetur,': 1, 'odio,': 1, 'facilisis,': 1, 'tristique.': 1, 'tellus,': 1, 'molestie,': 1, 'blandit.': 1, 'tempor.': 1, 'porttitor,': 1, 'sodales,': 1, 'commodo.': 1, 'aliquet.': 1, 'ut.': 1, 'in,': 1, 'sem,': 1, 'fringilla.': 1, 'turpis,': 1, 'vestibulum.': 1, 'ullamcorper,': 1, 'ante,': 1, 'in.': 1, 'porta,': 1, 'egestas.': 1, 'ligula,': 1, 'eu,': 1, 'pulvinar,': 1, 'lectus.': 1, 'neque,': 1}

        with self.subTest():
            self.assertDictEqual(test.countEachWord("../Temp/test1fileB.txt"),D1)
        with self.subTest():
            self.assertDictEqual(test.countEachWord("../Temp/test3fileA.txt"),D2)

    def test_numberOfLines(self):
        test = TextAnalyzer()

        with self.subTest():
            self.assertEqual(test.numberOfLines("../Temp/test1file.txt"),1)
        with self.subTest():
            self.assertEqual(test.numberOfLines("../Temp/test1fileB.txt"),6)
        with self.subTest():
            self.assertEqual(test.numberOfLines("../Temp/test2fileA.txt"), 3)

    def test_numberOfUppercase(self):
        test = TextAnalyzer()

        with self.subTest():
            self.assertEqual(test.numberOfUppercase("../Temp/test1file.txt"),0)
        with self.subTest():
            self.assertEqual(test.numberOfUppercase("../Temp/test1fileB.txt"),6)

    def test_countVowels(self):
        test = TextAnalyzer()
        D1= {'e': 1}
        D2 = {'u': 25, 'i': 24, 'a': 19, 'e': 18, 'o': 15, 'A': 1}
        with self.subTest():
            self.assertDictEqual(test.countVowels("../Temp/test1file.txt"),D1)
        with self.subTest():
            self.assertDictEqual(test.countVowels("../Temp/test1fileB.txt"),D2)

    def test_countConsonants(self):
        test = TextAnalyzer()
        D1= {'t': 2, 's': 1}
        D2 = {'r': 21, 's': 21, 't': 18, 'l': 13, 'c': 11, 'n': 11, 'm': 10, 'p': 8, 'd': 5, 'b': 4, 'h': 3, 'v': 3, 'g': 2, 'P': 2, 'q': 2, 'C': 2, 'f': 2, 'L': 1, 'j': 1}
        with self.subTest():
            self.assertDictEqual(test.countConsonants("../Temp/test1file.txt"),D1)
        with self.subTest():
            self.assertDictEqual(test.countConsonants("../Temp/test1fileB.txt"),D2)

if __name__ == '__main__':
    unittest.main()
