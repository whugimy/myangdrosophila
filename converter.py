import rawpy
import imageio
from matplotlib import pyplot as plt
import numpy as np

for i in range(10):

    print('currently handling ' + str(i) + '_UV.NEF')

    uv = rawpy.imread(str(i)+'_UV.NEF').postprocess(output_bps=8)
    fs = rawpy.imread(str(i)+'_FS.NEF').postprocess(output_bps=8)

    amber = (fs[...,0] * 0.4908 + fs[...,1] * 0.5091).astype(int)
    uv_just_red = (uv[...,0])
    blue = fs[...,2]

    combined = np.array([amber, uv_just_red, blue]).transpose(1,2,0)
    imageio.imwrite(str(i)+'_result.png', combined.astype(np.uint8))