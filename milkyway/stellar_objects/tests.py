import sys
from django.utils import timezone
from django.core.urlresolvers import reverse
from stellar_objects.models import StellarObject
from django.test import TestCase

# Create your tests here.

class StellarObjectDetailViewTest(TestCase):
    def setUp(self):
        super(StellarObjectDetailViewTest, self).setUp()
        self.stellarobject = StellarObject.objects.create(
            name = 'GH3789',
            stellar_object_type = 'Protostar',
            constellation = 'Sagittarius',
            distance = '12.8'
            created_at = timezone.now()
        )


    def tearDown(self):
        super(StellarObjectDetailViewTest, self).tearDown()
        self.stellarobject.delete()


    def stellarobject_post_detail_success(self):
        response = self.client.get(reverse('stellar:stellar-detail',
                                           args=(self.StellarObject.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add New StellarObject')


    def stellarobject_post_detail_404(self):
        response = self.client.get(reverse('stellar:stellar-detail',
                                           args=(sys.maxint,)))
        self.assertEqual(response.status_code, 404)
