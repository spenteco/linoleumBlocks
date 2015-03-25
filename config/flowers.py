
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
    'grayscaleChannelBreaks': [[0, 30], [31, 102], [103, 153], [154, 204], [205, 255]],
    
    #  
    'channelSpecs': [
        
        #   SOLID COLORS
    
        {'fill': '#151c3e', 'fill-opacity': '1.0', 'stroke': None, 'stroke-width': None},
        {'fill': '#5f6790', 'fill-opacity': '1.0', 'stroke': '#151c3e', 'stroke-width': '10'},
        {'fill': '#849a9a', 'fill-opacity': '1.0', 'stroke': '#151c3e', 'stroke-width': '10'},
        {'fill': '#eac671', 'fill-opacity': '1.0', 'stroke': '#151c3e', 'stroke-width': '10'},
        {'fill': '#f4ecbc', 'fill-opacity': '1.0', 'stroke': '#ffffff', 'stroke-width': '10'},
        
        
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
    'patterns': None,
    #'patterns': {
    
        #'crossHatch': '<pattern id="crossHatch" patternUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><g style="fill:#ffffff; stroke:#181b44; stroke-width: 32; stroke-opacity: 1.0;"><path d="M0,0 l100,100"/><path d="M100,0 l-100,100"/></g></pattern>',
        
        #'hatchingA': '<pattern id="hatchingA" patternUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><g style="fill:#ffffff; stroke:#181b44; stroke-width: 20; stroke-opacity: 1.0;"><path d="M0,0 l100,100"/><path d="M100,0 l-100,100"/></g></pattern>',
        
        #'hatchingB': '<pattern id="hatchingB" patternUnits="userSpaceOnUse" x="0" y="0" width="100" height="100"><g style="fill:#ffffff; stroke:#181b44; stroke-width: 8; stroke-opacity: 1.0;"><path d="M0,0 l100,100"/><path d="M100,0 l-100,100"/></g></pattern>'
            
        #'circle0': '<pattern id="circle0" patternUnits="userSpaceOnUse" x="0" y="0" width="50" height="50"><g style="fill: #ffffff;"><circle cx="25" cy="25" r="20" stroke="none" fill="#181b44"/></g></pattern>',

        #'circle1': '<pattern id="circle1" patternUnits="userSpaceOnUse" x="0" y="0" width="50" height="50"><g style="fill: #ffffff;"><circle cx="25" cy="25" r="15" stroke="none" fill="#181b44"/></g></pattern>',

        #'circle2': '<pattern id="circle2" patternUnits="userSpaceOnUse" x="0" y="0" width="50" height="50"><g style="fill: #ffffff;"><circle cx="25" cy="25" r="10" stroke="none" fill="#181b44"/></g></pattern>'
    #},
}
