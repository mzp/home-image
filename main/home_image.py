from google.appengine.api import images


class Spec(object):
    def __init__(self, count, margin):
        self.count = count
        self.margin = margin

class HomeImage(object):
    def __init__(self,width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def image_width(self):
        return (self.width * self.x.count +
                self.x.margin * (self.x.count - 1))

    def image_height(self):
        return (self.height * self.y.count +
                self.y.margin * (self.y.count - 1))

    def split(self, image):
        self.__resize(image)
        return self.__split(image)

    def __resize(self,image):
        image.resize(self.image_width(),
                     self.image_height())

    def __split(self,image):
        data = image.execute_transforms(output_encoding=images.PNG)
        imgs = []
        for x in xrange(0,self.x.count):
            for y in xrange(0,self.y.count):
                img = images.Image(data)
                img.crop(x * (1.0 / self.x.count),
                         y * (1.0 / self.y.count),
                         ( x + 1 ) * (1.0 / self.x.count),
                         ( y + 1 ) * (1.0 / self.y.count))
                imgs.append(img)
        return imgs



if __name__ == '__main__':
    HomeImage = HomeImage(54,54,
                          Spec(4,0),
                          Spec(4,0))

    with open('miku.jpg', 'r') as f:
        data = f.read()
        img =  HomeImage.split(images.Image(data))
        thumbnail = img.execute_transforms(output_encoding=images.PNG)
        print thumbnail
