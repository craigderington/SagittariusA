import sys
from django.utils import timezone
from django.core.urlresolvers import reverse
from galaxies.models import Galaxy
from django.test import TestCase

# Create your tests here.

class GalaxyDetailViewTest(TestCase):
    def setUp(self):
        super(GalaxyDetailViewTest, self).setUp()
        self.galaxy = Galaxy.objects.create(
            galaxy_name = 'Milky Way',
            galaxy_type = 'Spiral',
            constellation = 'Sagittarius',
            notes = 'none',
            distance = '28.4',
            diameter = '28.6',
            number_of_stars = 400000000,
            galaxy_mass = '1.5 x 10*12 M',
            created_at = timezone.now()
        )


    def tearDown(self):
        super(GalaxyDetailViewTest, self).tearDown()
        self.galaxy.delete()


    def galaxy_post_detail_success(self):
        response = self.client.get(reverse('galaxy:galaxy-detail',
                                           args=(self.galaxy.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add New Galaxy')


    def galaxy_post_detail_404(self):
        response = self.client.get(reverse('galaxy:galaxy-detail',
                                           args=(sys.maxint,)))
        self.assertEqual(response.status_code, 404)
