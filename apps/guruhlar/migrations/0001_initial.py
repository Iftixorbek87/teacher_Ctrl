from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [('patoklar', '0001_initial')]
    operations = [
        migrations.CreateModel(
            name='Guruh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nomi', models.CharField(max_length=150, verbose_name='Guruh nomi')),
                ('jami_vazifalar', models.IntegerField(default=75, verbose_name='Jami vazifalar soni')),
                ('tavsif', models.TextField(blank=True, verbose_name='Tavsif')),
                ('yaratilgan', models.DateTimeField(auto_now_add=True)),
                ('patok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guruhlar', to='patoklar.patok', verbose_name='Patok')),
            ],
            options={'verbose_name': 'Guruh', 'verbose_name_plural': 'Guruhlar', 'ordering': ['nomi']},
        ),
    ]
