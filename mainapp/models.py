from django.db import models
from django.contrib.postgres.indexes import GinIndex

# 1. Category (Мужской портрер, Love Story)
# 2. PhotoCard (сама фотография)
# 3. TextBlock (текстовые блоки для сайта)
# 3. ImageBlock (картинки для сайта)


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class PhotoCard(models.Model):
    title = models.CharField(max_length=256, null=True)
    front_image = models.ImageField(upload_to='photo_front_img', blank=True)
    publication_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        indexes = [GinIndex(fields=['title'])]

    def __unicode__(self):
        return self.title

    def __str__(self):
        return f'{self.title}'


class TextBlock(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок блока', null=True)
    main_information = models.CharField(blank=True, max_length=512, verbose_name='Текст блока', default='')

    class Meta:
        verbose_name = '<Текстовый блок>'
        verbose_name_plural = 'Текстовые блоки'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return f'{self.title}'


class ImageBlock(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название фото', null=True)
    author_photo = models.ImageField(upload_to='photo', verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return f'{self.title}'
