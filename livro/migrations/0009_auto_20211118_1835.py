# Generated by Django 3.2.9 on 2021-11-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0008_auto_20211117_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
