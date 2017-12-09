import requests
import os
import json

# this is used to store outputs from HTTP requests in files.
# please make sure all the input directory and all the required files
# are presented in this way, or it will throw errors:
# / testclient.py
# / inputs
# - / file1.txt
# - / file2.txt 
current_path = os.path.dirname(os.path.realpath(__file__))
input_path = os.path.join(current_path, 'inputs')
output_path = os.path.join(current_path, 'outputs')
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Based on the request of the other team, I need to use this cookie to 
# access their API. Note you need to login first and then get the
# JSESSIONID from the cookies, without that you cannot generate json outputs! 
cookies = dict(JSESSIONID='PASTE THE ID HERE!')   

# This part is for the pet-controller
url_for_all_pets = 'https://petrescueorganization.herokuapp.com/pets'
r = requests.get(url_for_all_pets, cookies = cookies)
all_pets_output_path = os.path.join(output_path, 'get_all_pets.txt')
write_file = open(all_pets_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_single_pet = 'https://petrescueorganization.herokuapp.com/pets/64'
r = requests.get(url_for_single_pet, cookies = cookies)
single_pet_output_path = os.path.join(output_path, 'get_single_pet.txt')
write_file = open(single_pet_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_inserting_pet = 'https://petrescueorganization.herokuapp.com/pets'
inserted_pet_path = os.path.join(input_path, 'insert_new_pet.txt')
read_file = open(inserted_pet_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_pet, json = data, cookies = cookies)
insert_pet_output_path = os.path.join(output_path, 'insert_single_pet.txt')
write_file = open(insert_pet_output_path, 'w')
write_file.write(r.text)
write_file.close()

# simply perform the insertion with the same pet id again to see what will happen
# if we insert pets with duplicated ids.
url_for_inserting_pet = 'https://petrescueorganization.herokuapp.com/pets'
inserted_pet_path = os.path.join(input_path, 'insert_new_pet.txt')
read_file = open(inserted_pet_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_pet, json = data, cookies = cookies)
insert_pet_output_path = os.path.join(output_path, 'insert_single_pet_with_duplicated_id.txt')
write_file = open(insert_pet_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_pet_features = 'https://petrescueorganization.herokuapp.com/pets/features'
r = requests.get(url_for_pet_features, cookies = cookies)
pet_features_output_path = os.path.join(output_path, 'get_pet_features.txt')
write_file = open(pet_features_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_updating_pet = 'https://petrescueorganization.herokuapp.com/pets'
updated_pet_path = os.path.join(input_path, 'update_pet.txt')
read_file = open(updated_pet_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.put(url_for_updating_pet, json = data, cookies = cookies)
updating_pet_output_path = os.path.join(output_path, 'updating_pet.txt')
write_file = open(updating_pet_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_delete_pet = 'https://petrescueorganization.herokuapp.com/pets/213'
r = requests.delete(url_for_delete_pet, cookies = cookies)
delete_pet_output_path = os.path.join(output_path, 'delete_pet.txt')
write_file = open(delete_pet_output_path, 'w')
write_file.write(r.text)
write_file.close()

# do the deletion with the same pet id again and check what will happen.
url_for_delete_pet = 'https://petrescueorganization.herokuapp.com/pets/213'
r = requests.delete(url_for_delete_pet, cookies = cookies)
delete_pet_output_path = os.path.join(output_path, 'delete_pet_with_same_id.txt')
write_file = open(delete_pet_output_path, 'w')
write_file.write(r.text)
write_file.close()

# this part is for the pet-type-controller
url_for_all_pet_types = 'https://petrescueorganization.herokuapp.com/pet-types'
r = requests.get(url_for_all_pet_types, cookies = cookies)
all_pet_types_output_path = os.path.join(output_path, 'get_all_pet_types.txt')
write_file = open(all_pet_types_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_single_pet_type = 'https://petrescueorganization.herokuapp.com/pet-types/44'
r = requests.get(url_for_single_pet_type, cookies = cookies)
single_pet_type_output_path = os.path.join(output_path, 'get_single_pet_type.txt')
write_file = open(single_pet_type_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_inserting_pet_type = 'https://petrescueorganization.herokuapp.com/pet-types'
inserted_pet_type_path = os.path.join(input_path, 'insert_new_pet_type.txt')
read_file = open(inserted_pet_type_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_pet_type, json = data, cookies = cookies)
insert_pet_type_output_path = os.path.join(output_path, 'insert_single_pet_type.txt')
write_file = open(insert_pet_type_output_path, 'w')
write_file.write(r.text)
write_file.close()

# simply perform the insertion with the same pet type again to see what will happen
# if we insert pet type with duplicated ids.
url_for_inserting_pet_type = 'https://petrescueorganization.herokuapp.com/pet-types'
inserted_pet_type_path = os.path.join(input_path, 'insert_new_pet_type.txt')
read_file = open(inserted_pet_type_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_pet_type, json = data, cookies = cookies)
insert_pet_type_output_path = os.path.join(output_path, 'insert_single_pet_type_with_duplicated_id.txt')
write_file = open(insert_pet_type_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_updating_pet_type = 'https://petrescueorganization.herokuapp.com/pet-types'
updated_pet_type_path = os.path.join(input_path, 'update_pet_type.txt')
read_file = open(updated_pet_type_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.put(url_for_updating_pet_type, json = data, cookies = cookies)
updating_pet_type_output_path = os.path.join(output_path, 'updating_pet_type.txt')
write_file = open(updating_pet_type_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_delete_pet_type = 'https://petrescueorganization.herokuapp.com/pet-types/213'
r = requests.delete(url_for_delete_pet_type, cookies = cookies)
delete_pet_type_output_path = os.path.join(output_path, 'delete_pet_type.txt')
write_file = open(delete_pet_type_output_path, 'w')
write_file.write(r.text)
write_file.close()

# do the deletion with the same pet type again and check what will happen.
url_for_delete_pet_type = 'https://petrescueorganization.herokuapp.com/pet-types/213'
r = requests.delete(url_for_delete_pet_type, cookies = cookies)
delete_pet_type_output_path = os.path.join(output_path, 'delete_pet_type_with_same_id.txt')
write_file = open(delete_pet_type_output_path, 'w')
write_file.write(r.text)
write_file.close()

# this part is for the shelter controller
url_for_all_shelters = 'https://petrescueorganization.herokuapp.com/shelters'
r = requests.get(url_for_all_shelters, cookies = cookies)
all_shelters_output_path = os.path.join(output_path, 'get_all_shelters.txt')
write_file = open(all_shelters_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_single_shelter = 'https://petrescueorganization.herokuapp.com/shelters/43'
r = requests.get(url_for_single_shelter, cookies = cookies)
single_shelter_output_path = os.path.join(output_path, 'get_single_shelter.txt')
write_file = open(single_shelter_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_inserting_shelter = 'https://petrescueorganization.herokuapp.com/shelters'
inserted_shelter_path = os.path.join(input_path, 'insert_new_shelter.txt')
read_file = open(inserted_shelter_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_shelter, json = data, cookies = cookies)
insert_shelter_output_path = os.path.join(output_path, 'insert_single_shelter.txt')
write_file = open(insert_shelter_output_path, 'w')
write_file.write(r.text)
write_file.close()

# simply perform the insertion with the same pet type again to see what will happen
# if we insert shelter with duplicated ids.
url_for_inserting_shelter = 'https://petrescueorganization.herokuapp.com/shelters'
inserted_shelter_path = os.path.join(input_path, 'insert_new_shelter.txt')
read_file = open(inserted_shelter_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_shelter, json = data, cookies = cookies)
insert_shelter_output_path = os.path.join(output_path, 'insert_single_shelter_with_duplicated_id.txt')
write_file = open(insert_shelter_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_updating_shelter = 'https://petrescueorganization.herokuapp.com/shelters'
updated_shelter_path = os.path.join(input_path, 'update_shelter.txt')
read_file = open(updated_shelter_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.put(url_for_updating_shelter, json = data, cookies = cookies)
updating_shelter_output_path = os.path.join(output_path, 'updating_shelter.txt')
write_file = open(updating_shelter_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_delete_shelter = 'https://petrescueorganization.herokuapp.com/shelters/213'
r = requests.delete(url_for_delete_shelter, cookies = cookies)
delete_shelter_output_path = os.path.join(output_path, 'delete_shelter.txt')
write_file = open(delete_shelter_output_path, 'w')
write_file.write(r.text)
write_file.close()

# do the deletion with the same shelter again and check what will happen.
url_for_delete_shelter = 'https://petrescueorganization.herokuapp.com/shelters/213'
r = requests.delete(url_for_delete_shelter, cookies = cookies)
delete_shelter_output_path = os.path.join(output_path, 'delete_shelter_with_same_id.txt')
write_file = open(delete_shelter_output_path, 'w')
write_file.write(r.text)
write_file.close()

# this part is for the track controller
url_for_all_tracks = 'https://petrescueorganization.herokuapp.com/tracks'
r = requests.get(url_for_all_tracks, cookies = cookies)
all_tracks_output_path = os.path.join(output_path, 'get_all_tracks.txt')
write_file = open(all_tracks_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_single_track = 'https://petrescueorganization.herokuapp.com/tracks/1'
r = requests.get(url_for_single_track, cookies = cookies)
single_track_output_path = os.path.join(output_path, 'get_single_track.txt')
write_file = open(single_track_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_inserting_track = 'https://petrescueorganization.herokuapp.com/tracks'
inserted_track_path = os.path.join(input_path, 'insert_new_track.txt')
read_file = open(inserted_track_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_track, json = data, cookies = cookies)
insert_track_output_path = os.path.join(output_path, 'insert_single_track.txt')
write_file = open(insert_track_output_path, 'w')
write_file.write(r.text)
write_file.close()

# simply perform the insertion with the same pet type again to see what will happen
# if we insert pet type with duplicated ids.
url_for_inserting_track = 'https://petrescueorganization.herokuapp.com/tracks'
inserted_track_path = os.path.join(input_path, 'insert_new_track.txt')
read_file = open(inserted_track_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.post(url_for_inserting_track, json = data, cookies = cookies)
insert_track_output_path = os.path.join(output_path, 'insert_single_track_with_duplicated_id.txt')
write_file = open(insert_track_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_updating_track = 'https://petrescueorganization.herokuapp.com/tracks'
updated_track_path = os.path.join(input_path, 'update_track.txt')
read_file = open(updated_track_path, 'r')
data = json.loads(read_file.read())
read_file.close()
r = requests.put(url_for_updating_track, json = data, cookies = cookies)
updating_track_output_path = os.path.join(output_path, 'updating_track.txt')
write_file = open(updating_track_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_delete_track = 'https://petrescueorganization.herokuapp.com/tracks/213'
r = requests.delete(url_for_delete_track, cookies = cookies)
delete_track_output_path = os.path.join(output_path, 'delete_shelter.txt')
write_file = open(delete_track_output_path, 'w')
write_file.write(r.text)
write_file.close()

# do the deletion with the same pet type again and check what will happen.
url_for_delete_track = 'https://petrescueorganization.herokuapp.com/tracks/213'
r = requests.delete(url_for_delete_track, cookies = cookies)
delete_track_output_path = os.path.join(output_path, 'delete_shelter_with_same_id.txt')
write_file = open(delete_track_output_path, 'w')
write_file.write(r.text)
write_file.close()

url_for_get_track_pets = 'https://petrescueorganization.herokuapp.com/tracks/pets'
r = requests.get(url_for_get_track_pets, cookies = cookies)
get_track_pets_output_path = os.path.join(output_path, 'get_track_pets.txt')
write_file = open(get_track_pets_output_path, 'w')
write_file.write(r.text)
write_file.close()