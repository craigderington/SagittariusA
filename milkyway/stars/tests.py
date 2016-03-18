import sys
from django.utils import timezone
from django.core.urlresolvers import reverse
from stars.models import Star
from django.test import TestCase

# Create your tests here.

class StarDetailViewTest(TestCase):
    def setUp(self):
        super(StarDetailViewTest, self).setUp()
        self.star = Star.objects.create(
            proper_name = 'Alpha Centauri A',
            magnitude = '1.33',
            bayer_designation = 'Alpha Centaurus',
            distance = '4.37',
            spectral_class = 'G2V',
            constellation_name = 'Centaurus',
            evolution_stage = 'Main Sequence',
            star_mass = '1.10',
            star_age = '4.4',
            surface_temperature = '5790',
            visual_brightness = '1.519',
            star_volume = '5.97',
            created_at = timezone.now()
        )


    def tearDown(self):
        super(StarDetailViewTest, self).tearDown()
        self.star.delete()


    def star_post_detail_success(self):
        response = self.client.get(reverse('star:star-detail', args=(self.star.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add New Star')


    def star_post_detail_404(self):
        response = self.client.get(reverse('stars:star-detail', args=(sys.maxint,)))
        self.assertEqual(response.status_code, 404)
