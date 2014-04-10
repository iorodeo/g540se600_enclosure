"""
Creates an enclosure for the water channel controller electronics.
"""
from __future__ import print_function
import math
import scipy
import os
import os.path
from py2scad import *


class G540SE600_Enclosure(Basic_Enclosure):

    def __init__(self, params):
        self.params = params
        self.createPowerSuppyHoles()
        self.createPowerCordHole()
        self.createFanHoles()
        self.createGeckoDriveHoles()
        self.createVentAndMeshHoles()
        self.createCableTieHoles()

    def make(self):
        super(G540SE600_Enclosure,self).make()

    def createPowerSuppyHoles(self):
        psHoleList = []

        # Add side holes
        for i in (-1,1):
            for j in (-1,1):
                xPos = i*0.5*self.params['ps_side_hole_spacing_x']  
                xPos += self.params['ps_side_hole_rel_pos_x']
                xPos += self.params['ps_side_center_x']

                yPos= j*0.5*self.params['ps_side_hole_spacing_y']
                yPos += self.params['ps_side_hole_rel_pos_y']
                yPos += self.params['ps_side_center_y']

                hole = {
                        'panel'     : self.params['ps_side_hole_panel'],
                        'type'      : 'round',
                        'location'  : (xPos, yPos),
                        'size'      : self.params['ps_side_hole_diameter'],
                        }
                psHoleList.append(hole)

        # Add bottom holes
        posList = zip(
                self.params['ps_bottom_hole_rel_pos_x'], 
                self.params['ps_bottom_hole_rel_pos_y'],
                )

        for xPos, yPos in posList:
            xPosAdj = xPos + self.params['ps_bottom_center_x']
            yPosAdj = yPos + self.params['ps_bottom_center_y']
            hole = {
                    'panel'    : self.params['ps_bottom_hole_panel'],
                    'type'     : 'round',
                    'location' : (xPosAdj, yPosAdj),
                    'size'     : self.params['ps_bottom_hole_diameter'],
                    }
            psHoleList.append(hole)

        self.params['hole_list'].extend(psHoleList)


    def createPowerCordHole(self):
        location = self.params['cord_hole_pos_x'], self.params['cord_hole_pos_y']
        hole = {
                'panel'     : self.params['cord_hole_panel'],
                'type'      : 'round',
                'location'  : location,
                'size'      : self.params['cord_hole_diameter'],
                }
        self.params['hole_list'].append(hole)

    def createFanHoles(self):
        fanHoleList = []
        # Add mount holes
        for i in (-1,1):
            for j in (-1,1):
                xPos = i*0.5*self.params['fan_hole_spacing_x']
                xPos += self.params['fan_center_pos_x']
                yPos = j*0.5*self.params['fan_hole_spacing_y']
                yPos += self.params['fan_center_pos_y']
                hole = {
                        'panel'    : self.params['fan_panel'],
                        'type'     : 'round',
                        'location' : (xPos,yPos),
                        'size'     : self.params['fan_hole_diameter'],
                        }
                fanHoleList.append(hole)
        # Add cutout Hole
        location = self.params['fan_center_pos_x'], self.params['fan_center_pos_y']
        cutoutHole = {
                'panel'    : self.params['fan_panel'],
                'type'     : 'round',
                'location' : location,
                'size'     : self.params['fan_cutout_diameter']
                }
        fanHoleList.append(cutoutHole)
        self.params['hole_list'].extend(fanHoleList)

    def createGeckoDriveHoles(self):
        driveHoleList = []
        # Add mount holes
        for i in (-1,1):
            for j in (-1,1):
                xPos = i*0.5*self.params['drive_hole_spacing_x']
                xPos += self.params['drive_center_pos_x']
                yPos = j*0.5*self.params['drive_hole_spacing_y']
                yPos += self.params['drive_center_pos_y']
                hole = {
                        'panel'    : self.params['drive_panel'],
                        'type'     : 'round',
                        'location' : (xPos,yPos),
                        'size'     : self.params['drive_hole_diameter'],
                        }
                driveHoleList.append(hole)
        # Add cutout hole
        cutoutLocation = (
                self.params['drive_center_pos_x'], 
                self.params['drive_center_pos_y'],
                )

        cutoutSize = (
                self.params['drive_cutout_size_x'],
                self.params['drive_cutout_size_y'],
                self.params['drive_cutout_radius'],
                )

        cutoutHole = {
                'panel'    : self.params['drive_panel'],
                'type'     : 'rounded_square',
                'location' : cutoutLocation,
                'size'     : cutoutSize,
                }
        driveHoleList.append(cutoutHole)
        self.params['hole_list'].extend(driveHoleList)

    def createVentAndMeshHoles(self):
        x,y,z = self.params['inner_dimensions']
        xSpacing = self.params['vent_hole_spacing_x']
        ySpacing = self.params['vent_hole_spacing_y']
        xPosMargin = self.params['vent_hole_margin_+x']
        xNegMargin = self.params['vent_hole_margin_-x']
        yPosMargin = self.params['vent_hole_margin_+y']
        yNegMargin = self.params['vent_hole_margin_-y']

        # Add vent holes
        numHolesX = int(math.floor((y - xPosMargin - xNegMargin)/xSpacing))
        numHolesY = int(math.floor((z - yPosMargin - yNegMargin)/ySpacing))

        xPosList = [i*xSpacing for i in range(numHolesX)]
        xPosShift = -0.5*xPosList[-1] + 0.5*xPosMargin - 0.5*xNegMargin
        xPosList = [xPos + xPosShift for xPos in xPosList]

        yPosList = [i*ySpacing for i in range(numHolesY)]
        yPosShift = -0.5*yPosList[-1] + 0.5*yPosMargin - 0.5*yNegMargin
        yPosList = [yPos + yPosShift for yPos in yPosList]

        holeList = []
        for xPos in xPosList:
            for yPos in yPosList:
                hole = {
                        'panel'    : self.params['vent_hole_panel'],
                        'type'     : 'round',
                        'location' : (xPos, yPos),
                        'size'     : self.params['vent_hole_diameter'],
                        }
                holeList.append(hole)

        self.params['hole_list'].extend(holeList)

        # Add mesh mount holes
        xMin = min(xPosList)
        xMax = max(xPosList)
        xMid = 0.5*(xMax + xMin)
        yMin = min(yPosList)
        yMax = max(yPosList)
        screwMargin = self.params['mesh_mount_screw_margin']
        ventDiam = self.params['vent_hole_diameter']

        screwXPosList = [
                (xMin - screwMargin - 0.5*ventDiam), 
                xMid, 
                (xMax + screwMargin + 0.5*ventDiam)
                ]

        screwYPosList = [
                yMax + screwMargin + 0.5*ventDiam, 
                yMin - screwMargin - 0.5*ventDiam,
                ]
                

        for xPos in screwXPosList:
            for yPos in  screwYPosList:
                hole = {
                        'panel'    : self.params['vent_hole_panel'],
                        'type'     : 'round', 
                        'location' : (xPos, yPos),
                        'size'     : self.params['mesh_mount_screw_diameter']
                        }
                holeList.append(hole)
        self.params['hole_list'].extend(holeList)


    def createCableTieHoles(self):
        x,y,z = self.params['inner_dimensions']
        xSpacing = self.params['tie_holder_hole_spacing_x']
        ySpacing = self.params['tie_holder_hole_spacing_y']
        xMargin = self.params['tie_holder_wall_margin_x']
        numHoles = int(math.floor((x-2*xMargin)/xSpacing))

        # Get relative position lists 
        xRelPosList = [i*xSpacing  for i in range(numHoles)] 
        xRelPosList = [xPos - 0.5*xRelPosList[-1] for xPos in xRelPosList]
        yRelPosList = [-0.5*ySpacing, 0.5*ySpacing]

        # Get rounded_square hole size
        holeSize = (
                self.params['tie_holder_hole_size_x'],
                self.params['tie_holder_hole_size_y'],
                self.params['tie_holder_hole_radius'],
                )

        # Create list of cable tie holes
        holeList = []
        for xRelPos in xRelPosList:
            for yRelPos in yRelPosList:
                xPos = xRelPos + self.params['tie_holder_center_pos_x']
                yPos = yRelPos + self.params['tie_holder_center_pos_y']
                hole = {
                        'panel'    : self.params['tie_holder_panel'],
                        'type'     : 'rounded_square',
                        'location' : (xPos,yPos),
                        'size'     :  holeSize,
                        }
                holeList.append(hole)
        self.params['hole_list'].extend(holeList)













