from werkzeug.datastructures import FileStorage
import cloudinary
import cloudinary.uploader
import os


class CloudinaryHelper:
    def __init__(self):
        cloudinary.config(
            cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
            api_key=os.getenv('CLOUDINARY_API_KEY'),
            api_secret=os.getenv('CLOUDINARY_API_SECRET'),
            secure=True
        )

    def upload_image(
            self,
            image: FileStorage,
            folder: str = 'products'
        ) -> tuple[str, str] | None:
        try:
            response = cloudinary.uploader.upload(
                image,
                folder=folder
            )
            secure_url = response.get('secure_url')
            public_id = response.get('public_id')
            return secure_url, public_id
        except Exception as e:
            return None
        
    def delete_image(
        self,
        public_id: str
    ) -> bool:
        try:
            cloudinary.uploader.destroy(public_id)
            return True
        except Exception as e:
            return False
        
    def get_secure_url(
        self,
        public_id: str
    ) -> str:
        try:
            secure_url = cloudinary.utils.cloudinary_url(
                public_id,
                secure=True
            )
            return secure_url[0]
        except Exception as e:
            return None
        
cloudinary_helper = CloudinaryHelper()