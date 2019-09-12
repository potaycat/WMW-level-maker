from lxml import etree
import objectList

def finalBuild(objList, path):
    #print(objList)
    root = etree.Element('Objects')
    
    for thing in objList:
        a = etree.Element('Object')
        root.append(a)
        
        try:
            a.set('name',thing.props['name'])
            
            loc = etree.Element('AbsoluteLocation')
            loc.set('value' , '%s %s' %(thing.props['location'][0] , thing.props['location'][1]) )
            a.append(loc)
            
            b = etree.Element('Properties')
            a.append(b)
            
            
            #angle
            prop = etree.Element('Property')
            prop.set('name', "Angle" )
            prop.set('value', str( thing.props['angle'] ) )
            b.append(prop)
        
        except:
            print("herrrrrrrrre")
            a = etree.Element('Room')
            root.append(a)
            loc = etree.Element('AbsoluteLocation')
            loc.set('value' , '%s %s' %(thing.props['location'][0] , thing.props['location'][1]) )
            a.append(loc)
            
        root.append(a)
        
        i=0
        while i < len( thing.props["PropList"] ):
            prop = etree.Element('Property')
            b.append(prop)
            try:
                prop.set('name', str( thing.props["PropList"][i] ) )
                prop.set('value', str( thing.props[ thing.props["PropList"][i] ][0] ) )
            except:
                pass
            root.append(a)
            
            i+=1
    
    string = etree.tostring(root, pretty_print=True)
    #print (string)
    text_file = open(path, "wb")
    #text_file.write("""<?xml version="1.0"?>\n""")
    text_file.write(string)
    text_file.close()
    
