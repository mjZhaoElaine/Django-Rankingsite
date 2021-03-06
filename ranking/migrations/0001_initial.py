# Generated by Django 2.1.4 on 2018-12-19 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CWURank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorldRank', models.IntegerField()),
                ('UnivName', models.CharField(max_length=70)),
                ('Country', models.CharField(max_length=24)),
                ('NationRank', models.IntegerField()),
                ('EducationRank', models.IntegerField()),
                ('EmploymentRank', models.IntegerField()),
                ('FacultyRank', models.IntegerField()),
                ('PublicationRank', models.IntegerField()),
                ('InfluenceRank', models.IntegerField()),
                ('CitationRank', models.IntegerField()),
                ('PatentRank', models.IntegerField()),
                ('TotalScore', models.DecimalField(decimal_places=2, max_digits=5)),
                ('RankYear', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SHJTRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorldRank', models.IntegerField()),
                ('UnivName', models.CharField(max_length=61)),
                ('Country', models.CharField(max_length=24)),
                ('NationRank', models.IntegerField()),
                ('TotalScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('AlumniScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('AwardScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('HICIScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('NSScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('PUBScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('PCPScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('RankYear', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TimesRank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorldRank', models.IntegerField()),
                ('UnivName', models.CharField(max_length=58)),
                ('Country', models.CharField(max_length=24)),
                ('TeachScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('InterScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('ResearchScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('CitationScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('IncomeScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('TotalScore', models.DecimalField(decimal_places=1, max_digits=4)),
                ('NumStudents', models.IntegerField()),
                ('StudentStaffRatio', models.DecimalField(decimal_places=1, max_digits=4)),
                ('InterStudentRatio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('RankYear', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Univ2Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UnivName', models.CharField(max_length=66)),
                ('Country', models.CharField(max_length=24)),
            ],
        ),
    ]
