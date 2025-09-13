from PIL import Image
import pytesseract, argparse
def main(path):
    print(pytesseract.image_to_string(Image.open(path)))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--input', default='ocr/tests/sample.jpg')
    args=p.parse_args()
    main(args.input)
