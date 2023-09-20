def delete_old_image(instance, filename):
    """
    Deletes old image
    """    
    from .models import BannerImage
    from .models import LogoImage
    # If an old image exists, delete it before saving the new one
    banner_instance = BannerImage.objects.last()
    logo_instance = LogoImage.objects.last()
    image_dir = ""
    
    if isinstance(instance, BannerImage):
        image_dir = "banner"
    else:
        image_dir = "logo"
            
    if banner_instance:
        if banner_instance.cover_image and banner_instance.cover_image != instance.cover_image:
            banner_instance.cover_image.delete(save=False)
            banner_instance.save()
    if logo_instance:
        if logo_instance.logo_image and logo_instance.logo_image != instance.logo_image:
            logo_instance.logo_image.delete(save=False)
            logo_instance.save()
    return f"static/images/{image_dir}/" + filename
