# Generated by Django 3.2.8 on 2021-10-17 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(db_index=True, max_length=128)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('scene_name', models.CharField(db_index=True, max_length=128)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcp_backend.project')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(db_index=True, max_length=128, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Take',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('take_name', models.CharField(db_index=True, max_length=128)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('model_file', models.FileField(upload_to='vcp_models/')),
                ('audio_file', models.FileField(upload_to='vcp_audios/')),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcp_backend.scene')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcp_backend.user'),
        ),
        migrations.CreateModel(
            name='Capture',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('video_file', models.FileField(upload_to='vcp_videos/')),
                ('take', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vcp_backend.take')),
            ],
        ),
    ]