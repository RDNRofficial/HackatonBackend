from django.db import models
from enum import Enum

class ListTypes(Enum):
    MATERIAL = "Material"
    EXECUTION = "Execution"
    EXPLANATION = "Explanation"

class Question(models.Model):
    """
    Describes a Question and its components, such as the background image and a voice over.

    Attributes
    ----------    
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
    Describes an answer, whether its correct and which question it belongs to. 

    Attributes
    ----------    
    before = models.ImageField(upload_to='images/answers/')
        visualized answer before clicking it
    after = models.ImageField(upload_to='images/answers/')
        visualized answer after clicking it
    solution = models.BooleanField()
        whether the answer is correct
    question = models.ForeignKey(Question, related_name='f_question', on_delete=models.CASCADE)
        question this answer belongs to
    x = models.DecimalField(max_digits=10, decimal_places=10)
        x position of the answer inside the background image
    y = models.DecimalField(max_digits=10, decimal_places=10)
        y position of the answer inside the background image
    size_before = models.DecimalField(max_digits=10, decimal_places=10)
        relative size of the before image in relation to the background image
    size_after = models.DecimalField(max_digits=10, decimal_places=10)
        relative size of the afet image in relation tp the background image
    """
    before = models.ImageField(upload_to='images/answers/')
    after = models.ImageField(upload_to='images/answers/')
    solution = models.BooleanField()
    question = models.ForeignKey(Question, related_name='f_question', on_delete=models.CASCADE)
    x = models.DecimalField(max_digits=10, decimal_places=10)
    y = models.DecimalField(max_digits=10, decimal_places=10)
    size_before = models.DecimalField(max_digits=10, decimal_places=10)
    size_after = models.DecimalField(max_digits=10, decimal_places=10)


class Userlevel(models.Model):
    """
    Describes the progress a user has made in the app.

    Attributes
    ----------
    score = models.IntegerField()
        score the user has archieved
    username = models.CharField(max_length=30 ,unique=True)
        unique username
    """
    level = models.IntegerField()
    username = models.CharField(max_length=30, unique=True)


class DIYManual(models.Model):
    """
    Describes a DIY Manual by its title and preview image.

    Attributes
    ----------
    title = models.CharField(max_length=100)
        name of the DIY manual
    title_image = models.ImageField(upload_to='images/diy/titles')
        preview image shown for selecting it in a list
    """
    title = models.CharField(max_length=200)
    title_image = models.ImageField(upload_to='images/diy/titles')

class DIYList(models.Model):
    diyType = models.CharField(choices=[(t.value,t.value) for t in ListTypes], max_length=200)
    title = models.CharField(max_length=200)
    manual = models.ForeignKey(
        DIYManual, related_name='diy_manual', on_delete=models.CASCADE)



class Explanation(models.Model):
    """
    Describes a step in a DIY Manual. Ech explanation consists of an image and an explanatory text.

    Attributes
    ----------
    image = models.ImageField(upload_to='images/diy/')
        visualisation of a step in the diy manual
    text = models.CharField(max_length=200)
        textual explanation of the image
    list = models.ForeignKey(DIYManual, related_name='diy_manual', on_delete=models.CASCADE)
        the DIY manual this explanation belongs to
    """
    image = models.ImageField(upload_to='images/diy/', null=True)
    text = models.CharField(max_length=200)
    diyList = models.ForeignKey(
        DIYList, related_name='diy_list', on_delete=models.CASCADE)
