import os
import tempfile
from typing import Optional

ICRA_FOLDER_NAMES = ["ICRA2024_Quadruped_Robot_Challenges", "ICRA2024_QRC_Simulation_Map"]
MESH_FOLDER = "meshes"
URDF_FOLDER = "urdf"

FILE_DIR = os.path.dirname(__file__)

SEARCH_PATH = os.path.join(FILE_DIR, "ICRA2024_Quadruped_Robot_Challenges")
URDF_PATH = os.path.join(FILE_DIR, *ICRA_FOLDER_NAMES, URDF_FOLDER)
MESH_PATH = os.path.join(os.path.dirname(URDF_PATH), MESH_FOLDER)

SLANTED_FLOOR_NAME = "map_sloped.urdf"
FLAT_FLOOR_NAME = "map_flat.urdf"

def get_sphere_path():
    sphere_path = os.path.join(FILE_DIR, "small_sphere.urdf")
    return sphere_path

def make_copy_urdf(urdf_name: str, out_dir_name: Optional[str] = None):
    if out_dir_name is None:
        out_dir_name = FILE_DIR
    new_file = os.path.join(out_dir_name, urdf_name)
    old_file = os.path.join(URDF_PATH, urdf_name)
    with open(new_file, "w") as file_handle:
        old_file_str = ""
        with open(old_file, "r") as old_file_handle:
            old_file_str = old_file_handle.read()
        old_file_str = old_file_str.replace("package://ICRA2024_Quadruped_Competition", SEARCH_PATH + "/ICRA2024_QRC_Simulation_Map")
        file_handle.write(old_file_str)
    return new_file
        

if __name__ == "__main__":
    make_copy_urdf(FLAT_FLOOR_NAME)