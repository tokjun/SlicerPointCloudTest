import os
import unittest
import random
import math
import tempfile
import time
import numpy
import vtk
from vtk.util.misc import vtkGetDataRoot

from __main__ import vtk, qt, ctk, slicer

def showPointCloud(modelNodeID):

    model = slicer.mrmlScene.GetNodeByID(modelNodeID)
    polydata = model.GetPolyData()

    # Reuse the locator
    locator = vtk.vtkStaticPointLocator()
    locator.SetDataSet(polydata)
    locator.BuildLocator()

    # Remove isolated points
    removal = vtk.vtkRadiusOutlierRemoval()
    removal.SetInputData(polydata)
    removal.SetLocator(locator)
    removal.SetRadius(10)
    removal.SetNumberOfNeighbors(2)
    removal.GenerateOutliersOn()

    # Time execution
    timer = vtk.vtkTimerLog()
    timer.StartTimer()
    removal.Update()
    timer.StopTimer()
    time = timer.GetElapsedTime()
    print("Time to remove points: {0}".format(time))
    print("   Number removed: {0}".format(removal.GetNumberOfPointsRemoved()),
          " (out of: {}".format(polydata.GetNumberOfPoints()))

    # First output are the non-outliers
    remMapper = vtk.vtkPointGaussianMapper()
    remMapper.SetInputConnection(removal.GetOutputPort())
    remMapper.EmissiveOff()
    remMapper.SetScaleFactor(0.0)

    remActor = vtk.vtkActor()
    remActor.SetMapper(remMapper)
    
    lm = slicer.app.layoutManager()
    tdWidget = lm.threeDWidget(0)
    tdView = tdWidget.threeDView()
    rWin = tdView.renderWindow()
    rCollection = rWin.GetRenderers()
    renderer = rCollection.GetItemAsObject(0)

    # Add the actors to the renderer, set the background and size
    #
    renderer.AddActor(remActor)


