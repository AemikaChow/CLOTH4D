import os
import sys
import cv2
import numpy as np

data_folder = 'Your root that stores the export obj files from blender'
file_list = os.listdir(data_folder)

count = 0

for id in file_list:
    if os.path.splitext(id)[1] == '.obj':
        obj_id = os.path.splitext(id)[0]
        # clo3d_obj_folder = os.path.join(data_folder, obj_id)
        clo3d_obj_file = os.path.join(data_folder,  obj_id + ".obj")

        clo3d_mtl_file = os.path.join(data_folder, obj_id + ".mtl")

        # UV names of different CLO3D projects may differ.
        clo3d_clothing_uv = os.path.join(data_folder, "1_diffuse_1001.png")
        # clo3d_clothing_uv_normal = os.path.join(data_folder, "1_normal_1001.png")
        face_uv = os.path.join(data_folder, "face.jpg")
        body_uv = os.path.join(data_folder, "body_Covered_Beige.jpg")
        arm_uv = os.path.join(data_folder, "arm.jpg")
        leg_uv = os.path.join(data_folder, "leg.jpg")
        eye_uv = os.path.join(data_folder, "eye.jpg")
        eyelash_uv = os.path.join(data_folder, "eyelash.jpg")
        pump_uv = os.path.join(data_folder, "FV2_Open_Toe_Pump.jpg")
        hair_uv = os.path.join(data_folder, "hair_01.jpg")
        tooth_uv = os.path.join(data_folder, "tooth.jpg")
        transparency_uv = os.path.join(data_folder, "transparency.png")

        # Check if these file exists.
        assert os.path.isfile(clo3d_obj_file)
        assert os.path.isfile(clo3d_mtl_file)
        assert os.path.isfile(clo3d_clothing_uv)
        # assert os.path.isfile(clo3d_clothing_uv_normal)
        assert os.path.isfile(face_uv)
        assert os.path.isfile(body_uv)
        assert os.path.isfile(arm_uv)
        assert os.path.isfile(leg_uv)
        assert os.path.isfile(eye_uv)
        assert os.path.isfile(eyelash_uv)
        assert os.path.isfile(pump_uv)
        assert os.path.isfile(hair_uv)
        assert os.path.isfile(tooth_uv)
        assert os.path.isfile(transparency_uv)

        # Step 1: Re-arrage the UVs into a unified UV
        tex_size = 4096
        assert tex_size % 8 == 0, "Texture size has to be a multiplier of 8."
        unified_uv = 255 * np.ones((tex_size, tex_size, 4), np.float32)
        unified_uv_file = os.path.join(data_folder, obj_id + "_uv.png")

        unified_uv[: tex_size // 4, : tex_size // 4, :3] = cv2.resize(
            cv2.imread(face_uv), (tex_size // 4, tex_size // 4)
        )
        unified_uv[tex_size // 4 : tex_size // 2, : tex_size // 4, :3] = cv2.resize(
            cv2.imread(body_uv), (tex_size // 4, tex_size // 4)
        )
        unified_uv[tex_size // 2 : tex_size // 4 * 3, : tex_size // 4, :3] = cv2.resize(
            cv2.imread(arm_uv), (tex_size // 4, tex_size // 4)
        )
        unified_uv[tex_size // 4 * 3 :, : tex_size // 4, :3] = cv2.resize(
            cv2.imread(leg_uv), (tex_size // 4, tex_size // 4)
        )
        unified_uv[
            : tex_size // 8, tex_size // 4 : tex_size // 4 + tex_size // 8, :3
        ] = cv2.resize(cv2.imread(eye_uv), (tex_size // 8, tex_size // 8))
        unified_uv[
            tex_size // 8 : tex_size // 4, tex_size // 4 : tex_size // 4 + tex_size // 8, :3
        ] = cv2.resize(cv2.imread(eyelash_uv), (tex_size // 8, tex_size // 8))
        unified_uv[: tex_size // 8, tex_size // 4 + tex_size // 8 : tex_size // 2] = cv2.resize(
            cv2.imread(transparency_uv, cv2.IMREAD_UNCHANGED), (tex_size // 8, tex_size // 8)
        )
        unified_uv[: tex_size // 4, tex_size // 2 : tex_size // 4 * 3, :3] = cv2.resize(
            cv2.imread(hair_uv), (tex_size // 4, tex_size // 4)
        )
        unified_uv[: tex_size // 4, tex_size // 4 * 3 :, :3] = cv2.resize(
            cv2.imread(pump_uv), (tex_size // 4, tex_size // 4)
        )

        unified_uv[tex_size // 4 :, tex_size // 4 :] = cv2.resize(
            cv2.imread(clo3d_clothing_uv, cv2.IMREAD_UNCHANGED),
            (tex_size // 4 * 3, tex_size // 4 * 3),
        )

        # unified_uv[tex_size // 4 :, tex_size // 4 :] = cv2.resize(
        #     cv2.imread(clo3d_clothing_uv_normal, cv2.IMREAD_UNCHANGED),
        #     (tex_size // 4 * 3, tex_size // 4 * 3),
        # )
        cv2.imwrite(unified_uv_file, unified_uv)


        # Step 2: change the obj file
        unified_uv_obj_file = os.path.join(data_folder, obj_id + "_uv.obj")
        unified_uv_mtl_file = os.path.join(data_folder, obj_id + "_uv.mtl")
        with open(unified_uv_mtl_file, "w") as f:
            f.write(
                "\n".join(
                    [
                        "newmtl Material",
                        "Ka 0.257132 0.257132 0.257132",
                        "Kd 1.000000 1.000000 1.000000",
                        "Ks 0.058500 0.058500 0.058500",
                        "Ns 16.000000",
                        "illum 2",
                        "d 1.000000",
                        "map_Ka " + obj_id + "_uv.png",
                        "map_Kd " + obj_id + "_uv.png",
                    ]
                )
            )


        all_vts = []  # We need to change all vts to coop with the unified UV.
        for line in open(clo3d_obj_file).read().splitlines():
            if line.startswith("vt "):
                u, v = line.split()[1:]
                all_vts.append(
                    [float(u), float(v), False]
                )  # Insert a changed flag to check if th vt has been changed.


        unified_uv_lines = []
        current_material = None
        for line in open(clo3d_obj_file).read().splitlines():
            if line.startswith("mtllib"):
                unified_uv_lines.append("mtllib " + obj_id + "_uv.mtl")
            elif line.startswith("usemtl"):
                unified_uv_lines.append("usemtl Material")  # Change it to a unified materila.
                current_material = line.split()[1]
            elif line.startswith("f "):
                # Loop all faces and change the corresponding vts.
                for face in line.split()[1:]:
                    vt_idx = int(face.split("/")[1]) - 1  # Face idx starts with 1
                    # If it has not been modified, modify it.
                    if all_vts[vt_idx][2]:
                        continue
                    # Change verts UV according to current material.
                    if current_material == "Mara:face2.002":  # face
                        all_vts[vt_idx][0] = all_vts[vt_idx][0] / 4
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 4 + 0.75
                    elif current_material == "Mara:body3.002":  # body
                        all_vts[vt_idx][0] = (all_vts[vt_idx][0] - 1) / 4
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 4 + 0.5
                    elif current_material == "Mara:arm2.002":  # arm
                        all_vts[vt_idx][0] = (all_vts[vt_idx][0] - 2) / 4
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 4 + 0.25
                    elif current_material == "Mara:leg2.002":  # leg
                        all_vts[vt_idx][0] = (all_vts[vt_idx][0] - 3) / 4
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 4
                    elif current_material in ["Mara:eye2.005", "Mara:eye2.004"]:  # eyes
                        all_vts[vt_idx][0] = (all_vts[vt_idx][0] - 4) / 8 + 0.25
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 8 + 0.875
                    elif current_material in ["Mara:skin_14:skin_13:skin_11:skin_10:pose:pose:eyelash1.004", "Mara:skin_14:skin_13:skin_11:skin_10:pose:pose:eyelash1.005"]:  # eyelash
                        all_vts[vt_idx][0] = (all_vts[vt_idx][0] - 5) / 8 + 0.25
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 8 + 0.75
                    elif current_material in [
                        "dummySG1SG1.004",
                        "dummySG1SG1.005",
                    ]:  # transparency, pump heels
                        all_vts[vt_idx][0] = all_vts[vt_idx][0] / 8 + 0.375
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 8 + 0.875
                    elif current_material == "Mara:tooth2.002":  # tooth
                        all_vts[vt_idx][0] = all_vts[vt_idx][0] / 8 + 0.375
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 8 + 0.75
                    elif current_material == "Feifei_hair_opencollada_hair2.002":  # hair
                        all_vts[vt_idx][0] = (all_vts[vt_idx][0] - 3) / 4 + 0.5
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 4 + 0.75
                    elif current_material in [
                        "W_Shoes_skinSG1SG1SG1.004",
                        "HEELSG1SG1.004",
                        "W_Shoes_skinSG1SG1SG1.005",
                        "HEELSG1SG1.005",
                    ]:  # pump
                        all_vts[vt_idx][0] = all_vts[vt_idx][0] / 4 + 0.75
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 4 + 0.75
                    else:  # Clothing material
                        all_vts[vt_idx][0] = all_vts[vt_idx][0] / 4 * 3 + 0.25
                        all_vts[vt_idx][1] = all_vts[vt_idx][1] / 4 * 3
                    # After modification, change the flag to True.
                    all_vts[vt_idx][2] = True

                unified_uv_lines.append(line)
            elif line.startswith("vt "):
                pass
            else:
                unified_uv_lines.append(line)

        for vt in all_vts:
            unified_uv_lines.append("vt " + str(vt[0]) + " " + str(vt[1]))

        with open(unified_uv_obj_file, "w") as f:
            f.write("\n".join(unified_uv_lines))
        count = count + 1    
        print(count)