from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name='Patok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nomi', models.CharField(max_length=150, verbose_name='Patok nomi')),
                ('tavsif', models.TextField(blank=True, verbose_name='Tavsif')),
                ('yaratilgan', models.DateTimeField(auto_now_add=True)),
                ('oqituvchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patoklar', to=settings.AUTH_USER_MODEL, verbose_name="O'qituvchi")),
            ],
            options={'verbose_name': 'Patok', 'verbose_name_plural': 'Patoklar', 'ordering': ['-yaratilgan']},
        ),
    ]
