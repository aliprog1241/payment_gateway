from django.db import models

class Package(models.Model):
    title = models.CharField(max_length=48)
    price = models.PositiveBigIntegerField()
    description = models.TextField(blank=True)
    days = models.PositiveSmallIntegerField()
    is_enabled = models.BooleanField(default=True)

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PackageAttribute(models.Model):
    package = models.ForeignKey(Package, related_name='attribute',on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title