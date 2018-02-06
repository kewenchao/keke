import time

from rest_framework import serializers

from .models import User

import uuid

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('user', 'phone', 'birthday', 'sex', 'idnumber', 'address', 'recordate', 'insurancedate', 'cartype',
        #           'caridentnumber', 'engineno', 'carno',
        #           'carlable', )

        fields = serializers.ALL_FIELDS