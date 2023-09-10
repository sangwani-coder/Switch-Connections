def delete_old_image(instance, filename):
        from .models import BrandImages
        # If an old image exists, delete it before saving the new one
        if instance.pk:
            old_instance = BrandImages.objects.get(pk=instance.pk)
            if old_instance.cover_image and old_instance.cover_image != instance.cover_image:
                old_instance.cover_image.delete(save=False)
            if old_instance.logo_image and old_instance.logo_image != instance.logo_image:
                old_instance.logo_image.delete(save=False)
        return filename
    
    
    