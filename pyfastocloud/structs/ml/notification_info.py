from pyfastogt.maker import Maker


class Rect:
    x = 0
    y = 0
    width = 0
    height = 0


class ImageBox(Maker):
    UNIQUE_COMPONENT_ID = 'unique_component_id'
    CLASS_ID_FIELD = 'class_id'
    CONFIDENCE_FIELD = 'confidence'
    OBJECT_ID_FIELD = 'object_id'
    # rect
    LEFT_FIELD = 'left'
    TOP_FIELD = 'top'
    WIDTH_FIELD = 'width'
    HEIGHT_FIELD = 'height'

    def __init__(self):
        self.unique_component_id = 0
        self.class_id = 0
        self.object_id = 0
        self.confidence = 0.0
        self.rect = Rect()

    def update_entry(self, json: dict):
        Maker.update_entry(self, json)

        res, unique_component_id = self.check_required_type(ImageBox.UNIQUE_COMPONENT_ID, int, json)
        if res:
            self.unique_component_id = unique_component_id

        res, class_id = self.check_required_type(ImageBox.CLASS_ID_FIELD, int, json)
        if res:
            self.class_id = class_id

        res, object_id = self.check_required_type(ImageBox.OBJECT_ID_FIELD, int, json)
        if res:
            self.object_id = object_id

        res, confidence = self.check_required_type(ImageBox.CONFIDENCE_FIELD, float, json)
        if res:
            self.confidence = confidence

        res, left = self.check_required_type(ImageBox.LEFT_FIELD, int, json)
        if res:
            self.rect.x = left

        res, top = self.check_required_type(ImageBox.TOP_FIELD, int, json)
        if res:
            self.rect.y = top

        res, width = self.check_required_type(ImageBox.WIDTH_FIELD, int, json)
        if res:
            self.rect.width = width

        res, height = self.check_required_type(ImageBox.HEIGHT_FIELD, int, json)
        if res:
            self.rect.height = height


class NotificationInfo(Maker):
    ID_FIELD = 'id'
    IMAGES_FIELD = 'images'

    def __init__(self):
        self._sid = None
        self._images = []

    def update_entry(self, json: dict):
        Maker.update_entry(self, json)

        res, sid = self.check_required_type(NotificationInfo.ID_FIELD, str, json)
        if res:
            self._sid = sid

        res, images = self.check_required_type(NotificationInfo.IMAGES_FIELD, list, json)
        if res:
            result = []
            for image in images:
                result.append(ImageBox.make_entry(image))

            self._images = result
