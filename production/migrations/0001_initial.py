# Generated by Django 2.2.5 on 2019-12-27 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('dPrice', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('eName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('eNum', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Firm',
            fields=[
                ('FirmID', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('fName', models.CharField(max_length=20)),
                ('Tele', models.CharField(max_length=10)),
                ('Address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Made',
            fields=[
                ('mID', models.PositiveIntegerField()),
                ('mTime', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('mNum', models.PositiveIntegerField()),
                ('mDish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Dish')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('MemberID', models.AutoField(primary_key=True, serialize=False)),
                ('mName', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=10)),
                ('Phone', models.CharField(max_length=13)),
                ('Email', models.EmailField(blank=True, max_length=100)),
                ('BDay', models.DateField()),
                ('Pets', models.BooleanField(default=True)),
                ('Student', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProvideStock',
            fields=[
                ('psTime', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('psNum', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('sName', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('sNum', models.PositiveIntegerField()),
                ('Expired', models.DateField()),
                ('dish', models.ManyToManyField(through='production.Made', to='production.Dish')),
                ('firm', models.ManyToManyField(through='production.ProvideStock', to='production.Firm')),
            ],
        ),
        migrations.AddField(
            model_name='providestock',
            name='pStock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Stock'),
        ),
        migrations.AddField(
            model_name='providestock',
            name='psFirm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Firm'),
        ),
        migrations.CreateModel(
            name='ProvideEquip',
            fields=[
                ('peTime', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('peNum', models.PositiveIntegerField()),
                ('pEquip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Equipment')),
                ('peFirm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Firm')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('oID', models.AutoField(primary_key=True, serialize=False)),
                ('oTime', models.DateTimeField(auto_now_add=True)),
                ('orderNum', models.PositiveIntegerField()),
                ('MID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Member')),
                ('dishName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Dish')),
            ],
        ),
        migrations.AddField(
            model_name='made',
            name='mStock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.Stock'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='firm',
            field=models.ManyToManyField(through='production.ProvideEquip', to='production.Firm'),
        ),
        migrations.AddField(
            model_name='dish',
            name='Mid',
            field=models.ManyToManyField(through='production.Order', to='production.Member'),
        ),
    ]
