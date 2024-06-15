from django.test import TestCase

# Create your tests here.

        else:
            Add_party(
                medical_id=medical_id,
                party_name=party_name,
                party_address=party_address,
                license_number=license_number,
                gst_number=gst_number
                ).save()
            status = 1

if p:
            status = 0
            #k = Add_party.objects.values().get(gst_number=gst_number, license_number=license_number, medical_id=medical_id)