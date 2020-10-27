from django.db import models
import uuid
import accounts.models as acc_models
# Create your models here.


class CollectorEdition(models.Model):
    cid = models.UUIDField(default=uuid.uuid4,verbose_name='CID',primary_key=True,editable=False)
    name = models.CharField(max_length=50,verbose_name='name',unique=True)
    price = models.FloatField(default=1500.0,verbose_name="Price of Edition")
    no_of_content = models.IntegerField(default=0,verbose_name="Number of contents")
    date_of_creation = models.DateTimeField(verbose_name='date created', auto_now_add=True)
    uid = models.ForeignKey(acc_models.IndieUser,verbose_name='User ID',on_delete=models.CASCADE)
    game_name = models.CharField(max_length=50,verbose_name='Game Name')

    def __str__(self):
        return 'Game '+self.name+' owned by '+str(self.uid)


class Images(models.Model):
    img_id = models.UUIDField(default=uuid.uuid4,verbose_name='Image ID',primary_key=True,editable=False)
    cid = models.ManyToManyField(CollectorEdition,verbose_name="Collector's edition ID")
    url_thumbnail = models.URLField(verbose_name='Thumbnail URL')
    url_high_res = models.URLField(verbose_name='High Resolution URL')

    def __str__(self):
        used_names = [x.name for x in self.cid.all() ]
        return 'Image used by games: '+','.join(used_names)



class CollectorsEditionGenre(models.Model):
    cid = models.ManyToManyField(CollectorEdition,verbose_name="Collector's edition ID")
    genre_name = models.CharField(max_length=50,verbose_name='Genre Name')

    def __str__(self):
        return self.genre_name

