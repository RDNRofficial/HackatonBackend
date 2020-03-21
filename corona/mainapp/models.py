from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)
    background = models.ImageField(upload_to='images/background/')
    audio = models.FileField(upload_to='audio/')
    score = models.IntegerField()


class Answer(models.Model):
    before = models.ImageField(upload_to='images/answers/')
    after = models.ImageField(upload_to='images/answers/')
    solution = models.BooleanField()
    question = models.ForeignKey(Question, related_name='f_question', on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()

class Userscore(models.Model):
    score = models.IntegerField()
    username = models.CharField(max_length=30 ,unique=True)

class DIYManual(models.Model):
    title = models.CharField(max_length=100)
    title_image = models.ImageField(upload_to='images/diy/titles')

class Explanation(models.Model):
    image = models.ImageField(upload_to='images/diy/')
    text = models.CharField(max_length=200)
    manual = models.ForeignKey(DIYManual, related_name='diy_manual', on_delete=models.CASCADE)