from django.db import models


class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Belonging(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Borrowed(models.Model):
    what = models.ForeignKey(Belonging, on_delete=models.CASCADE)
    to_who = models.ForeignKey(Friend, on_delete=models.CASCADE)
    when = models.DateField(auto_now=True)
    returned = models.DateField(blank=True,  null=True)

    def __str__(self):
        return f"{self.what} to {self.to_who} at {self.when}"
