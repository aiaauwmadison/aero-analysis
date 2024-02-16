import zipfile
import os
import xmltodict
# import math
# from lxml.etree import fromstring, tostring
# from xml.etree import ElementTree as ET
# import uuid
# import tkinter as tk
# from tkinter import ttk


filename = 'variables.txt'

# TODO

def run():
    global filename
    with open(filename, 'r') as file:
        for line in file:
            key, value = line.strip().split(':')
            value = value.replace(',', '').strip()
            # print(f"key: {key}, value: {value}")  # test print
            if key == 'ork_filename':
                ork_filename = value
            elif key == 'author':
                author = value
            elif key == 'G':
                G = float(value)
            elif key == 'h_g':
                h_g = float(value)
            elif key == 'h_relVmax':
                h_relVmax = float(value)
            elif key == 'm':
                m = float(value)
            elif key == 'v_i':
                v_i = float(value)
            elif key == 'v_f':
                v_f = float(value)
            elif key == 't_infl':
                t_infl = float(value)
            elif key == 'V_max':
                V_max = float(value)
            elif key == 'Cd_m':
                Cd_m = float(value)
            elif key == 'D_m':
                D_m = float(value)
            elif key == 'rho_m':
                rho_m = float(value)
            elif key == 'Cd_d':
                Cd_d = float(value)
            elif key == 'rho_d':
                rho_d = float(value)
            elif key == 'D_d':
                D_d = float(value)
            elif key == 'D_a':
                D_a = float(value)
            elif key == 'L_Dbay':
                L_Dbay = float(value)
            elif key == 'L_Mbay':
                L_Mbay = float(value)
            elif key == 'P_e':
                P_e = float(value)

        # --- import vars from ork ---
        # ork_string = ork_toString(ork_filename)
        ork_dict = get_ork_dict(ork_filename)

        # --- fin parameters ---
        finset_dict = get_finset_dict(ork_dict)
        b = float(finset_dict['height'])/0.0254
        c_r = float(finset_dict['rootchord'])/0.0254
        c_t = float(finset_dict['tipchord'])/0.0254
        FT = float(finset_dict['thickness'])/0.0254

        ### WIP
        # --- main chute parameters ---
        # main_chute_dict = get_main_chute_dict(ork_dict)
        # print(main_chute_dict)
        # print(main_chute_dict['diameter'])
        # D_a = float(main_chute_dict['diameter'])/0.0254
        # Cd_m = float(main_chute_dict['dragcoefficient'])
        # D_m = math.sqrt(4*float(main_chute_dict['area'])/math.pi)/0.0254
        # rho_m = float(main_chute_dict['@density'])    # not in .ork
        # rho_m = 1.225
        # tk_tree_view(main_chute_dict)

        ### WIP
        # --- drogue chute parameters ---
        # drogue_chute_dict = get_drogue_chute_dict(ork_dict)

        ### WIP: test prints
        # print(f"b: {b}")
        # print(f"c_r: {c_r}")
        # print(f"c_t: {c_t}")
        # print(f"t: {t}")

        ### WIP: testing more variable imports
        # h_launch = ork_dict['openrocket']['simulations']['simulation'][0]['conditions']['launchaltitude']
        # print(f"h_launch: {h_launch}")
        # .ork has peak velocity listed but you must search the file t
        # max_v = ork_dict['openrocket']['simulations']['simulation'][0]['flightdata']['@maxvelocity']
        # datapoint = find_datapoint_in_dict(ork_dict, 251.677)
        # print(datapoint)
        # data_str = find_datapoint_with_number(ork_string, 251.677)
        # print(data_str)
        # flightdata_str = ork_dict['openrocket']['simulations']['simulation'][0]['flightdata']
        # root = ET.fromstring(flightdata_str)
        # max_v = root.attrib['maxvelocity']

    return author, c_r, c_t, FT, b, G, h_g, h_relVmax, m, v_i, v_f, t_infl, V_max, Cd_m, D_m, rho_m, Cd_d, rho_d, D_d, D_a, L_Dbay, L_Mbay, P_e


def extract_ork(ork_file_path, extract_path):
    with zipfile.ZipFile(ork_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    return


def get_ork_dict(ork_filename):
    while True:
        file_path = os.path.join(os.getcwd(), ork_filename)
        if not os.path.exists(file_path):
            print(f'Error: {ork_filename} not found in {os.getcwd()}')
        elif not ork_filename.endswith('.ork'):
            print(f'Error: {ork_filename} is not a valid .ork file')
        elif not os.access(file_path, os.R_OK):
            print(f'Error: {ork_filename} is not readable')
        else:
            break
    extract_ork(file_path, os.getcwd())
    path = os.path.join(os.getcwd(), 'rocket.ork')
    ork_string = ork_toString(path)
    ork_dict = ork_to_dict(ork_string)
    return ork_dict


def ork_to_dict(ork_string):
    ork_dict = xmltodict.parse(ork_string)
    return ork_dict


def ork_toString(ork_file_path):
    with open(ork_file_path, "r") as file:
        ork_string = file.read()
    return ork_string



def get_finset_dict(ork_dict):
    ### testing
    # tk_tree_view(ork_dict)
    # subcomponents_dict = ork_dict['openrocket']['rocket']['subcomponents']['stage']['subcomponents']
    # tk_tree_view(subcomponents_dict)
    # for key, value in subcomponents_dict.items():
    #     print(key)

    finset_dict = ork_dict['openrocket']['rocket']['subcomponents']['stage'][
        'subcomponents']['bodytube'][4]['subcomponents']['trapezoidfinset']
    # semispan = finset_dict['height']
    # rootchord = finset_dict['rootchord']
    # tipchord = finset_dict['tipchord']
    # thickness = finset_dict['thickness']
    
    return finset_dict


def get_main_chute_dict(ork_dict):
    main_chute_dict = ork_dict['openrocket']['rocket']['subcomponents']['stage'][
        'subcomponents']['bodytube'][1]['subcomponents']['parachute']
    return main_chute_dict

def get_drogue_chute_dict(ork_dict):
    drogue_chute_dict = ork_dict['openrocket']['rocket']['subcomponents']['stage'][
        'subcomponents']['bodytube'][4]['subcomponents']['parachute']
    return drogue_chute_dict

### WIP: find a main chute in any .ork
# def find_main_chute_in_dict(data):
#     # print(data)
#     # If data is a dictionary
#     if isinstance(data, dict):
#         # If this dictionary is a 'parachute' with the name 'Main Chute'
#         if data.get('name') == 'Main Chute':
#             print(data)
#             return data
#         # Otherwise, search recursively in values
#         for key, value in data.items():
#             result = find_main_chute_in_dict(value)
#             if result is not None:
#                 return result
#     # If data is a list, iterate over its items
#     elif isinstance(data, list):
#         for item in data:
#             result = find_main_chute_in_dict(item)
#             if result is not None:
#                 return result
#     # Return None if not found
#     return None

# def get_main_chute_dict(ork_dict):
#     return find_main_chute_in_dict(ork_dict)

### WIP: find a drogue chute in any .ork
# def find_drogue_chute_in_dict(data):
#     # If data is a dictionary
#     if isinstance(data, dict):
#         # If this dictionary is a 'parachute' with the name 'Drogue Chute'
#         if data.get('name') == 'Drogue Chute':
#             return data
#         # Otherwise, search recursively in values
#         for key, value in data.items():
#             result = find_drogue_chute_in_dict(value)
#             if result is not None:
#                 return result
#     # If data is a list, iterate over its items
#     elif isinstance(data, list):
#         for item in data:
#             result = find_drogue_chute_in_dict(item)
#             if result is not None:
#                 return result
#     # Return None if not found
#     return None

# def get_drogue_chute_dict(ork_dict):
#     return find_drogue_chute_in_dict(ork_dict)


### WIP: for tree visualization, not working
# def j_tree(tree, parent, dic):
#     for key in sorted(dic.keys()):
#         uid = uuid.uuid4()
#         if isinstance(dic[key], dict):
#             tree.insert(parent, 'end', uid, text=key)
#             j_tree(tree, uid, dic[key])
#         elif isinstance(dic[key], tuple):
#             tree.insert(parent, 'end', uid, text=str(key) + '()')
#             j_tree(tree, uid,
#                    dict([(i, x) for i, x in enumerate(dic[key])]))
#         elif isinstance(dic[key], list):
#             tree.insert(parent, 'end', uid, text=str(key) + '[]')
#             j_tree(tree, uid,
#                    dict([(i, x) for i, x in enumerate(dic[key])]))
#         else:
#             value = dic[key]
#             if isinstance(value, str):
#                 value = value.replace(' ', '_')
#             tree.insert(parent, 'end', uid, text=key, value=value)

### WIP: for tree visualization, not working
# def tk_tree_view(data):
#     # Setup the root UI
#     root = tk.Tk()
#     root.title("tk_tree_view")
#     root.columnconfigure(0, weight=1)
#     root.rowconfigure(0, weight=1)

#     # Setup the Frames
#     tree_frame = ttk.Frame(root, padding="3")
#     tree_frame.grid(row=0, column=0, sticky=tk.NSEW)

#     # Setup the Tree
#     tree = ttk.Treeview(tree_frame, columns=('Values'))
#     tree.column('Values', width=100, anchor='center')
#     tree.heading('Values', text='Values')
#     j_tree(tree, '', data)
#     tree.pack(fill=tk.BOTH, expand=1)

#     # Limit windows minimum dimensions
#     root.update_idletasks()
#     root.minsize(root.winfo_reqwidth(), root.winfo_reqheight())
#     root.mainloop()

### WIP: for testing
# def find_datapoint_with_number(xml_string, target_number):
#     root = ET.fromstring(xml_string)

#     for datapoint in root.iter('datapoint'):
#         datapoint_text = datapoint.text
#         datapoint_numbers = [float(number)
#                              for number in datapoint_text.split(',')]

#         if target_number in datapoint_numbers:
#             return datapoint

#     return None

### WIP: for testing
# def find_datapoint_in_dict(ork_dict, number):
#     # Get the XML string from the dictionary
#     xml_string = ork_dict['openrocket']['simulations']['simulation'][0]['flightdata']['databranch']

#     # Iterate over all 'datapoint' elements in the tree
#     for datapoint in root.iter('datapoint'):
#         # Split the text of the 'datapoint' element into a list of strings
#         values = datapoint.text.split(',')
#         # If the number is in the list of strings, return the 'datapoint' element as a string
#         if str(number) in values:
#             return ET.tostring(datapoint, encoding='unicode')

#     return None


# def run_parser():
    # rocket_ork_path = get_ork()
    # ork_string = ork_toString(rocket_ork_path)
    # fin_dict = get_finset_dict(ork_string)

# Extracting parachute details from the bodytube subcomponents
# def extract_parachutes(data):
#     parachutes = []
#     if isinstance(data, dict):
#         for key, value in data.items():
#             if key == 'parachute':
#                 parachutes.append(value)
#             elif isinstance(value, (dict, list)):
#                 parachutes.extend(extract_parachutes(value))
#     elif isinstance(data, list):
#         for item in data:
#             parachutes.extend(extract_parachutes(item))
#     return parachutes

### WIP: for testing
# with open(filename, 'r') as file:
#     for line in file:
#         key, value = line.strip().split(':')
#         value = value.replace(',', '').strip()
#         # print(f"key: {key}, value: {value}")  # test print
#         if key == 'ork_filename':
#             ork_filename = value
# ork_dict = get_ork_dict(ork_filename)
# # Extract parachutes from the 'bodytube' subcomponents
# parachutes = extract_parachutes(ork_dict['openrocket']['rocket']['subcomponents']['stage']['subcomponents']['bodytube'][1])
# parachutes  # Display the extracted parachute details to verify

# run()