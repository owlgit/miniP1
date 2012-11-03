### Get correct atom position for linkage
import numpy as np

### Get positions of the atoms
def getPos(pFile):

   fName = pFile
   open(fName, 'r')

   # get cell size - assume cubic
   str1 = ' '.join(file(fName).readlines()[2:5])
   cellSize = np.fromstring(str1, sep=' ')
   cellSize.shape = (3,3)
   xlat = cellSize[0]
   ylat = cellSize[1]
   zlat = cellSize[2]

   # get number of atoms per species
   str1 = ' '.join(file(fName).readlines()[6:7])
   dataElements = np.fromstring(str1, sep=' ')
   sizeElements = len(dataElements)

   # get the coordinates of each atom
   ttlAtoms = np.sum(dataElements)
   str1  = ' '.join(file(fName).readlines()[8:8+int(ttlAtoms)])
   dataCoord = np.fromstring(str1, sep=' ')
   dataCoord.shape = (int(ttlAtoms),3)
   for i in range(int(ttlAtoms)):
      dataCoord[i,0] = dataCoord[i,0]*xlat[0] + dataCoord[i,1]*ylat[0] + dataCoord[i,2]*zlat[0]
      dataCoord[i,1] = dataCoord[i,0]*xlat[1] + dataCoord[i,1]*ylat[1] + dataCoord[i,2]*zlat[1]
      dataCoord[i,2] = dataCoord[i,0]*xlat[2] + dataCoord[i,1]*ylat[2] + dataCoord[i,2]*zlat[2]

   return dataCoord,sizeElements,ttlAtoms,dataElements



### Check if value is integer type
def isStringInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


###  Get linkage between atoms
def getLinks(lName,ttlAtoms):

   fName2 = lName
   open(fName2, 'r')

   notFound = True
   i = 0
   inD = 0
   while (notFound):
      str = ' '.join(file(fName2).readlines()[i:i+1])
      inD = str.find("nearest neighbor table")
      if(inD > 0):
         break
      i += 1

   i += 1
   n1 = []
   n2 = []
   for j in range(int(ttlAtoms)):
      #read single line of the nearest neighbour list
      str1 = ' '.join(file(fName2).readlines()[i+j:i+j+1])
      s = str1.split(" ")
      #test for each element if it is an integer
      for k in range(len(s)):
         if(isStringInt(s[k]) and int(s[k]) > j+1):
            n1.append(j)
            n2.append(int(s[k])-1)

   return n1,n2

### Plot the charge density
#def plotCDdensity(dirCal,plotLinks,plotCell):
    ##############################################
    ########## Start  Plotting ###################
    ##############################################

    #from enthought.mayavi import mlab
    #from jasp import *
    #from ase.data.colors import cpk_colors
    #import getPosLink as gPL
    #import os

    #with jasp(dirCal) as calc:
    #    calc.calculate()
    #    cObj = calc.get_atoms()
    #    xCD, yCD, zCD, cd = calc.get_charge_density()
    #    print calc

    # assume path is current directory + folder name where calculations are stored
    #path = os.getcwd() + '/' + dirCal + '/'

    #mlab.figure(1, bgcolor=(1, 1, 1))
    #mlab.clf()

    ##############################
    # Plot position of the atoms #
    ##############################

    # read file to get position
    #dataCoord,sizeElements, ttlAtoms, dataElements = gPL.getPos(path + 'CHG')
    #a = 0
    #i = 0
    #for a in range(int(sizeElements)):
    #    b = 0
    #    for b in range(int(dataElements[a])):
    #        mlab.points3d(dataCoord[i,0], dataCoord[i,1], dataCoord[i,2],
    #                    scale_factor=0.5,
    #                    resolution=20,
    #                    color=tuple(cpk_colors[a]),
    #                    scale_mode='none')
    #        i += 1


    ###########################
    # Plot links between atoms #
    ###########################

    #if(plotLinks == 1):
    ## read file to get linkage or connectivity between atoms
       #   n1,n2 = gPL.getLinks(path + 'OUTCAR',ttlAtoms)
       #for j in range(len(n1)):
       #     pts = [n1[j],n2[j]]
       #   ptsX = dataCoord[pts,0]
       #   ptsY = dataCoord[pts,1]
       #   ptsZ = dataCoord[pts,2]
       #   mlab.plot3d(ptsX, ptsY, ptsZ,
       #               tube_radius=0.05,tube_sides=8,colormap='Reds')


    ##########################
    # draw the cell boundary #
    ##########################

    #if(plotCell == 1):
    #    a1, a2, a3 = cObj.get_cell()
    #    origin = [0, 0, 0]
    #    cell_matrix = [[origin, a1],
    #           [origin, a2],
    #           [origin, a3],
    #           [a1, a1 + a2],
    #           [a1, a1 + a3],
    #           [a2, a2 + a1],
    #           [a2, a2 + a3],
    #           [a3, a1 + a3],
    #           [a3, a2 + a3],
    #           [a1 + a2, a1 + a2 + a3],
    #           [a2 + a3, a1 + a2 + a3],
    #           [a1 + a3, a1 + a3 + a2]]

    #    for p1, p2 in cell_matrix:
    #        mlab.plot3d([p1[0], p2[0]], # x-positions
    #                     [p1[1], p2[1]], # y-positions
    #                     [p1[2], p2[2]], # z-positions
    #                     tube_radius=0.01)

    ####################################
    # Plot the charge density as "fog" #
    ####################################

    #dataCD = cd
    #x = xCD
    #y = yCD
    #z = zCD

    #densityCD = mlab.pipeline.scalar_field(x,y,z,dataCD)
    #minCD  = dataCD.min()
    #maxCD  = dataCD.max()

    #vol = mlab.pipeline.volume(densityCD,
    #                       vmin=minCD+0.01*(maxCD -minCD),
    #                       vmax=minCD+0.1*(maxCD-minCD))


    #mlab.savefig(dirCal +'2.png')
    #mlab.show()
    #return mlab.gcf()
