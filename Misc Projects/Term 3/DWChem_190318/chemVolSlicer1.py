# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 11:21:33 2018

@author: TTM
"""
import os
os.environ['QT_API'] = 'pyqt'
os.environ['ETS_TOOLKIT'] = 'qt4'
print('done------------------------------------------')


#--------------------------------------Note: The hydrogen_wave_func code is all in py3-----
from scipy.misc import derivative
import math
from sympy import *
import numpy as np
import scipy.constants as c

from tvtk.api import tvtk
from tvtk.pyface.scene import Scene

from traits.api import HasTraits, Instance, Array, \
    on_trait_change
from traitsui.api import View, Item, HGroup, Group

from mayavi import mlab
from mayavi.core.api import PipelineBase, Source
from mayavi.core.ui.api import SceneEditor, MayaviScene, \
                                MlabSceneModel

def spherical_to_cartesian(r,theta,phi):
    x = round(r*np.sin(theta)*np.cos(phi),5)
    y = round(r*np.sin(theta)*np.sin(phi),5)
    z = round(r*np.cos(phi),5)
    return (x,y,z)

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2+y**2+z**2)
    theta = np.arccos(z/np.sqrt(x**2+y**2+z**2))
    phi = np.arctan2(y,x)
    return r,theta,phi

def absolute(cn):
    absol = np.sqrt((np.real(cn))**2 + (np.imag(cn))**2)
    return absol

def angular_wave_func(m,l,theta,phi):
    if l == 0:
        if m == 0:
            ans = np.sqrt(1/(4*c.pi))
    elif l == 1:
        if m == 0:
            ans = np.sqrt(3/(4*c.pi)) * np.cos(theta)
        elif m == 1:
            ans = -np.sqrt(3/(8*c.pi))*np.sin(theta)*np.exp(phi*1j)
        elif m == -1:
            ans = np.sqrt(3/(8*c.pi))*np.sin(theta)*np.exp(phi*-1j)
    elif l == 2:
        if m == 0: # l=2, m=0
            ans = np.sqrt(5/(16*c.pi))*(3*(np.cos(theta)**2)-1)
        elif m == 1: # l=2, m= +1
            ans = -np.sqrt(15/(8*c.pi))*np.cos(theta)*np.sin(theta)*np.exp(phi*1j)
        elif m == 2: # l=2, m= +2
            ans = np.sqrt(15/(32*c.pi))*(np.sin(theta)**2)*np.exp(phi*2j)
        elif m == -1: # l=2, m= -1
            ans = np.sqrt(15/(8*c.pi))*np.cos(theta)*np.sin(theta)*np.exp(phi*-1j)
        elif m == -2: # l=2, m= -2
            ans = np.sqrt(15/(32*c.pi))*(np.sin(theta)**2)*np.exp(phi*-2j)
    return ans

def radial_wave_func(n,l,r):
    #print('---------------------------------------')
    #print('a: {0}'.format(a))
    #print('r: {0}'.format(r))
    if n == 1: # If n = 1
        if l == 0:
            R = ((2/np.sqrt(a**3)) * np.exp(-r/a) / a(-3/2))
    elif n == 2:
        if l == 0:
            R = (1/np.sqrt(2)) * (a**(-3/2)) * (1-(r/(2*a))) * (np.exp(-r/(2*a))) / (a**(-3/2))
        elif l == 1:
            R = ((1/np.sqrt(24)) * (a**(-3/2)) * (r/a) * np.exp(-r/(2*a)) / a**(-3/2))
    elif n == 3:
        if l == 0:
            R = (2/81*np.sqrt(2)) * (a**(-3/2)) * ((27-18)*(r/a)+2*(r/a)*2) * (np.exp(-r/(3*a))) / (a**(-3/2))
            ############################################################^here###
        elif l == 1:
            R = (8/(27*np.sqrt(6))) * (a**(-3/2)) * (((1-(r/(6*a)))*(r/a))) * (np.exp(-r/(3*a))) / (a**(-3/2))
        elif l == 2:
            R = (4/(81*np.sqrt(30))) * (a**(-3/2)) * (r/a)*2 * (np.exp(-r/(3*a))) / (a**(-3/2))
            ##############################################^here####
    return R


def linspace(start, stop, num=50):
    step = (stop - start)/(num-1)
    space = []
    if not num:
        step = (stop - start)/(49)
        for i in range(num ):
            space.append(start + step * i)
    for i in range(num ):
        space.append(round(start + step * i, 5))
    return space



def meshgrid(x,y,z):
    row1 = []
    for h in range(len(y)):
        second_list = []
        for i in range(len(x)):
            inner_list = []
            for j in range(len(z)):
                inner_list.append(float(x[i]))
            second_list.append(inner_list)
        row1.append(second_list)
    row2 = []
    for i in range(len(y)):
        inner_list = []
        second_list = []
        for j in range(len(z)):
            inner_list.append(float(y[i]))
        for k in range(len(x)):
            second_list.append(inner_list)
        row2.append(second_list)
    row3 = []
    for h in range(len(y)):
        second_list = []
        for i in range(len(x)):
            inner_list = []
            for j in range(len(z)):
                inner_list.append(float(z[j]))
            second_list.append(inner_list)
        row3.append(second_list)
    return (row1,row2,row3)


vspherical = np.vectorize(cartesian_to_spherical)
vangular = np.vectorize(angular_wave_func)
vradial = np.vectorize(radial_wave_func)
vabs = np.vectorize(absolute)
vround=np.vectorize(round)
a=c.physical_constants['Bohr radius'][0]
def hydrogen_wave_func(n,l, m, roa, Nx, Ny, Nz):
    xx, yy, zz = np.mgrid[-roa:roa:(Nx*1j),-roa:roa:(Ny*1j),-roa:roa:(Nz*1j)]

    r, theta, phi = vspherical(xx, yy, zz)

    if m == 0:
        angular = vangular(m,l,theta,phi)

    elif m > 0:
        angular = (1/np.sqrt(2))*(vangular(-m,l,theta,phi)+(-1)**m*vangular(m,l,theta,phi))

    elif m < 0:
        angular = (1j/np.sqrt(2))*(vangular(m,l,theta,phi)-(-1)**m*vangular(-m,l,theta,phi))

    radial = vradial(n,l,r*a)
    mag = vabs(radial * angular)**2
    return np.round(mag,5)


class VolumeSlicer(HasTraits):
    # The data to plot
    data = hydrogen_wave_func(3,0,0,20,150,150,150)

    # The 4 views displayed
    scene3d = Instance(MlabSceneModel, ())
    scene_x = Instance(MlabSceneModel, ())
    scene_y = Instance(MlabSceneModel, ())
    scene_z = Instance(MlabSceneModel, ())

    # The data source
    data_src3d = Instance(Source)

    # The image plane widgets of the 3D scene
    ipw_3d_x = Instance(PipelineBase)
    ipw_3d_y = Instance(PipelineBase)
    ipw_3d_z = Instance(PipelineBase)

    _axis_names = dict(x=0, y=1, z=2)


    #---------------------------------------------------------------------------
    def __init__(self, **traits):
        super(VolumeSlicer, self).__init__(**traits)
        # Force the creation of the image_plane_widgets:
        self.ipw_3d_x
        self.ipw_3d_y
        self.ipw_3d_z


    #---------------------------------------------------------------------------
    # Default values
    #---------------------------------------------------------------------------
    def _data_src3d_default(self):
        return mlab.pipeline.scalar_field(self.data,
                            figure=self.scene3d.mayavi_scene)

    def make_ipw_3d(self, axis_name):
        ipw = mlab.pipeline.image_plane_widget(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        plane_orientation='%s_axes' % axis_name)
        return ipw

    def _ipw_3d_x_default(self):
        return self.make_ipw_3d('x')

    def _ipw_3d_y_default(self):
        return self.make_ipw_3d('y')

    def _ipw_3d_z_default(self):
        return self.make_ipw_3d('z')


    #---------------------------------------------------------------------------
    # Scene activation callbaks
    #---------------------------------------------------------------------------
    @on_trait_change('scene3d.activated')
    def display_scene3d(self):
        outline = mlab.pipeline.outline(self.data_src3d,
                        figure=self.scene3d.mayavi_scene,
                        )
        self.scene3d.mlab.view(40, 50)
        # Interaction properties can only be changed after the scene
        # has been created, and thus the interactor exists
        for ipw in (self.ipw_3d_x, self.ipw_3d_y, self.ipw_3d_z):
            # Turn the interaction off
            ipw.ipw.interaction = 0
        self.scene3d.scene.background = (0, 0, 0)
        # Keep the view always pointing up
        self.scene3d.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleTerrain()
        #mlab.axes()


    def make_side_view(self, axis_name):
        scene = getattr(self, 'scene_%s' % axis_name)

        # To avoid copying the data, we take a reference to the
        # raw VTK dataset, and pass it on to mlab. Mlab will create
        # a Mayavi source from the VTK without copying it.
        # We have to specify the figure so that the data gets
        # added on the figure we are interested in.
        outline = mlab.pipeline.outline(
                            self.data_src3d.mlab_source.dataset,
                            figure=scene.mayavi_scene,
                            )
        ipw = mlab.pipeline.image_plane_widget(
                            outline,
                            plane_orientation='%s_axes' % axis_name)
        setattr(self, 'ipw_%s' % axis_name, ipw)

        # Synchronize positions between the corresponding image plane
        # widgets on different views.
        ipw.ipw.sync_trait('slice_position',
                            getattr(self, 'ipw_3d_%s'% axis_name).ipw)

        # Make left-clicking create a crosshair
        ipw.ipw.left_button_action = 0
        # Add a callback on the image plane widget interaction to
        # move the others
        def move_view(obj, evt):
            position = obj.GetCurrentCursorPosition()
            for other_axis, axis_number in self._axis_names.items():
                if other_axis == axis_name:
                    continue
                ipw3d = getattr(self, 'ipw_3d_%s' % other_axis)
                ipw3d.ipw.slice_position = position[axis_number]

        ipw.ipw.add_observer('InteractionEvent', move_view)
        ipw.ipw.add_observer('StartInteractionEvent', move_view)

        # Center the image plane widget
        ipw.ipw.slice_position = 0.5*self.data.shape[
                    self._axis_names[axis_name]]

        # Position the view for the scene
        views = dict(x=( 0, 90),
                     y=(90, 90),
                     z=( 0,  0),
                     )
        scene.mlab.view(*views[axis_name])
        # 2D interaction: only pan and zoom
        scene.scene.interactor.interactor_style = \
                                 tvtk.InteractorStyleImage()
        scene.scene.background = (0, 0, 0)
        #mlab.axes()


    @on_trait_change('scene_x.activated')
    def display_scene_x(self):
        return self.make_side_view('x')

    @on_trait_change('scene_y.activated')
    def display_scene_y(self):
        return self.make_side_view('y')

    @on_trait_change('scene_z.activated')
    def display_scene_z(self):
        return self.make_side_view('z')


    #---------------------------------------------------------------------------
    # The layout of the dialog created
    #---------------------------------------------------------------------------
    view = View(HGroup(
                  Group(
                       Item('scene_y',
                            editor=SceneEditor(scene_class=MayaviScene),
                            height=250, width=300),
                       Item('scene_z',
                            editor=SceneEditor(scene_class=MayaviScene),
                            height=250, width=300),
                       show_labels=True,
                  ),
                  Group(
                       Item('scene_x',
                            editor=SceneEditor(scene_class=MayaviScene),
                            height=250, width=300),
                       Item('scene3d',
                            editor=SceneEditor(scene_class=MayaviScene),
                            height=250, width=300),
                       show_labels=True,
                  ),
                ),
                resizable=True,
                title='Volume Slicer',
                )


m = VolumeSlicer()
m.configure_traits()       
 

