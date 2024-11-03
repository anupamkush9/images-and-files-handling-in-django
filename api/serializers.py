from rest_framework import serializers
from api.models import Profile
from django.core.exceptions import ValidationError

def validate_file_size(value):
  filesize = value.size # returns the file size in byte

  if filesize > 1048576:  # 1MB limit
      raise ValidationError(f"The maximum file size that can be uploaded is 1048576 bytes but your file size is {filesize} bytes")
  return value

class ProfileSerializer(serializers.ModelSerializer):
  rdoc = serializers.FileField(validators=[validate_file_size])

  class Meta:
    model=Profile
    fields = ['id', 'name', 'email', 'dob', 'state', 'gender', 'location', 'pimage', 'rdoc']