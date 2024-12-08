import os
import sys
import time

lib_dir = os.path.join(os.path.dirname(__file__), "..", "..")
abs_path = os.path.abspath(lib_dir)
sys.path.extend([abs_path])

import pybullet as pb
import pybullet_data

from icra_maps.common import make_copy_urdf, FLAT_FLOOR_NAME, SEARCH_PATH, get_sphere_path

def main():
    urdf_path = make_copy_urdf(FLAT_FLOOR_NAME)
    client_id = pb.connect(pb.GUI)
    print(pybullet_data.getDataPath())
    pb.setAdditionalSearchPath(pybullet_data.getDataPath(), physicsClientId=client_id)
    # planeId = pb.loadURDF("plane.urdf", physicsClientId=client_id)
    # pb.setAdditionalSearchPath(SEARCH_PATH, physicsClientId=client_id)
    pb.setGravity(0,0,-9.81, physicsClientId=client_id)
    startPos = [0,0,0]
    startOrientation = pb.getQuaternionFromEuler([0,0,0])
    map_id = pb.loadURDF(urdf_path,startPos, startOrientation, physicsClientId=client_id)

    startPos = [0,3,1]
    sphere_id = pb.loadURDF("sphere2red.urdf", startPos, startOrientation, physicsClientId=client_id) 
    loop_rate = 100
    pb.setTimeStep(1/loop_rate, physicsClientId=client_id)
    for i in range (1000):
        pb.stepSimulation(physicsClientId=client_id)
        time.sleep(1/loop_rate)
    sphere_pos, sphere_ori = pb.getBasePositionAndOrientation(sphere_id, physicsClientId=client_id)
    print(sphere_pos,sphere_ori)
    pb.disconnect(physicsClientId=client_id)




if __name__ == "__main__":
    main()