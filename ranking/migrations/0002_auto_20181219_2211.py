# Generated by Django 2.1.4 on 2018-12-19 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cwurank',
            name='CitationRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='Country',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='EducationRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='EmploymentRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='FacultyRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='InfluenceRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='NationRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='PatentRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cwurank',
            name='PublicationRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='AlumniScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='AwardScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='Country',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='HICIScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='NSScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='NationRank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='PCPScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='PUBScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='shjtrank',
            name='TotalScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='CitationScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='Country',
            field=models.CharField(max_length=24, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='IncomeScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='InterScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='InterStudentRatio',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='NumStudents',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='ResearchScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='StudentStaffRatio',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesrank',
            name='TeachScore',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
    ]
