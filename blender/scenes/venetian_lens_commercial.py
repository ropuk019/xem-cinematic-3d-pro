"""Code-only photorealistic desk / camera-lens commercial.
Run with Blender background mode through scripts/render_blender.py.
All scene geometry, materials, lights, typography and animation are procedural.
"""
import bpy, math
from mathutils import Vector

# ---------- reusable procedural primitives ----------
def material(name, color, roughness=.35, metallic=0.0, transmission=0.0, coat=0.0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value=(*color,1); p.inputs['Roughness'].default_value=roughness
    p.inputs['Metallic'].default_value=metallic
    if 'Transmission Weight' in p.inputs: p.inputs['Transmission Weight'].default_value=transmission
    if 'Coat Weight' in p.inputs: p.inputs['Coat Weight'].default_value=coat
    return m

def assign(obj, mat): obj.data.materials.append(mat); return obj

def bevel(obj, width=.025, segments=4):
    mod=obj.modifiers.new('Machined edge highlights','BEVEL'); mod.width=width; mod.segments=segments
    obj.modifiers.new('Weighted corner normals','WEIGHTED_NORMAL'); return obj

def cube(name, loc, dims, mat, edge=.02):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc); o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if edge: bevel(o,edge)
    return assign(o,mat)

def cylinder(name, loc, radius, depth, mat, axis='Z', vertices=96):
    rot=(0,0,0) if axis=='Z' else ((math.pi/2,0,0) if axis=='Y' else (0,math.pi/2,0))
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices, radius=radius, depth=depth, location=loc, rotation=rot)
    o=bpy.context.object; o.name=name; bevel(o,.008,3); return assign(o,mat)

def torus(name, loc, major, minor, mat, axis='Y'):
    rot=(math.pi/2,0,0) if axis=='Y' else (0,0,0)
    bpy.ops.mesh.primitive_torus_add(major_radius=major, minor_radius=minor, major_segments=96, minor_segments=16, location=loc, rotation=rot)
    o=bpy.context.object; o.name=name; return assign(o,mat)

def aim(obj, point): obj.rotation_euler=(Vector(point)-obj.location).to_track_quat('-Z','Y').to_euler()

def area_light(name, loc, target, power, color, size, size_y=None):
    data=bpy.data.lights.new(name,'AREA'); data.energy=power; data.shape='RECTANGLE'; data.size=size
    if size_y is not None: data.size_y=size_y
    ob=bpy.data.objects.new(name,data); bpy.context.collection.objects.link(ob); ob.location=loc; aim(ob,target); return ob

# ---------- materials ----------
def build_scene():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    wood=material('Walnut | satin oiled grain',(.19,.075,.032),.34)
    darkwood=material('Desk edge | dark walnut',(.055,.024,.014),.42)
    black=material('Lens barrel | anodized black',(.012,.017,.023),.24,.72,.0,.35)
    metal=material('Lens rings | brushed titanium',(.38,.43,.48),.2,.92,.0,.25)
    glass=material('Optical glass | coated',(.025,.13,.19),.09,.48,.42,.6)
    rubber=material('Focus grip | rubber',(.012,.014,.016),.78)
    ceramic=material('Warm ivory ceramic',(.72,.59,.43),.2,.0,.0,.25)
    screen=material('Laptop screen | dark glass',(.009,.014,.02),.12,.22,.0,.3)
    silver=material('Laptop | satin aluminum',(.32,.36,.38),.27,.82)
    wall=material('Background plaster',(.16,.115,.085),.9)
    slatmat=material('Blind slats | warm ivory',(.48,.36,.25),.48)
    # walnut desk with a dark fascia
    cube('Desk top',(0,0,.72),(5.8,3.8,.16),wood,.055)
    cube('Desk front fascia',(0,-1.88,.57),(5.8,.08,.24),darkwood,.025)
    for x in (-2.45,2.45): cube('Desk leg',(x,.0,.27),(.13,3.4,.55),darkwood,.025)
    # back wall and window surround
    cube('Rear wall',(0,2.08,2.5),(7,.16,4.2),wall,.02)
    # window aperture represented by dark recess; sun and real slats cast shadows onto desk
    cube('Window recess',(-1.15,1.97,2.45),(2.9,.025,2.55),screen,.01)
    for z in [1.35+i*.17 for i in range(14)]:
        sl=cube('Venetian blind slat',(-1.15,1.82,z),(3.0,.13,.035),slatmat,.012)
        sl.rotation_euler[1]=math.radians(-8)
    # Laptop: aluminum base, keyboard deck, screen shell and dark display
    cube('Laptop lower chassis',(0,-.48,.88),(2.55,1.62,.095),silver,.055)
    cube('Keyboard inset',(0,-.42,.935),(2.25,.78,.018),screen,.018)
    for row in range(5):
        for col in range(14):
            x=-1.02+col*.157; y=-.73+row*.145
            cube('Individual keyboard key',(x,y,.953),(.125,.105,.018),black,.009)
    cube('Trackpad',(0,-1.12,.947),(.92,.48,.012),silver,.025)
    # upright display plane facing camera at back edge
    cube('Display rear shell',(0,.27,1.78),(2.55,.09,1.72),silver,.055)
    cube('Display glass',(0,.215,1.78),(2.39,.018,1.55),screen,.025)
    # Subtle screen typography: all text is generated in Blender
    def text_obj(body, name, loc, size, mat, align='CENTER'):
        cu=bpy.data.curves.new(name,'FONT'); cu.body=body; cu.size=size; cu.align_x=align; cu.extrude=.0008
        ob=bpy.data.objects.new(name,cu); bpy.context.collection.objects.link(ob); ob.location=loc
        ob.rotation_euler=(math.pi/2,0,0); return assign(ob,mat)
    type_mat=material('Screen typography | warm amber',(1.0,.34,.12),.5,.0)
    text_obj('LIGHT','Screen title',(-.83,.194,2.22),.17,type_mat,'LEFT')
    text_obj('sun through / blinds','Screen subtitle',(-.83,.194,1.93),.095,ceramic,'LEFT')
    # Hero camera lens on foreground right, with actual nested optical components
    root=bpy.data.objects.new('HERO LENS | animated rig',None); bpy.context.collection.objects.link(root); root.location=(1.05,-.55,.98)
    def parent(obj): obj.parent=root; return obj
    parent(cylinder('Lens main barrel',(0,0,0),.48,.92,black,'Y'))
    parent(cylinder('Front filter ring',(0,-.49,0),.49,.10,metal,'Y'))
    parent(cylinder('Front gasket',(0,-.55,0),.425,.035,rubber,'Y'))
    parent(cylinder('Optical front element',(0,-.575,0),.39,.025,glass,'Y'))
    for r,minor,y,ma in [(.465,.018,-.555,metal),(.405,.009,-.592,metal),(.31,.008,-.594,glass),(.22,.006,-.595,metal)]:
        parent(torus('Precision concentric lens ring',(0,y,0),r,minor,ma,'Y'))
    # knurled grip rings and engraved band
    for i in range(48):
        a=2*math.pi*i/48
        rib=cube('Focus ring knurl',(0,0,0),(.024,.24,.025),metal,.006)
        rib.location=(.475*math.cos(a),-.02,.475*math.sin(a)); rib.rotation_euler[1]=-a; parent(rib)
    for y in (-.27,.18,.31): parent(torus('Barrel seam',(0,y,0),.468,.009,metal,'Y'))
    # aperture blades hinted behind the front element, generated radially
    for i in range(9):
        a=2*math.pi*i/9
        blade=cube('Aperture blade',(0,-.603,0),(.19,.008,.018),black,.004)
        blade.location=(.12*math.cos(a),-.603,.12*math.sin(a)); blade.rotation_euler[1]=-a; parent(blade)
    # coffee cup and saucer, plus handle torus
    cylinder('Cup body',(-1.72,-.28,.99),.29,.48,ceramic,'Z')
    cylinder('Cup coffee',(-1.72,-.28,1.235),.255,.012,material('Espresso surface',(.055,.021,.009),.16), 'Z')
    torus('Cup handle',(-2.02,-.28,1.02),.16,.045,ceramic,'Y')
    cylinder('Cup saucer',(-1.72,-.28,.79),.39,.045,ceramic,'Z')
    # small styling prop: notebook and pen
    cube('Notebook',(2.15,.55,.84),(.85,1.1,.08),darkwood,.025)
    cube('Notebook paper',(2.15,.55,.89),(.79,1.03,.018),ceramic,.012)
    cylinder('Pen body',(2.12,.42,.94),.018,.9,black,'Z',32)
    # Environment / physically motivated lighting. Sun angle creates slat shadows.
    sun_data=bpy.data.lights.new('SUN | late afternoon through blinds','SUN'); sun_data.energy=2.2; sun_data.angle=math.radians(.35)
    sun=bpy.data.objects.new('SUN | late afternoon through blinds',sun_data); bpy.context.collection.objects.link(sun)
    sun.location=(-3.5,1.5,5.5); aim(sun,(1.3,-1.2,.6))
    area_light('KEY | warm window bounce',(-3.2,-1.0,4.3),(0,-.2,1),380,(1.0,.62,.34),3.5,2.0)
    area_light('FILL | soft cool room',(3.2,-3.5,3.2),(1,-.3,1),110,(.48,.62,1.0),3.0,2.0)
    area_light('RIM | lens edge strip',(2.8,1.0,2.8),(1,-.5,1),520,(1.0,.48,.22),.45,2.2)
    area_light('TOP | subtle ambient card',(0,-.1,5.5),(0,0,0),180,(1.0,.82,.62),4.0,2.0)
    world=bpy.data.worlds.new('XEM | warm interior world') if not bpy.data.worlds else bpy.data.worlds[0]
    bpy.context.scene.world=world; world.use_nodes=True
    world.node_tree.nodes['Background'].inputs['Color'].default_value=(.16,.105,.065,1)
    world.node_tree.nodes['Background'].inputs['Strength'].default_value=.22
    # Camera: wide establishing -> slow macro push -> lens hero close-up
    camdata=bpy.data.cameras.new('Cinematic macro camera'); cam=bpy.data.objects.new('Cinematic macro camera',camdata)
    bpy.context.collection.objects.link(cam); bpy.context.scene.camera=cam; camdata.lens=48
    camdata.dof.use_dof=True; camdata.dof.aperture_fstop=2.2
    def camera_key(frame, loc, target, lens, focus):
        cam.location=loc; aim(cam,target); camdata.lens=lens
        focus_obj=camdata.dof.focus_object
        if focus_obj is None:
            focus_obj=bpy.data.objects.new('Camera focus target',None); bpy.context.collection.objects.link(focus_obj); camdata.dof.focus_object=focus_obj
        focus_obj.location=focus; focus_obj.keyframe_insert(data_path='location',frame=frame)
        cam.keyframe_insert(data_path='location',frame=frame); cam.keyframe_insert(data_path='rotation_euler',frame=frame); camdata.keyframe_insert(data_path='lens',frame=frame)
    camera_key(1,(4.7,-8.8,3.4),(0,-.15,1.15),48,(0,-.3,1.0))
    camera_key(150,(3.8,-7.2,2.8),(.6,-.4,1.0),55,(.9,-.5,1.0))
    camera_key(300,(2.7,-4.2,1.9),(1.0,-.55,1.0),78,(1.05,-.55,1.0))
    camera_key(450,(2.35,-3.2,1.55),(1.05,-.55,1.0),92,(1.05,-.55,1.0))
    root.rotation_euler[2]=math.radians(-12); root.keyframe_insert(data_path='rotation_euler',frame=1)
    root.rotation_euler[2]=math.radians(5); root.keyframe_insert(data_path='rotation_euler',frame=450)
    for obj in (cam,root,camdata.dof.focus_object):
        if obj.animation_data and obj.animation_data.action:
            for fc in obj.animation_data.action.fcurves:
                for key in fc.keyframe_points:
                    key.interpolation='BEZIER'; key.handle_left_type='AUTO_CLAMPED'; key.handle_right_type='AUTO_CLAMPED'
    scene=bpy.context.scene; scene.frame_start=1; scene.frame_end=450; scene.render.fps=30
    scene.render.resolution_x=1920; scene.render.resolution_y=1080; scene.render.resolution_percentage=100
    scene.render.engine='CYCLES'; scene.cycles.samples=96; scene.cycles.use_denoising=True
    scene.view_settings.view_transform='AgX'; scene.view_settings.look='AgX - Medium High Contrast'
    scene.render.image_settings.file_format='PNG'
    scene.render.film_transparent=False
    scene.frame_set(1)

if __name__=='__main__': build_scene()
