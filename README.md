# linoleumBlocks

Python scripts for producing artistic image transformations

## V1

Requires imagemagick, lxml, PIL, OpenCV, numpy, matplotlib and potrace. And batik (how could I forget it?).  Too much, I know.  Later versions will almost certainly require lxml, potrace and batik (I like the convenience of manipulating SVG), although I hope to settle on one image processing library (OpenCV, most likely).

USAGE: ./linoleumBlocksV1.py pathToInputImage pathToConfig

Config files contain an elaborate python dictionary specifying how the input image should be transformed.  

To run the script using the sample images and configs:

> ./linoleumBlocksV1.py images/1024px-Osteospermum_lemon_symphony.jpg config/flowers.py

> ./linoleumBlocksV1.py images/Winston_Churchill_1874_-_1965_ZZZ5426F.jpg config/churchill.py

> ./linoleumBlocksV1.py images/Jefferson_Memorial_rear_view_IMG_4733.JPG config/jefferson.py

I owe a debt of inspiration and example to [Greg Borenstein](http://gregborenstein.com/), who used a similar process for his 2014 nanogenmo entry, available [here](https://github.com/dariusk/NaNoGenMo-2014/issues/70) and [here](http://gregborenstein.com/comics/generated_detective/1/).
