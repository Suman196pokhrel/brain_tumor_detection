from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


class DataGenerator:
     def __init__(self,src_img,src_dir,batch_size=1,prefx_name="AugData",saved_img_format="jpg",no_of_images=50):

          self.datagen = ImageDataGenerator(
            rotation_range=40,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,
            horizontal_flip=True,
            fill_mode='nearest')
          self.src_image = src_img
          self.src_dir = src_dir
          self.batch_size = batch_size
          self.perfix_name = prefx_name
          self.saved_img_format = saved_img_format
          self.no_of_img = no_of_images

          self.img_path = self.src_image
          self.img = load_img(self.img_path)

          self.x = img_to_array(self.img)
          self.x = self.x.reshape((1,) + self.x.shape)


          i =0
          for _ in self.datagen.flow(self.x, batch_size=1,save_to_dir=self.src_dir, save_prefix=self.perfix_name,save_format=self.saved_img_format):
               i +=1
               if i > self.no_of_img:
                    break

          


if __name__ == "__main__":
    DataGenerator(src_img=r"E:\Final_year_project\btd_final_project\mlModule\testData\test1.jpeg",
                         src_dir=r"E:\Final_year_project\btd_final_project\mlModule\augumentedImages",
                         no_of_images=10)
