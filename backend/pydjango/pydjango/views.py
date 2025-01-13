from pymongo import MongoClient
from django.http import JsonResponse
from decouple import config
from .serializers import MongoDataSerializer

# MongoDB URI 가져오기
MONGO_URI = config("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["local"]
collection = db["smp_actual"]


def get_data(request):
    # MongoDB에서 데이터 가져오기
    data = collection.find_one({"year": 2021})
    print(data)

    if data:
        # MongoDataSerializer로 데이터 직렬화
        serializer = MongoDataSerializer(data)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({"message": "No data found"}, status=404)
