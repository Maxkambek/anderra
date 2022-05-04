from django.db import models

TYPE=(
    (0,'Fashion'),
    (1,'Travel'),
)


class Category(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tags=models.CharField(max_length=50)

    def __str__(self):
        return self.tags


def post_image_path(instance,filename):
    return 'posts/%s/%s' % (instance.type,filename)


class Post(models.Model):
    title=models.CharField(max_length=222)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    type=models.IntegerField(choices=TYPE)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to=post_image_path)
    tag=models.ManyToManyField(Tag,blank=True)
    slug=models.SlugField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name=models.CharField(max_length=50)
    avatar=models.ImageField(upload_to='comments',null=True,blank=True)
    email=models.EmailField()
    website=models.URLField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    message=models.TextField()

    def __str__(self):
        return self.name
