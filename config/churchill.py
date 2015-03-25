
#   linoleumBlocks CONFIG FILE.  DICTIONARY MUST BE NAMED CONFIG  

config = {

    #   None, OR AN INTEGER
    'resizeWidth': 750,

    #   BOOLEAN         
    #'posterize': True, 
    'posterize': False, 
    
    #   None (defaults to 2), or int
    'posterize-value': None,
    #'posterize-value': 5,

    #   None, 'canny', OR 'imagemagick'   
        
    'edgeType': None,
    'edge-fill': None,
    'edge-fill-opacity': None,
    'edge-stroke': None,
    'edge-stroke-width': None,
        
    #'edgeType': 'canny',
    #'edge-fill': '#000000',
    #'edge-fill-opacity': '1.0',
    #'edge-stroke': '#000000',
    #'edge-stroke-width': '1',         

    #'edgeType': 'imagemagick',
    #'edge-fill': None,
    #'edge-fill-opacity': None,
    #'edge-stroke': '#FF0000',
    #'edge-stroke-width': '20',
    
    #   rgb OR grayscale         
    'channelType': 'grayscale',           
    
    #   None IF channelType RBG; OTHERWISE AN INTEGER
    'grayscaleChannels': 5,
    
    #   None, OR ELSE A LIST OF IN 0-254; 
    #'grayscaleChannelBreaks': None, 
    'grayscaleChannelBreaks': [[0, 15], [16, 76], [77, 137], [138, 198], [199, 255]],
    
    #  
    'channelSpecs': [
        
        #   SOLID COLORS
    
        {'fill': 'url(\'#crossHatch\')', 'fill-opacity': '1.0', 'stroke': '#0c200d', 'stroke-width': '25'},
        {'fill': 'url(\'#hatchingA\')', 'fill-opacity': '1.0', 'stroke': '#00420f', 'stroke-width': '25'},
        {'fill': 'url(\'#hatchingB\')', 'fill-opacity': '1.0', 'stroke': '#00420f', 'stroke-width': '25'},
        {'fill': '#fdd8d9', 'fill-opacity': '1.0', 'stroke': '#00420f', 'stroke-width': '25'},
        {'fill': '#ffffff', 'fill-opacity': '1.0', 'stroke': '#fdd8d9', 'stroke-width': '25'},
        
        
        #   HATCHING
        
        #{'fill': 'url(\'#crossHatch\')', 'fill-opacity': '1.0', 'stroke': None, 'stroke-width': None},
        #{'fill': 'url(\'#hatchingA\')', 'fill-opacity': '1.0', 'stroke': None, 'stroke-width': None},
        #{'fill': 'url(\'#hatchingB\')', 'fill-opacity': '1.0', 'stroke': None, 'stroke-width': None},
        
        #   CIRCLES
        
        #{'fill': 'url(\'#circle0\')', 'fill-opacity': '1.0', 'stroke': '#181b44', 'stroke-width': '10'},
        #{'fill': 'url(\'#circle1\')', 'fill-opacity': '1.0', 'stroke': '#181b44', 'stroke-width': '10'},
        #{'fill': 'url(\'#circle2\')', 'fill-opacity': '1.0', 'stroke': '#181b44', 'stroke-width': '10'},
    ],
      
    #   A DICTIONARY OR ELSE None
    #'patterns': None,
    'patterns': {
    
        'crossHatch': '<pattern id="crossHatch" patternUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><g style="fill:#ffffff; stroke:#00420f; stroke-width: 32; stroke-opacity: 1.0;"><path d="M0,0 l100,100"/><path d="M100,0 l-100,100"/></g></pattern>',
        
        'hatchingA': '<pattern id="hatchingA" patternUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><g style="fill:#ffffff; stroke:#00420f; stroke-width: 20; stroke-opacity: 1.0;"><path d="M0,0 l100,100"/></g></pattern>',
        
        'hatchingB': '<pattern id="hatchingB" patternUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><g style="fill:#ffffff; stroke:#00420f; stroke-width: 10; stroke-opacity: 1.0;"><path d="M100,0 l-100,100"/></g></pattern>',
        
        'hatchingC': '<pattern id="hatchingC" patternUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><g style="fill:#ffffff; stroke:#fdd8d9; stroke-width: 10; stroke-opacity: 1.0;"><path d="M0,0 l100,100"/></g></pattern>',
            
        'circle0': '<pattern id="circle0" patternUnits="userSpaceOnUse" x="0" y="0" width="50" height="50"><g style="fill: #ffffff;"><circle cx="25" cy="25" r="20" stroke="none" fill="#181b44"/></g></pattern>',

        'circle1': '<pattern id="circle1" patternUnits="userSpaceOnUse" x="0" y="0" width="50" height="50"><g style="fill: #ffffff;"><circle cx="25" cy="25" r="15" stroke="none" fill="#181b44"/></g></pattern>',

        'circle2': '<pattern id="circle2" patternUnits="userSpaceOnUse" x="0" y="0" width="50" height="50"><g style="fill: #ffffff;"><circle cx="25" cy="25" r="10" stroke="none" fill="#181b44"/></g></pattern>'
    },
}
