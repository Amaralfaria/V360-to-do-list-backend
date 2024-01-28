from django.db import models
# from list.models import User

class List(models.Model):
    list_name = models.CharField(max_length=30)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user_fk',null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['list_name','user'], name='list_user_unique')
        ]
        

    def __str__(self):
        return self.list_name
    
class ListItem(models.Model):
    item_name = models.CharField(max_length=30)
    description = models.TextField()
    done = models.BooleanField(default=False)
    due_date = models.DateField(null=True)
    list = models.ForeignKey(List, on_delete=models.CASCADE,related_name='list_fk',null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['item_name','description'], name='name_list_unique')
        ]

    def __str__(self):
        return self.item_name


