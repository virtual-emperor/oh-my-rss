# Generated by Django 2.2 on 2019-08-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='uindex',
            field=models.IntegerField(db_index=True, unique=True, verbose_name='唯一地址'),
        ),
        migrations.AlterField(
            model_name='site',
            name='author',
            field=models.CharField(max_length=100, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='site',
            name='cname',
            field=models.CharField(max_length=100, verbose_name='站点名称'),
        ),
        migrations.AlterField(
            model_name='site',
            name='favicon',
            field=models.CharField(default='', max_length=100, verbose_name='favicon'),
        ),
        migrations.AlterField(
            model_name='site',
            name='link',
            field=models.CharField(max_length=200, verbose_name='站点主页'),
        ),
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True, verbose_name='scrapy代号'),
        ),
        migrations.AlterField(
            model_name='site',
            name='status',
            field=models.CharField(choices=[('active', '激活'), ('close', '关闭，下线')], default='active', max_length=20, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='site',
            name='tag',
            field=models.CharField(choices=[('前端', '前端'), ('客户端', '客户端'), ('后端', '后端'), ('全栈', '全栈'), ('产品', '产品'), ('安全', '安全'), ('设计', '设计'), ('测试', '测试'), ('刊物', '刊物'), ('算法', '算法'), ('大数据', '大数据')], max_length=20, null=True, verbose_name='一个词形容'),
        ),
    ]