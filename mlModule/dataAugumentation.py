from keras.backend import softplus
import PIL
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


class CreateData:
     def __init__(self,
     sourc_image,
     destination_dir_name,
     rotation_range=40,
     width_shift_range=0.2,
     height_shift_range=0.2,
     shear_range= 0.2,
     zoom_range= 0.2,
     horizontal_flip=True,
     fill_mode='nearest'
     ):

          # Required 
          self.source_image = sourc_image
          self.destination_dir_name = destination_dir_name
          print(f"The source path is  {self.source_image}\n")
          


          self.datagen = ImageDataGenerator(
            rotation_range= rotation_range,
            width_shift_range= width_shift_range,
            height_shift_range= height_shift_range,
            shear_range= shear_range,
            zoom_range= zoom_range,
            horizontal_flip= horizontal_flip,
            fill_mode=fill_mode
            )

          # reshaping Image 
          img_path = self.source_image
          img = load_img(img_path)
          self.x = img_to_array(img)
          self.x = self.x.reshape((1,) + self.x.shape)

     def generate_data(self,batch_size=1,number_of_images=50,name_prefix="testImg",image_format="jpg"):
          self.batch_size = batch_size
          self.number_of_images = number_of_images
          self.name_prefix = name_prefix
          self.image_format = image_format

          i = 0
          for batch in self.datagen.flow(self.x, batch_size=self.batch_size,save_to_dir=self.destination_dir_name, save_prefix=self.name_prefix,save_format=image_format):
               i +=1
               if i > self.number_of_images:
                    break



if __name__ == "__main__":
     obj = CreateData(
          sourc_image=r"C:\Users\Suman pokhrel\OneDrive\Desktop\Final_Year_Project\btdCode\testData\test1.jpg",
          destination_dir_name="abc"
          )
     obj.generate_data()
          
