import sys
from django.utils import timezone
from django.core.urlresolvers import reverse
from constellations.models import Constellation
from django.test import TestCase

# Create your tests here.

class ConstellationDetailViewTest(TestCase):
    def setUp(self):
        super(ConstellationDetailViewTest, self).setUp()
        self.constellation = Constellation.objects.create(
            constellation_name = 'Andromeda',
            iau_abbr = 'And',
            other_abbr = 'Andr',
            genitive = 'Andromedae',
            family = 'Perseus',
            origin = 'Ptolemy',
            meaning = 'The Chained Woman',
            brightest_star = '',
            right_ascension = '4h 6m 12.345s',
            declination = '10.87'
            number_of_stars = '10',
            stars_with_planets = '8',
            created_at = timezone.now()
        )


    def tearDown(self):
        super(ConstellationDetailViewTest, self).tearDown()
        self.constellation.delete()


    def constellation_post_detail_success(self):
        response = self.client.get(reverse('constellation:constellation-detail',
                                           args=(self.constellation.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add New Constellation')


    def constellation_post_detail_404(self):
        response = self.client.get(reverse('constellation:constellation-detail',
                                           args=(sys.maxint,)))
        self.assertEqual(response.status_code, 404)
