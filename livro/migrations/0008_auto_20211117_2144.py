# Generated by Django 3.2.9 on 2021-11-18 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('livro', '0007_auto_20211117_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='emprestimos',
            name='nome_emprestado_anonimo',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='nome_emprestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario'),
        ),
    ]
