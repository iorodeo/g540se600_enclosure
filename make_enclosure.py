from py2scad import *
from g540se600_enclosure import G540SE600_Enclosure

# Enclosure inner dimensions
x,y,z = 14.0*INCH2MM, 10.0*INCH2MM, 4.0*INCH2MM

fn = 50

params = {

        # Basic enclosure parameters
        'inner_dimensions'           : (x,y,z), 
        'wall_thickness'             : 6.0,              # Check this ....
        'lid_radius'                 : 0.25*INCH2MM,  
        'top_x_overhang'             : 0.375*INCH2MM,
        'top_y_overhang'             : 0.375*INCH2MM,
        'bottom_x_overhang'          : 0.375*INCH2MM,
        'bottom_y_overhang'          : 0.375*INCH2MM, 
        'lid2front_tabs'             : (0.2,0.4,0.6,0.8),
        'lid2side_tabs'              : (0.25,0.5,0.75),
        'side2side_tabs'             : (0.5,),
        'lid2front_tab_width'        : 1.0*INCH2MM,
        'lid2side_tab_width'         : 1.0*INCH2MM, 
        'side2side_tab_width'        : 1.0*INCH2MM,
        'tab_depth_adjust'           : 0.0,
        'standoff_diameter'          : (3.0/8.0)*INCH2MM,
        'standoff_offset'            : 0.05*INCH2MM,
        'standoff_hole_diameter'     : 0.196*INCH2MM, 
        'hole_list'                  : [],

        # Power supply parameters
        'ps_side_hole_panel'         : 'back',
        'ps_side_hole_diameter'      : 3.4,
        'ps_side_hole_spacing_x'     : 220.0,
        'ps_side_hole_spacing_y'     : 20.0,
        'ps_side_hole_rel_pos_x'     : 0.0,
        'ps_side_hole_rel_pos_y'     : -8.25,
        'ps_side_center_x'           : 0.0,
        'ps_side_center_y'           : -0.5*z + 0.5*63.5, 
        'ps_side_hole_info'          : 'M3-thru',

        'ps_bottom_hole_panel'       : 'bottom',
        'ps_bottom_hole_diameter'    : 3.5,
        'ps_bottom_hole_rel_pos_x'   : [-91.2, 116.0, 97.1, -116.0], 
        'ps_bottom_hole_rel_pos_y'   : [54.75, 54.75, -54.75, -54.75],
        'ps_bottom_center_x'         : 0.0,
        'ps_bottom_center_y'         : 0.5*y - 0.5*127.0,
        'ps_bottom_hole_info'        : 'M3-thru',

        # Power cord parameters
        'cord_hole_panel'            : 'left',
        'cord_hole_diameter'         : 0.84*INCH2MM,
        'cord_hole_pos_x'            : 3.8*INCH2MM,
        'cord_hole_pos_y'            : -0.8*INCH2MM,
        'cord_hole_info'             : '1/2-NPT-thru',

        # Fan hole parameters
        'fan_panel'                  : 'right',
        'fan_center_pos_x'           : -2.0*INCH2MM,
        'fan_center_pos_y'           : 0.0*INCH2MM,
        'fan_hole_spacing_x'         : 71.6,
        'fan_hole_spacing_y'         : 71.6,
        'fan_hole_diameter'          : 0.1960*INCH2MM,
        'fan_hole_info'              : '10-32-thru',
        'fan_cutout_diameter'        : 76.5,

        # Gecko drive parameters
        'drive_panel'                : 'front',
        'drive_center_pos_x'         : 0.0,
        'drive_center_pos_y'         : 0.0,
        'drive_cutout_size_x'        : 5.6875*INCH2MM,
        'drive_cutout_size_y'        : 2.41*INCH2MM,
        'drive_cutout_radius'        : 1.0,
        'drive_hole_spacing_x'       : 6.125*INCH2MM,
        'drive_hole_spacing_y'       : 1.5*INCH2MM,
        'drive_hole_diameter'        : 0.144*INCH2MM,
        'drive_hole_info'            : '6-32-thru',

        ## Vent holes
        'vent_hole_panel'            : 'left',
        'vent_hole_diameter'         : 0.375*INCH2MM,
        'vent_hole_spacing_x'        : 0.5*INCH2MM,
        'vent_hole_spacing_y'        : 0.5*INCH2MM,
        'vent_hole_margin_+x'        : 0.5*INCH2MM,
        'vent_hole_margin_-x'        : 1.8*INCH2MM,
        'vent_hole_margin_+y'        : 0.5*INCH2MM,
        'vent_hole_margin_-y'        : 0.5*INCH2MM,
        'mesh_mount_screw_diameter'  : 0.088*INCH2MM,
        'mesh_mount_screw_margin'    : 0.15*INCH2MM, 

        # Cable tie holder holes
        'tie_holder_panel'           : 'bottom',
        'tie_holder_center_pos_x'    : 0.0,
        'tie_holder_center_pos_y'    : -0.5*y + 2.75*INCH2MM,
        'tie_holder_hole_size_x'     : 5.5,
        'tie_holder_hole_size_y'     : 2.5,
        'tie_holder_hole_radius'     : 0.25,
        'tie_holder_hole_spacing_y'  : 15.0,
        'tie_holder_hole_spacing_x'  : 25.0,
        'tie_holder_wall_margin_x'   : 0.5*INCH2MM,
        }

enclosure = G540SE600_Enclosure(params)
enclosure.make()

part_assembly = enclosure.get_assembly(
        explode=(100,100,100),
        show_top=False,
        show_bottom=True,
        show_front=True,
        )
part_projection = enclosure.get_projection()

prog_assembly = SCAD_Prog()
prog_assembly.fn = fn 
prog_assembly.add(part_assembly)
prog_assembly.write('enclosure_assembly.scad')

prog_projection = SCAD_Prog()
prog_projection.fn = fn
prog_projection.add(part_projection)
prog_projection.write('enclosure_projection.scad')
