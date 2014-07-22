## PARAMETERS 

case_name = "darcy_impes_mms_p1_2phase_coreyrelperm" 
mesh_type_list = ['reg']
mesh_res_list_1D = ['10', '20', '40', '80']
mesh_res_list_2D = ['10', '20', '40']
mesh_res_list_3D = []                       # [3]
field_list = ['Phase1::Pressure', 
              'Phase2::Saturation']         # [1]
norm_list = ['2']

reference_mesh_res = 5
reference_timestep_number = 10                  # [1]

command_line_in_xml = 'python processing.py pre proc post clean'

# [see also note 2]


## SCRIPT

from sys import argv, exit, path
path.append('../darcy_impes_common')

if len(argv)==1:
    print("""\nRun this script with one or more of the following arguments:
    xml - make an xml file for the test harness
    gen - generate source terms etc. using solution_generator.py
    pre - preprocess (generate meshes and options files)
    proc - process (run simulations)
    post - postprocess (write convergence rates)
    all - all of the above
    clean - clean everything no longer needed by the test harness
            (*.geo, *.msh, *.diml, *.vtu)""")
    exit()


# initialise helper object
from manufactured_solution_test_tools import ManufacturedSolutionTestSuite
test_helper = ManufacturedSolutionTestSuite(
    case_name, mesh_type_list, [mesh_res_list_1D, mesh_res_list_2D,
    mesh_res_list_3D], field_list, norm_list, 
    reference_mesh_res, reference_timestep_number,
    command_line_in_xml, python_layer_verbosity=1)

# pass client commands
for arg in argv[1:]:
    test_helper.do(arg)


# Notes:
# 
# [1] the starting number of timesteps has been increased to 10 because
#     with too few, the rates can look OK even for bad convergence
#     (TODO: check impact on total test time).
# 
# [2] velocity boundary conditions were supposed to be tested in this
#     folder, but there are convergence problems when the BCs are
#     non-zero.
#
# [3] Current problem with 3D simulations in this folder.  When running the
#     simulator, get:
#     Option shape error. Key is: /material_phase[1]/scalar_field::Saturation/prognostic/scalar_field::Source/prescribed/value[0]/python 
