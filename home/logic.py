def get_timestamp_path(instanse, filename):
    """
    Создает папку в MEDIA_ROOT с названием категории товара(если её там нет) 
    и сохраняет туда фото с именем (текущее время в секундах с начала эпохи)
    """
    from datetime import datetime
    import os
    from webcandlshop.settings import MEDIA_ROOT
    
    path_to_product = os.path.join(str(MEDIA_ROOT), instanse.category.slag)
    if os.path.exists(path_to_product):
         return os.path.join(path_to_product, f'{datetime.now().timestamp()}, {os.path.splitext(filename)[1]}')
    else:
        os.mkdir(path_to_product)
        return os.path.join(path_to_product, f'{datetime.now().timestamp()}, {os.path.splitext(filename)[1]}')