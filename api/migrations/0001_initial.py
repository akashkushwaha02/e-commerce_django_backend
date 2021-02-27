from django.db import migrations

from api.user.models import CustomUser


class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(first_name='akash',
            email='akash.kushwaha02@gmail.com',
            is_staff=True,
            phone='7489653839',
            gender='Male',
            is_superuser=True)
        user.set_password('1234')
        user.save()



    dependencies = [    
    ]

    operations = [
        migrations.RunPython(seed_data),
            
    ]