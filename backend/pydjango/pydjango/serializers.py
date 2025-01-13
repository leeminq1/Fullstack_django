from rest_framework import serializers
from bson import ObjectId
from datetime import datetime


class MongoDataSerializer(serializers.Serializer):
    _id = serializers.CharField()  # ObjectId를 문자열로 변환
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")  # ISO 8601 형식
    hour = serializers.IntegerField()
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    smp = serializers.FloatField()

    def to_representation(self, instance):
        """
        MongoDB 데이터를 JSON 직렬화 가능 형식으로 변환.
        """
        data = super().to_representation(instance)

        # ObjectId 처리
        if isinstance(instance.get("_id"), ObjectId):
            data["_id"] = str(instance["_id"])

        # datetime 처리
        if isinstance(instance.get("date"), datetime):
            data["date"] = instance["date"].isoformat()

        return data
