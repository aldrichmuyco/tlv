# Generated by Django 3.0.3 on 2020-03-03 08:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.BooleanField(default=False)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('key', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, default='', max_length=50)),
                ('middle_name', models.CharField(blank=True, default='', max_length=50)),
                ('last_name', models.CharField(blank=True, default='', max_length=50)),
                ('extension', models.CharField(blank=True, default='', max_length=16)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=15)),
                ('nationality', models.CharField(blank=True, max_length=20)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('S', 'Single'), ('M', 'Married'), ('W', 'Widowed')], max_length=24)),
                ('address_1', models.CharField(blank=True, default='', max_length=255)),
                ('address_2', models.CharField(blank=True, default='', max_length=255)),
                ('country', models.CharField(default='Philippines', max_length=100)),
                ('contact_no', models.CharField(blank=True, default='', max_length=16)),
                ('is_guest', models.BooleanField(blank=True, default=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='cities', to='member.City')),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='provinces', to='member.Province')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership_id', models.CharField(blank=True, default='', max_length=50)),
                ('membership_date', models.DateField()),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='member.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.Province'),
        ),
    ]
