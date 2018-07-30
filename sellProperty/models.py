# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from Login.models import BaseModel
from django.contrib.auth.models import User

#create your property type.
class property_type(BaseModel):
    
    type_name = models.CharField(max_length=150,null=True,blank=True)
    description = models.CharField(max_length=150,null=True,blank=True)

class property_type_list(BaseModel):
    
    type_list = models.CharField(max_length=150,null=True,blank=True)  
    description = models.CharField(max_length=150,null=True,blank=True)
    type_id = models.ForeignKey(property_type,on_delete=models.CASCADE, null=True, blank=True)  
    
class area_unit_list(BaseModel):
    
    unit_name = models.CharField(max_length=150,null=True,blank=True)  
    description = models.CharField(max_length=150,null=True,blank=True)
    
class floor_plan_image(BaseModel):
    
    plan_image_path = models.TextField(null=True, blank=True)
    plan_image_format = models.CharField(max_length=150,null=True,blank=True)
    
class floor_plan_list(BaseModel):
    
    plan_image_path = models.ManyToManyField(floor_plan_image,on_delete=models.CASCADE, null=True, blank=True)  
    no_bathroom = models.IntegerField(default=0,null=True, blank=True)
    no_studyroom = models.IntegerField(default=0,null=True, blank=True)
    no_balcony = models.IntegerField(default=0,null=True, blank=True)
    no_servantroom = models.IntegerField(default=0,null=True, blank=True)
    no_poojaroom = models.IntegerField(default=0,null=True, blank=True)
    no_storeroom = models.IntegerField(default=0,null=True, blank=True)
    area_measure = models.FloatField(default=0,null=True, blank=True)
    area_unit = models.ForeignKey(area_unit_list,on_delete=models.CASCADE, blank=True, null=True)
    
class sell_property_image(BaseModel):
    
    property_image_name = models.CharField(max_length=150,null=True,blank=True)
    property_image_path = models.TextField(null=True, blank=True)
    property_image_format = models.CharField(max_length=150,null=True,blank=True)
    
class sell_property_video(BaseModel):
    
    property_video_name = models.CharField(max_length=150,null=True,blank=True)
    property_video_path = models.TextField(null=True, blank=True)
    property_video_format = models.CharField(max_length=150,null=True,blank=True)
    
# Create your models here.
class sell_property_info(BaseModel):
    
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    property_for = models.CharField(max_length=150, null=True, blank=True)
    sale_type = models.CharField(max_length=150, null=True, blank=True)
    property_type = models.ForeignKey(property_type_list,on_delete=models.CASCADE, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    project_name = models.CharField(max_length=150, null=True, blank=True)
    locality = models.CharField(max_length=150, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    configuration = models.CharField(max_length=150, null=True, blank=True)
    floor_plan = models.ForeignKey(floor_plan_list,on_delete=models.CASCADE, blank=True, null=True)
    super_built_up_area = models.FloatField(default=0,null=True, blank=True)
    super_built_up_area_unit = models.ForeignKey(area_unit_list,on_delete=models.CASCADE, blank=True, null=True)
    built_up_area = models.FloatField(default=0,null=True, blank=True)
    built_up_area_unit = models.ForeignKey(area_unit_list,on_delete=models.CASCADE, blank=True, null=True)
    carpet_area = models.FloatField(default=0,null=True, blank=True)
    carpet_area_unit = models.ForeignKey(area_unit_list,on_delete=models.CASCADE, blank=True, null=True)
    no_bathroom = models.IntegerField(default=0,null=True, blank=True)
    no_studyroom = models.IntegerField(default=0,null=True, blank=True)
    no_bedroom = models.IntegerField(default=0,null=True, blank=True)
    total_floor = models.IntegerField(default=0,null=True, blank=True)
    on_floor = models.CharField(max_length=150,null=True,blank=True)
    other_rooms = models.CharField(max_length=150,null=True,blank=True)
    reserverd_parking = models.CharField(max_length=150,null=True,blank=True)
    no_of_covered_parkings = models.IntegerField(default=0,null=True, blank=True)
    no_of_opened_parkings = models.IntegerField(default=0,null=True, blank=True)
    availability = models.CharField(max_length=150,null=True,blank=True)
    age_of_property = models.CharField(max_length=150,null=True,blank=True)
    ownership = models.CharField(max_length=150,null=True,blank=True)
    expected_price = models.FloatField(default=0,null=True, blank=True)
    price_per_sq_ft = models.FloatField(default=0,null=True, blank=True)
    maintenance = models.FloatField(default=0,null=True, blank=True)
    maintenance_period = models.CharField(max_length=150,null=True,blank=True)
    expected_rental = models.FloatField(default=0,null=True, blank=True)
    booking_amount = models.FloatField(default=0,null=True, blank=True)
    annual_dues_payable = models.FloatField(default=0,null=True, blank=True)
    membership_charge = models.FloatField(default=0,null=True, blank=True)
    booking_amount = models.FloatField(default=0,null=True, blank=True)
    property_image = models.ManyToManyField(sell_property_image,on_delete=models.CASCADE, null=True, blank=True)  
    property_video = models.ManyToManyField(sell_property_video,on_delete=models.CASCADE, null=True, blank=True)  
    tag_photo_location = models.CharField(max_length=150,null=True,blank=True)
    power_backup = models.CharField(max_length=150,null=True,blank=True)
    water_source = models.CharField(max_length=150,null=True,blank=True)
    overlooking = models.CharField(max_length=150,null=True,blank=True)
    facing = models.CharField(max_length=150,null=True,blank=True)
    facing_road_width = models.IntegerField(default=0,null=True, blank=True)
    facing_road_width_unit = models.CharField(max_length=150,null=True,blank=True)
    flooring_type = models.CharField(max_length=150,null=True,blank=True)
    furnishing = models.CharField(max_length=150,null=True,blank=True)
    description = models.TextField(null=True, blank=True)
    property_in = models.CharField(max_length=150,null=True,blank=True)