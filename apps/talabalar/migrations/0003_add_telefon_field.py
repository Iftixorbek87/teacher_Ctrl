from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('talabalar', '0002_alter_vazifabajarish_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='talaba',
            name='telefon',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Telefon raqami'),
        ),
    ]
