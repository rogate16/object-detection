library(image.darknet)
yolo <- image_darknet_model(type = "detect", 
                            model = "tiny-yolo-voc.cfg", 
                            weights = system.file(package="image.darknet", "models", "tiny-yolo-voc.weights"), 
                            labels = system.file(package="image.darknet", "include", "darknet", "data", "voc.names"))