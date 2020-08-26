from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from wb_api.settings import MEDIA_ROOT



class Tag(models.Model):
    name = models.CharField('Название тега', max_length=120, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False, db_index=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

class Post(models.Model):
    tags = models.ManyToManyField(Tag, verbose_name='Теги', related_name='tags')
    name = models.CharField('Название статьи', max_length=120, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False, db_index=True)
    image = models.ImageField('Изображение превью 290х140)', upload_to='post/', blank=False, null=True)
    image_post = models.ImageField('Изображение в шапке статьи 850х500)', upload_to='post/', blank=False, null=True)
    title = models.CharField('TITLE', max_length=120, blank=True, null=True)
    description = models.TextField('DESCRIPTION', blank=True, null=True)
    short_description = models.TextField('Короткое описание', blank=False, null=True)
    text = RichTextUploadingField('Статья.', blank=False, null=True)
    views = models.IntegerField('Просмотров', default=0)
    is_active = models.BooleanField('Отображать статью ?', default=True, db_index=True)
    created_at = models.DateTimeField('Создана', auto_now_add=True)

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return ''

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/blog/{self.name_slug}'

    def __str__(self):
        return f'id: {self.id} | Статья : {self.name}'


class BlackListType(models.Model):
    name = models.CharField('Тип', max_length=120, blank=False, null=True)

    def __str__(self):
        return self.name

class BlackListItem(models.Model):
    image = models.ImageField('Изображение превью 330x260)', upload_to='bl/', blank=False, null=True)

    type = models.ForeignKey(BlackListType,on_delete=models.CASCADE,verbose_name='Тип',blank=False,null=True )
    name = models.CharField('Название', max_length=255, blank=False, null=True)
    name_slug = models.CharField(max_length=255, blank=True, null=True, editable=False, db_index=True)
    reason = models.CharField('Причина', max_length=255, blank=False, null=True)
    contact = models.CharField('Контакты', max_length=255, blank=False, null=True)

    details = RichTextUploadingField('Детали.', blank=False, null=True)
    proofs = RichTextUploadingField('Доказаьельства.', blank=False, null=True)

    created_at = models.DateTimeField('Создана', auto_now_add=True,null=True)

    def save(self, *args, **kwargs):
        self.name_slug = slugify(self.name)
        super(BlackListItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

