from django.db import models

class Question(models.Model):
    """
    question = models.CharField(max_length=100)
        the actual textual question
    background = models.ImageField(upload_to='images/background/')
        background image for the specific question
    audio = models.FileField(upload_to='audio/')
        read aloud question
    score = models.IntegerField()
        amount of points received on correct answers
    """
    question = models.CharField(max_length=100)
    background = models.ImageField(upload_to='images/background/')
    audio = models.FileField(upload_to='audio/')
    level = models.IntegerField()


class Answer(models.Model):
    """
    before = models.ImageField(upload_to='images/answers/')
        visualized answer before clicking it
    after = models.ImageField(upload_to='images/answers/')
        visualized answer after clicking it
    solution = models.BooleanField()
        whether the answer is correct
    question = models.ForeignKey(Question, related_name='f_question', on_delete=models.CASCADE)
        question this answer belongs to
    x = models.IntegerField()
        x position of the answer inside the background image
    y = models.IntegerField()
        y position of the answer inside the background image
    """
    before = models.ImageField(upload_to='images/answers/')
    after = models.ImageField(upload_to='images/answers/')
    solution = models.BooleanField()
    question = models.ForeignKey(Question, related_name='f_question', on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()

class Userlevel(models.Model):
    """
    score = models.IntegerField()
        score the user has archieved
    username = models.CharField(max_length=30 ,unique=True)
        unique username
    """
    level = models.IntegerField()
    username = models.CharField(max_length=30 ,unique=True)

class DIYManual(models.Model):
    """
    title = models.CharField(max_length=100)
        name of the DIY manual
    title_image = models.ImageField(upload_to='images/diy/titles')
        preview image shown for selecting it in a list
    """
    title = models.CharField(max_length=100)
    title_image = models.ImageField(upload_to='images/diy/titles')

class Explanation(models.Model):
    """
    image = models.ImageField(upload_to='images/diy/')
        visualisation of a step in the diy manual
    text = models.CharField(max_length=200)
        textual explanation of the image
    manual = models.ForeignKey(DIYManual, related_name='diy_manual', on_delete=models.CASCADE)
        the DIY manual this explanation belongs to
    """
    image = models.ImageField(upload_to='images/diy/')
    text = models.CharField(max_length=200)
    manual = models.ForeignKey(DIYManual, related_name='diy_manual', on_delete=models.CASCADE)