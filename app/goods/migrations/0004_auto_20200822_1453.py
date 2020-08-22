# Generated by Django 3.1 on 2020-08-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_auto_20200822_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='allergy',
            field=models.CharField(max_length=512, null=True, verbose_name='알레르기 정보'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='each',
            field=models.CharField(max_length=64, null=True, verbose_name='판매 단위'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='expiration',
            field=models.CharField(max_length=512, null=True, verbose_name='유통기한'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='packing',
            field=models.CharField(max_length=128, null=True, verbose_name='포장 타입'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='short_desc',
            field=models.CharField(max_length=100, verbose_name='간단 설명'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='transfer',
            field=models.CharField(max_length=64, null=True, verbose_name='배송 구분'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='weight',
            field=models.CharField(max_length=64, null=True, verbose_name='중량/용량'),
        ),
    ]
