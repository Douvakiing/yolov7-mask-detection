import xml.etree.ElementTree as ET
import os


def convert_bbox(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x_center = (box[0] + box[1]) / 2.0 - 1
    y_center = (box[2] + box[3]) / 2.0 - 1
    width = box[1] - box[0]
    height = box[3] - box[2]
    x_center = x_center * dw
    width = width * dw
    y_center = y_center * dh
    height = height * dh
    return (x_center, y_center, width, height)


def convert_annotation(image_id, classes, input_dir, output_dir):
    in_file = open(f"{input_dir}/{image_id}.xml")
    out_file = open(f"{output_dir}/{image_id}.txt", "w")
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    for obj in root.iter("object"):
        difficult = obj.find("difficult").text
        cls = obj.find("name").text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find("bndbox")
        b = (
            float(xmlbox.find("xmin").text),
            float(xmlbox.find("xmax").text),
            float(xmlbox.find("ymin").text),
            float(xmlbox.find("ymax").text),
        )
        bbox = convert_bbox((w, h), b)
        out_file.write(f"{cls_id} " + " ".join([f"{a:.6f}" for a in bbox]) + "\n")


if __name__ == "__main__":
    classes = [
        "without_mask",
        "with_mask",
        "mask_weared_incorrect",
    ]  # Replace with your classes
    input_dir = "dataset/annotations/"
    output_dir = "dataset/annotations2/"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_ids = [f.split(".")[0] for f in os.listdir(input_dir) if f.endswith(".xml")]
    for image_id in image_ids:
        convert_annotation(image_id, classes, input_dir, output_dir)
