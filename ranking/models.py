from django.db import models

# Create your models here.
class TimesRank(models.Model):
    WorldRank = models.IntegerField()
    UnivName = models.CharField(max_length=58)
    Country = models.CharField(max_length=24, null=True)
    TeachScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    InterScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    ResearchScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    CitationScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    IncomeScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    TotalScore = models.DecimalField(decimal_places=1 ,max_digits=4)
    NumStudents = models.IntegerField(null=True)
    StudentStaffRatio = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    InterStudentRatio = models.DecimalField(decimal_places=2 ,max_digits=4, null=True)
    RankYear = models.IntegerField()

class CWURank(models.Model):
    WorldRank = models.IntegerField()
    UnivName = models.CharField(max_length=70)
    Country = models.CharField(max_length=24, null=True)
    NationRank = models.IntegerField(null=True)
    EducationRank = models.IntegerField(null=True)
    EmploymentRank = models.IntegerField(null=True)
    FacultyRank = models.IntegerField(null=True)
    PublicationRank = models.IntegerField(null=True)
    InfluenceRank = models.IntegerField(null=True)
    CitationRank = models.IntegerField(null=True)
    PatentRank = models.IntegerField(null=True)
    TotalScore = models.DecimalField(decimal_places=2 ,max_digits=5)
    RankYear = models.IntegerField()

class SHJTRank(models.Model):
    WorldRank = models.IntegerField()
    UnivName = models.CharField(max_length=61)
    Country = models.CharField(max_length=24, null=True)
    NationRank = models.IntegerField(null=True)
    TotalScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    AlumniScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    AwardScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    HICIScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    NSScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    PUBScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    PCPScore = models.DecimalField(decimal_places=1 ,max_digits=4, null=True)
    RankYear = models.IntegerField()

class Univ2Country(models.Model):
    UnivName = models.CharField(max_length=66)
    Country = models.CharField(max_length=24)
