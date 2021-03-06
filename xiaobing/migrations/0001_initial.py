# Generated by Django 2.1.5 on 2019-01-15 14:03

from django.db import migrations, models
import djangoUeditor.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeId', models.CharField(blank=True, max_length=100, null=True)),
                ('isShow', models.CharField(blank=True, max_length=10, null=True)),
                ('isShowOrder', models.CharField(blank=True, max_length=10, null=True)),
                ('orderId', models.CharField(blank=True, max_length=100, null=True)),
                ('orderName', djangoUeditor.models.UEditorField(blank=True, verbose_name='指令名称')),
                ('orderDescription', djangoUeditor.models.UEditorField(default='test', verbose_name='指令说明')),
                ('typeDescription', djangoUeditor.models.UEditorField(default='test', verbose_name='类型说明')),
                ('createTime', models.DateTimeField()),
                ('number', models.IntegerField()),
            ],
            options={
                'ordering': ('-createTime',),
            },
        ),
        migrations.CreateModel(
            name='OrderType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeId', models.CharField(blank=True, max_length=100, null=True)),
                ('typeName', djangoUeditor.models.UEditorField(default='test', verbose_name='类型名称')),
                ('createTime', models.DateTimeField()),
                ('number', models.IntegerField()),
            ],
            options={
                'ordering': ('number', '-createTime'),
            },
        ),
    ]
