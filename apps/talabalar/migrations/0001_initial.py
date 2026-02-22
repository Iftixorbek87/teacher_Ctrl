from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guruhlar', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism_familya', models.CharField(max_length=200, verbose_name='Ism-familya')),
                ('telefon', models.CharField(blank=True, default='', max_length=20, verbose_name='Telefon raqami')),
                ('telegram', models.CharField(blank=True, default='', max_length=100, verbose_name='Telegram username')),
                ('yaratilgan', models.DateTimeField(auto_now_add=True)),
                ('guruh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talabalar', to='guruhlar.guruh', verbose_name='Guruh')),
            ],
            options={
                'verbose_name': 'Talaba',
                'verbose_name_plural': 'Talabalar',
                'ordering': ['ism_familya'],
            },
        ),
        migrations.CreateModel(
            name='VazifaBajarish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vazifa_raqam', models.IntegerField(verbose_name='Vazifa raqami')),
                ('bajarildi', models.BooleanField(default=False)),
                ('vaqt', models.DateTimeField(blank=True, null=True)),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vazifalar', to='talabalar.talaba')),
            ],
            options={
                'verbose_name': 'Vazifa bajarishi',
                'verbose_name_plural': 'Vazifa bajarishlari',
                'ordering': ['vazifa_raqam'],
                'unique_together': {('talaba', 'vazifa_raqam')},
            },
        ),
    ]
