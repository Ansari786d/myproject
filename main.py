import os


def createIfnotexist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(foldername, files):   # it moves the files in folder
    for file in files:
        os.replace(file, f"{foldername}/{file}")  # move this file into this folder name


if __name__ == "__main__":

    files = os.listdir()
    files.remove("main.py")
    
    
    print(files)

    createIfnotexist('Images')
    createIfnotexist('Docs')
    createIfnotexist('Media')
    createIfnotexist("others")

    imgExts = [".jpg", ".jpeg", ".png"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    # print(images)

    docExts = [".doc", ".txt", ".pdf", ".docx"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    # print(docs)


    mediaExt = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExt]
    # print(medias)

    others = []

    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExt) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    # print(others)

    move("Images", images)  # here folder name is Images and files name is images
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)
