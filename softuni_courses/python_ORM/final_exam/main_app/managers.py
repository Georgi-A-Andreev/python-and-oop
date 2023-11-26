from django.db import models


class CustomManager(models.Manager):
    def get_authors_by_article_count(self):
        return self.annotate(num_articles=Count())