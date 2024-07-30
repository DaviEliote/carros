from django.db.models.signals import post_save,post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Sum
from cars.models import Car,carinvetory
# from openai_api.client import get_car_ai_bio



def car_invetory_update():
    cars_count= Car.objects.all().count()
    cars_value= Car.objects.aggregate(
        total_value= Sum('value')
    )['total_value']

    carinvetory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )




# @receiver(pre_save, sender=Car)
# def car_pre_save(sender,instance, **kwargs):
#     if not instance.bio:
#         ai_bio= get_car_ai_bio(
#              instance.model,
#              instance.factory_year,
#             instance.brand
#         )
#         instance.bio=ai_bio








@receiver(post_save,sender=Car)
def func_post_save(sender,instance,**kwargs):
    car_invetory_update()



@receiver(post_delete,sender=Car)
def func_post_delete(sender,instance,**kwargs):
    car_invetory_update()