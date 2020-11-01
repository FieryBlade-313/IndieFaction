from django.db import models
import uuid
import accounts.models as acc_models
# Create your models here.


class Images(models.Model):
    img_id = models.UUIDField(
        default=uuid.uuid4, verbose_name='Image ID', primary_key=True, editable=False)
    url_thumbnail = models.URLField(verbose_name='Thumbnail URL')
    url_high_res = models.URLField(verbose_name='High Resolution URL')

    def __str__(self):
        return self.url_thumbnail


class CollectorsEditionGenre(models.Model):
    genre_name = models.CharField(max_length=50, verbose_name='Genre Name')

    def __str__(self):
        return self.genre_name


class CollectorEdition(models.Model):
    cid = models.UUIDField(
        default=uuid.uuid4, verbose_name='CID', primary_key=True, editable=False)
    name = models.CharField(max_length=50, verbose_name='name', unique=True)
    price = models.FloatField(default=1500.0, verbose_name="Price of Edition")
    no_of_content = models.IntegerField(
        default=0, verbose_name="Number of contents")
    date_of_creation = models.DateTimeField(
        verbose_name='date created', auto_now_add=True)
    uid = models.ForeignKey(acc_models.IndieUser,
                            verbose_name='User ID', on_delete=models.CASCADE)
    game_name = models.CharField(max_length=50, verbose_name='Game Name')
    images = models.ManyToManyField(Images, verbose_name="Images")
    genre = models.ManyToManyField(
        CollectorsEditionGenre, verbose_name="Genre")

    def __str__(self):
        return 'Game '+self.name+' owned by '+str(self.uid)
