# Generated by Django 5.1.6 on 2025-03-14 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('llm', '0002_gemini2_delete_gemini'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGPT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('explain', models.TextField()),
                ('aiexplain', models.TextField()),
                ('file', models.FileField(upload_to='chatgpt/')),
                ('today', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
