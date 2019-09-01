from django.db import models


class Example(models.Model):

    number = models.IntegerField("number", null=True, blank=True)
    short_text = models.CharField("char", max_length=30, blank=True)
    long_text = models.TextField("text", blank=True)
    some_date = models.DateField("some date", null=True, blank=True)
    boolean = models.BooleanField("true or false", default=False)

    class Meta:
        verbose_name = "example"
        verbose_name_plural = "examples"

    def __str__(self):
        return f"{self.id}"
