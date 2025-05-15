from rest_framework import serializers
from .models import Map

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ['id', 'name', 'layout', 'public', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at']

    def validate_layout(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Layout must be a list")
        for row in value:
            if not isinstance(row, list):
                raise serializers.ValidationError("Each row must be a list")
            for cell in row:
                if cell not in ['R', '#']:
                    raise serializers.ValidationError("Cells must be 'R' or '#'")
        return value