from random import randint

class Object():
    def __init__(self, props = None):
        self.props = props or dict()
        #self.props["name"] = None
        self.props["location"] = (0 , 0)
        self.props["angle"] = 0
        self.props['intput'] = []
        self.props['tplput'] = []
        self.props['connec'] = None
        self.props['canConnectTo'] = False
        #self.more_data_here = None
    
    def specificProps(self, selflist, props = None):
        self.props["texture"] = selflist['path2img']
        self.props["PropList"] = selflist['Properties']
        
        i=0
        while i < len(self.props["PropList"]):
            propertay = selflist[ self.props["PropList"][i] ]
            if len( propertay ) <= 1:
                if type( propertay  ) is str:
                    if propertay[:6] == 'intput':
                        self.intput.append( propertay[8:] , i , None)
                    if propertay[:6] == 'tplput':
                        self.tplput.append( propertay[8:] , i , None)
                        
                    if propertay[:6] == 'connec':
                        self.connec.append( propertay[8:] , i , None)
                else:
                    self.props[ self.props["PropList"][i] ] = propertay
            
            i += 1

def addObject(otype, noOfO):
    thingy = Object()
    thingy.props["name"] = 'Object%s' %(noOfO)
    
    for attribute in otype['specialAtrb']:
        if attribute == 'isRoom':
            thingy.props.pop("name")
            thingy.props.pop("angle")
        if attribute == 'can_be_connect2':
            thingy.props['canConnectTo'] = True
            
    thingy.specificProps(selflist = otype)
    
    return thingy
        
