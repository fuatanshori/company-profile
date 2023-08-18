from django.core.exceptions import ValidationError

def validate_aspect_ratio_1920_900(image):
    if image.width != 1920 or image.height != 900:
        raise ValidationError("gambar harus memiliki dimensi 1920 x 900 kunjungi https://www.img2go.com/id/ubah-ukuran-gambar untuk merubah")
