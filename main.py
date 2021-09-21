
from import_library import *

# Programm starts here..
print("Present Working Directory")
main_dir = os.getcwd()
print(main_dir)
print("\n")

assets_dir = os.path.join(os.getcwd(), "Assets")
banana_dir = os.path.join(assets_dir, "banana")

extensions = ["jpeg", "jpg", "webp"]


def rename_files(directory):  # provide base directory of fruit folder

    os.chdir(directory)
    for idx, filename in enumerate(os.listdir(directory)):

        if os.path.isfile(filename):
            # file_name_tuple[0] -> filename without extension  ,  file_name_tuple[1] -> extention of the file
            filename_tuple = os.path.splitext(filename)
            # print(f"{filename_tuple} {idx}")

            newfilename = f"banana_{idx}{filename_tuple[1]}"
            os.rename(filename, newfilename)
            # if extension in filename:
            # print(filename)
    os.chdir(main_dir)


def resize_img(directory, dim=(100, 100)):  # provide base directory of fruit folder
    os.chdir(directory)
    file_index_not_open = []
    resized_img_folder_path = os.path.join(directory, 'resized_img')

    if (len(os.listdir(directory))-1) != len(os.listdir(resized_img_folder_path)):

        for idx, filename in enumerate(os.listdir(directory)):
            # print(filename)
            if os.path.isfile(filename):
                try:
                    img = cv.imread(filename=filename)
                    resized_img = cv.resize(
                        img, dim, interpolation=cv.INTER_AREA)
                    resized_img_file_path = os.path.join(
                        resized_img_folder_path, filename)
                    cv.imwrite(resized_img_file_path, resized_img)
                    cv.waitKey(0)
                    print(idx)
                except:
                    print("File Not Found!")
                    file_index_not_open.append(idx)

    print(len(file_index_not_open))

    os.chdir(main_dir)


def make_dataset(directory, save_filename):  # provide base directory of fruit folder

    resized_img_folder_path = os.path.join(directory, 'resized_img')
    dataset = []
    print("Changed dir to:", resized_img_folder_path)
    os.chdir(resized_img_folder_path)
    for idx, filename in enumerate(os.listdir(resized_img_folder_path)):
        if os.path.isfile(filename):
            try:
                img = cv.imread(filename=filename)
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                dataset.append(img)
                print(f"{filename} appended", img.shape)
            except:
                print("File Not Found!!")

    dataset = np.array(dataset)
    print(f"Final shape after making dataset", dataset.shape)
    os.chdir(main_dir)
    np.save(save_filename, dataset)
    print(f"Dataset Saved with filename {save_filename}")

    return dataset


# rename_files(banana_dir)
# resize_img(banana_dir)
# main_data = make_dataset(banana_dir,"banana.npy")

main_data = np.load("banana.npy")

# for i in range(3):
#     plt.hist(main_data[0, :, :, i].ravel(), bins=100)
# plt.xlim((0,255))
# plt.show()

def show_images(directory):    
    for filename in os.listdir(directory):
        if os.path.isfile(filename):
            path = directory + "/" + filename
            # im = Image.open(path)
            plt.imshow(path)
            plt.show()
            # plt.clf()
            # im.close()
            # time.sleep(5)
        
show_images(banana_dir)