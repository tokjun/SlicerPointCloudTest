SlicerPointCloudTest
====================

Point cloud demo for 3D Slicer


Useage
======

1. Load .ply file in 3D Slicer. It is loaded as vtkMRMLModelNode, but it won't show up in the viewer. 
2. Check the MRML ID of the model node created in the previous step. If the node is created right after starting 3D Slicer, the ID could be 'vtkMRMLModelNode4".
3. Execute the python script from the Slicer's Python Interactor:
 
  >>> execfile('/home/develop/Development/PointCloud/SlicerPointCloudTest/SlicerPointCloudTest.py')

4. Call the following command with the MRML ID found in the previous step:

  >>> showPointCloud('vtkMRMLModelNode4')



  





