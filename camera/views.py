from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'camera/index.html')


import base64
import cv2
import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def detect(request):
    if request.method == 'POST':
        data = request.json()
        image_data = data.get('image')
        if image_data:
            # Decode the image from base64
            header, image_data = image_data.split(',', 1)
            img = base64.b64decode(image_data)
            np_arr = np.frombuffer(img, np.uint8)
            img_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Perform object detection (this is a placeholder)
            detection_text = "Detected Object 1, Object 2"

            return JsonResponse({"detection_text": detection_text})

    return JsonResponse({"error": "Invalid request"}, status=400)
