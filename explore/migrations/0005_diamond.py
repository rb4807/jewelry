# Generated by Django 4.2.2 on 2023-07-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0004_anklet_ban_brace_co_ear_neck_pen_ri'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diamond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='Diamond')),
            ],
        ),
    ]
