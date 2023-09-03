def get_data_or_none(model):
    try:
        return model.objects.get(is_active=True)
    except model.DoesNotExist:
        return None