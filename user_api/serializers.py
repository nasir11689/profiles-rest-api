from rest_framework import serializers
from . import models
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model  =models.UserLogin
        fields  =('id','email','name','password')
        extra_kwargs = {'password':{'write_only':True}}


    def create(self, validated_data):
        user = models.UserLogin(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserDetailsSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetails
        fields = ('id','user_id','first_name','last_name','address','phone_number','created_on')
        extra_kwargs = {'user_id':{'read_only':True}}

