import numpy as np
import requests
from PIL import Image
from io import BytesIO
import cv2
import requests
import io
from PIL import Image
import cv2
import requests
import numpy as np
from PIL import Image
import io

async def improve_image_quality_with_api(url, session):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            image_data = await response.read()

        # Используем OpenCV для улучшения качества
        img_array = np.asarray(bytearray(image_data), dtype=np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

        # Преобразование OpenCV изображения обратно в PIL Image
        enhanced_pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Сохранение PIL изображения в байтовый массив
        img_byte_array = io.BytesIO()
        enhanced_pil_image.save(img_byte_array, format='JPEG')
        img_byte_array = img_byte_array.getvalue()

        # Загрузка улучшенного изображения на imgbb и получение URL
        api_key = "283ec90df5005330d588c090c682a787"
        async with session.post(
            "https://api.imgbb.com/1/upload",
            data={"key": api_key},
            files={"image": img_byte_array}
        ) as response:
            result_data = await response.json()

        improved_url = result_data.get("data", {}).get("url")
        return improved_url

    except Exception as e:
        print(f"An error occurred: {e}")
        return None