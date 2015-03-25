#!/usr/bin/python   

import sys, codecs, commands, imp, re

#   ALSO REQUIRES IMAGEMAGICK
from lxml import etree
from PIL import Image
import cv2
import numpy as np
import matplotlib.image as mpimg

#   --------------------------------------------------------------------
#   
#   --------------------------------------------------------------------

def executeCommand(cmd, printCommand):

    if printCommand == True:
        print cmd

    results = commands.getoutput(cmd)

    if printCommand == True:
        print results

#   --------------------------------------------------------------------
#   
#   --------------------------------------------------------------------

def linoleumBlocks(pathToInputImage, pathToConfig):
    
    #   REMOVE TEMP FILES
    
    executeCommand('rm lb.temp*', True)
    
    config = imp.load_source('config', pathToConfig).config
    
    #   RESIZE
    
    finalImageWidth = ''
    
    if config['resizeWidth'] == None:
        executeCommand('cp ' + pathToInputImage + ' lb.temp.png', True)
            
        im = Image.open(pathToInputImage)
        finalImageWidth = im.size[0]
    else:
        executeCommand('convert ' + pathToInputImage + ' -resize ' + str(config['resizeWidth']) + 'x lb.temp.png', True)
        finalImageWidth = config['resizeWidth']
        
    allChannelsImage = 'lb.temp.png'
    
    #   POSTERIZE
        
    if config['posterize'] == True:
        
        posterizeValue = 2
        if config['posterize-value'] != None:
            posterizeValue = config['posterize-value']
            
        executeCommand('convert lb.temp.png  +dither -posterize ' + str(posterizeValue) + '  lb.temp.posterize.png', True)
        allChannelsImage = 'lb.temp.posterize.png'
    
    #   EDGE DETECTION
        
    edgeImage = ''    
        
    if config['edgeType'] == 'canny': 

        img = cv2.imread(allChannelsImage, 0)
        blur = cv2.blur(img, (5, 5))
        edges = cv2.Canny(blur, 10, 125)
        mpimg.imsave('lb.temp_edge.png', edges)

        executeCommand('convert lb.temp_edge.png -channel R -separate -reverse lb.temp_edge_red.bmp', True)
        executeCommand('convert lb.temp_edge_red.bmp -negate -monochrome lb.temp_edge_red.bmp', True)
        
        edgeImage = 'lb.temp_edge_red.bmp'
        
    if config['edgeType'] == 'imagemagick': 
    
        executeCommand('convert ' + allChannelsImage + ' -colorspace Gray -edge 2 lb.temp_edge.jpg', True)
        executeCommand('convert lb.temp_edge.jpg -channel R -separate lb.temp_edge_red.bmp', True)
        executeCommand('convert lb.temp_edge_red.bmp -negate lb.temp_edge_red_neg.bmp', True)
        
        edgeImage = 'lb.temp_edge_red_neg.bmp'
    
    #   CHANNEL SEPARATION
    
    channelImageFiles = []
    
    if config['channelType'] == 'rgb':      
           
        executeCommand('convert ' + allChannelsImage + ' -channel R -separate lb.temp_red.bmp', True)
        executeCommand('convert ' + allChannelsImage + ' -channel G -separate lb.temp_green.bmp', True)
        executeCommand('convert ' + allChannelsImage + ' -channel B -separate lb.temp_blue.bmp', True)
        
        channelImageFiles = ['lb.temp_red.bmp', 'lb.temp_green.bmp', 'lb.temp_blue.bmp']
    
    if config['channelType'] == 'grayscale': 
    
        executeCommand('convert ' + allChannelsImage + ' -colorspace Gray -resize 750x lb.temp.g.png', True)
    
        allChannelsImage = 'lb.temp.g.png'
    
        breaks = []
        
        if config['grayscaleChannelBreaks'] == None:
            
            
            a = 255 / config['grayscaleChannels']
            b = 0
            c = a
            while c < 256:
                breaks.append([b, c])
                b = b + a
                c = c + a
                
            for d in range(0, len(breaks)):
                breaks[d][0] = breaks[d][0]  + 1   
                
            breaks[0][0] = 0
            breaks[-1][-1] = 255    
            
            print 'breaks', breaks
            
        else:
            breaks = config['grayscaleChannelBreaks']
            
        im = Image.open(allChannelsImage)

        channelImages = []
        for i in range(0, config['grayscaleChannels']):
            channelImages.append(Image.new(im.mode, im.size, color=255))

        w = im.size[0]
        h = im.size[1]

        for x in range(0, w):
            for y in range(0, h):
                
                c = im.getpixel((x, y))

                i = -1
                for b in range(0, len(breaks)):
                    if c >= breaks[b][0] and c <= breaks[b][1]:
                        i = b
                        break

                channelImages[i].putpixel((x, y), 0)
    
        for i, c in enumerate(channelImages):
            channelImages[i].save('lb.temp.channel.' + str(i) + '.bmp')
            channelImageFiles.append('lb.temp.channel.' + str(i) + '.bmp')
    
    #   CONVERT TO SVG
    
    if edgeImage > '':
        
        executeCommand('potrace -s -z black ' + edgeImage, True)
        
    for c in channelImageFiles:
        
        executeCommand('potrace -s ' + c, True)
    
    #   LOAD SVG AND ADD EDGES, FILLS, ETC
    
    finalTree = None
    finalTreeRoot = None
    
    for i, c in enumerate(channelImageFiles):
        
        cTree = etree.parse(c.replace('.bmp', '.svg'))
        
        gNodes = cTree.xpath('//svg:g', namespaces={'svg': 'http://www.w3.org/2000/svg'})
        
        for g in gNodes:
    
            g.set('fill', config['channelSpecs'][i]['fill'])
            g.set('fill-opacity', config['channelSpecs'][i]['fill-opacity'])
            
            if config['channelSpecs'][i]['stroke'] != None:
                g.set('stroke', config['channelSpecs'][i]['stroke'])
                
            if config['channelSpecs'][i]['stroke-width'] != None:
                g.set('stroke-width', config['channelSpecs'][i]['stroke-width'])
            
            if i > 0:
                finalTreeRoot.append(g)
        
        if i == 0:
            finalTree = cTree
            finalTreeRoot = finalTree.getroot()
    
    if edgeImage > '':
        
        edgeTree = etree.parse(edgeImage.replace('.bmp', '.svg'))
        
        gNodes = edgeTree.xpath('//svg:g', namespaces={'svg': 'http://www.w3.org/2000/svg'})
        
        for g in gNodes:
            
            if config['edge-fill'] == None:
                g.set('fill', 'none')
            else:
                g.set('fill', config['edge-fill'])
                
            if config['edge-fill-opacity'] == None:
                g.set('fill-opacity', '0.0')
            else:
                g.set('fill-opacity', config['edge-fill-opacity'])
            
            if config['edge-stroke'] != None:
                g.set('stroke', config['edge-stroke'])
            
            if config['edge-stroke-width'] != None:
                g.set('stroke-width', config['edge-stroke-width'])
    
            finalTreeRoot.append(g)
    
    if config['patterns'] != None:
        for k, v in config['patterns'].iteritems():
            p = etree.fromstring(v)
            finalTreeRoot.insert(0, p)
    
    #   OUTPUT SVG
    
    fileNameParts = re.split('\/|\.', pathToInputImage)
    
    print 'fileNameParts', fileNameParts
    
    outputFileName = '/'.join(fileNameParts[:-2]) + '/lb.' + fileNameParts[-2] + '.svg'
    
    outF = codecs.open(outputFileName, 'w', encoding='utf-8')
    outF.write(etree.tostring(finalTree, pretty_print=True))
    outF.close()
    
    #   PROCESS SVG THROUGH BATIK
    
    executeCommand('cd batik-1.7; java -jar batik-rasterizer.jar -bg 255.255.255.255 -w ' + str(finalImageWidth) + ' ../' + outputFileName, True)
    
    #   REMOVE TEMP FILES
    
    executeCommand('rm lb.temp*', True)
    executeCommand('rm ' + outputFileName, True)
    
#   --------------------------------------------------------------------
#   
#   --------------------------------------------------------------------

if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print 'USAGE: ./linoleumBlocksV1.py pathToInputImage pathToConfig'
        print len(sys.argv)
        exit()
        
    pathToInputImage = sys.argv[1]
    pathToConfig = sys.argv[2]
    
    linoleumBlocks(pathToInputImage, pathToConfig)
