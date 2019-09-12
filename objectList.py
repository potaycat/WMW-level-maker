import os
cur_dir = os.path.dirname(os.path.realpath(__file__))

Ducky = {
    'path2img' : os.path.join(cur_dir, 'assets/Ducky.png'),
    "Properties" : ['Filename' , 'Type'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/star.hs'],
    'Type' : ['star']
}

AllieDucky = {
    'path2img' : os.path.join(cur_dir, 'assets/AllieDucky.png'),
    "Properties" : ['Filename' ,'StarType' , 'Type'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/star_steam_allie.hs'],
    'StarType' : ['allie'],
    'Type' : ['star']
}

CrankyDucky = {
    'path2img' : os.path.join(cur_dir, 'assets/CrankyDucky.png'),
    "Properties" : ['Filename' , 'Type'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/star_poison.hs'],
    'Type' : ['star']
}

GiantDucky = {
    'path2img' : os.path.join(cur_dir, 'assets/GiantDucky.png'),
    "Properties" : ['Filename' , 'Type' , 'StarType'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/star_mega.hs'],
    'StarType' : ['mega'],
    'Type' : ['star']
}

TinyDucky = {
    'path2img' : os.path.join(cur_dir, 'assets/TinyDucky.png'),
    "Properties" : ['Filename' , 'Type' , 'StarType'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/star_baby.hs'],
    'StarType' : ['baby'],
    'Type' : ['star']
}

BrokenPipe = {
    'path2img' : os.path.join(cur_dir, 'assets/BrokenPipe.png'),
    "Properties" : ['Filename' , 'Type' , 'ConnectedSpout0' , 'ConnectedSpoutProbability0'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/broken_pipe.hs'],
    'Type' : ['spout'],
    'ConnectedSpout0' : ['SWAMPY_SPOUT'],
    'ConnectedSpoutProbability0' : ['1']
}

Pipe = {
    'path2img' : os.path.join(cur_dir, 'assets/Pipe.png'),
    "Properties" : ['Filename'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/pipe_straight.hs']
}

PipeElbow = {
    'path2img' : os.path.join(cur_dir, 'assets/PipeElbow.png'),
    "Properties" : ['Filename'],
    'specialAtrb' : [],
    
    'Filename' : ['/Objects/pipe_elbow_1.hs']
}

Spout = {
    'path2img' : os.path.join(cur_dir, 'assets/Spout.png'),
    "Properties" : ['Filename' , 'Type' , 'FluidType' , 'NumberParticles' , 'ParticleSpeed' , 'ParticlesPerSecond'],
    'specialAtrb' : ['can_be_connect2'],
    
    'Filename' : ['/Objects/shower_head.hs'],
    'FluidType' : ['Water' , 'ContaminatedWater', 'Lava'],
    'NumberParticles' : ['0'],# 'intput ', 
    'ParticleSpeed' : 'intput Shooting Force', # [50],
    'ParticlesPerSecond' : 'intput Shooting Speed', # [8],
    'Type' : ['spout'],
    #'Timer0' : 'intput', # [(1 , 3.5)],
    #'Timer1' : 'intput' # [(0 , 99999)]
}

Drain = {
    'path2img' : os.path.join(cur_dir, 'assets/Drain.png'),
    "Properties" : ['Filename' , 'Type' , 'ConnectedSpout0' , 'ConnectedSpoutProbability0'],
    'specialAtrb' : [],

    'ConnectedSpout0' : 'connec Connected Sprout', # ['Spout5'],
    'ConnectedSpoutProbability0' : ['1'],
    'Filename' : ['/Objects/basic_drain.hs'],
    'Type' : ['spout']
}

PipeElbow2 = {
    'path2img' : os.path.join(cur_dir, 'assets/PipeElbow2.png'),
    "Properties" : ['Filename'],
    'specialAtrb' : [],

    'Filename' : ['/Objects/pipe_elbow_2.hs']
}

Bomb = {
    'path2img' : os.path.join(cur_dir, 'assets/Bomb.png'),
    "Properties" : ['Filename'],
    'specialAtrb' : [],

    'Filename' : ['/Objects/pipe_elbow_2.hs']
}









Room = {
    'path2img' : os.path.join(cur_dir, 'assets/Room.png'),
    "Properties" : [],
    'specialAtrb' : ['isRoom'],
}
