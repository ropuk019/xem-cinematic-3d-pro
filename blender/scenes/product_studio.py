import bpy, math
from mathutils import Vector

def mat(name, color, metallic=0.0, rough=0.3, coat=0.0, transmission=0.0):
    m=bpy.data.materials.new(name); m.diffuse_color=(*color,1); m.use_nodes=True
    p=m.node_tree.nodes.get("Principled BSDF")
    p.inputs["Base Color"].default_value=(*color,1); p.inputs["Metallic"].default_value=metallic
    p.inputs["Roughness"].default_value=rough
    if "Coat Weight" in p.inputs: p.inputs["Coat Weight"].default_value=coat
    if "Transmission Weight" in p.inputs: p.inputs["Transmission Weight"].default_value=transmission
    return m

def put(o,m): o.data.materials.append(m); return o
def bevel(o,w=.06,s=5):
    b=o.modifiers.new("Precision bevel","BEVEL"); b.width=w; b.segments=s
    n=o.modifiers.new("Weighted normals","WEIGHTED_NORMAL"); n.keep_sharp=True
    return o
def cube(name,loc,dim,material,r=.05):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc); o=bpy.context.object; o.name=name
    o.dimensions=dim; bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if r: bevel(o,r)
    return put(o,material)
def cyl(name,loc,radius,depth,material,rot=(math.pi/2,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=96,radius=radius,depth=depth,location=loc,rotation=rot)
    o=bpy.context.object; o.name=name; bevel(o,.018,4); return put(o,material)
def tor(name,loc,major,minor,material,rot=(math.pi/2,0,0)):
    bpy.ops.mesh.primitive_torus_add(major_radius=major,minor_radius=minor,major_segments=96,minor_segments=16,location=loc,rotation=rot)
    return put(bpy.context.object,material)
def aim(o,target): o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler()
def area(name,loc,target,power,color,size,size_y):
    d=bpy.data.lights.new(name,'AREA'); d.energy=power; d.shape='RECTANGLE'; d.size=size; d.size_y=size_y
    o=bpy.data.objects.new(name,d); bpy.context.collection.objects.link(o); o.location=loc; aim(o,target); return o

def build_scene():
    bpy.ops.object.select_all(action='SELECT'); bpy.ops.object.delete(use_global=False)
    graphite=mat("Ceramic graphite",(0.045,.06,.085),.68,.23,.5)
    titanium=mat("Brushed titanium",(.42,.49,.58),.94,.27,.22)
    black=mat("Rubber gasket",(.008,.012,.018),0,.78)
    glass=mat("Optical blue glass",(.02,.2,.34),.25,.12,.7,.25)
    floor_mat=mat("Satin charcoal floor",(.025,.032,.045),.18,.32)
    # Subtle floor microtexture
    nt=floor_mat.node_tree; noise=nt.nodes.new("ShaderNodeTexNoise"); noise.inputs["Scale"].default_value=180
    bump=nt.nodes.new("ShaderNodeBump"); bump.inputs["Strength"].default_value=.055; bump.inputs["Distance"].default_value=.008
    nt.links.new(noise.outputs["Fac"],bump.inputs["Height"])
    nt.links.new(bump.outputs["Normal"],nt.nodes.get("Principled BSDF").inputs["Normal"])
    root=bpy.data.objects.new("HERO | animated product",None); bpy.context.collection.objects.link(root); root.location=(0,0,1.60)
    def parent(o): o.parent=root; return o
    parent(cube("Main chassis",(0,0,0),(2.5,.55,3.0),graphite,.23))
    parent(cube("Titanium face surround",(0,-.29,.1),(2.28,.075,2.72),titanium,.19))
    parent(cube("Inset front panel",(0,-.34,.1),(2.15,.05,2.59),graphite,.16))
    parent(cyl("Lens outer ring",(0,-.405,.42),.72,.12,titanium))
    parent(cyl("Lens gasket",(0,-.48,.42),.63,.08,black))
    parent(cyl("Optical glass",(0,-.535,.42),.56,.045,glass))
    parent(tor("Lens etched ring",(0,-.563,.42),.48,.012,titanium))
    parent(tor("Inner lens ring",(0,-.565,.42),.34,.007,glass))
    for i in range(3):
        z=-.72-i*.22
        parent(cube("Status slot",(0.74,-.38,z),(.1,.025,.055),titanium,.018))
    parent(cyl("Top control",(.78,-.03,1.56),.15,.13,titanium,rot=(0,0,0)))
    parent(cyl("Top control inset",(.78,-.03,1.64),.085,.03,black,rot=(0,0,0)))
    for x in (-.78,.78): parent(cyl("Rubber foot",(x,0,-1.55),.13,.1,black,rot=(0,0,0)))
    for x in (-1.08,1.08): parent(cube("Side seam",(x,0,0),(.018,.34,2.25),titanium,.008))
    bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,0)); put(bpy.context.object,floor_mat).name="Shadow receiving studio floor"
    world=bpy.data.worlds.new("XEM Studio") if not bpy.data.worlds else bpy.data.worlds[0]
    bpy.context.scene.world=world; world.use_nodes=True
    world.node_tree.nodes["Background"].inputs["Color"].default_value=(.12,.15,.21,1)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value=.24
    area("KEY | overhead softbox",(1.5,-4.5,7),(0,0,1.2),1100,(.78,.86,1),5,3)
    area("FILL | cool card",(-4,-3,2.6),(0,0,1.2),460,(.38,.58,1),3.5,4)
    area("RIM | warm strip",(2.5,3,4.8),(0,0,1.5),1500,(1,.48,.24),1.0,5)
    area("EDGE | cyan strip",(-3.5,0,3),(0,0,1.5),820,(.26,.75,1),.8,4.5)
    area("TOP | narrow reflection",(0,2,7),(0,0,1.2),650,(1,1,1),3,.8)
    cd=bpy.data.cameras.new("Hero camera"); cam=bpy.data.objects.new("Hero camera",cd); bpy.context.collection.objects.link(cam)
    cam.location=(4.8,-9,4.4); aim(cam,(0,0,1.55)); cd.lens=58; cd.dof.use_dof=True
    cd.dof.focus_object=root; cd.dof.aperture_fstop=5.6; bpy.context.scene.camera=cam
    root.rotation_euler[2]=math.radians(-12); root.keyframe_insert(data_path="rotation_euler",frame=1)
    root.rotation_euler[2]=math.radians(24); root.keyframe_insert(data_path="rotation_euler",frame=240)
    cam.location=(4.8,-9,4.4); cam.keyframe_insert(data_path="location",frame=1)
    cam.location=(4.35,-8.2,4.1); cam.keyframe_insert(data_path="location",frame=240)
    for obj in (root,cam):
        if obj.animation_data and obj.animation_data.action:
            for fc in obj.animation_data.action.fcurves:
                for k in fc.keyframe_points: k.interpolation='BEZIER'; k.handle_left_type='AUTO_CLAMPED'; k.handle_right_type='AUTO_CLAMPED'
    scene=bpy.context.scene; scene.frame_start=1; scene.frame_end=240; scene.render.fps=30
    scene.render.resolution_x=1920; scene.render.resolution_y=1080; scene.render.resolution_percentage=100
    scene.render.engine='BLENDER_EEVEE_NEXT'
    scene.view_settings.view_transform='AgX'; scene.view_settings.look='AgX - Medium High Contrast'
    scene.use_nodes=True; tree=scene.node_tree; tree.nodes.clear()
    rl=tree.nodes.new("CompositorNodeRLayers"); glare=tree.nodes.new("CompositorNodeGlare")
    glare.glare_type='FOG_GLOW'; glare.quality='MEDIUM'; glare.threshold=1.8; glare.size=7
    comp=tree.nodes.new("CompositorNodeComposite"); tree.links.new(rl.outputs["Image"],glare.inputs["Image"])
    tree.links.new(glare.outputs["Image"],comp.inputs["Image"])
    scene.frame_set(1)
if __name__=="__main__": build_scene()
