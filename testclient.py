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

# this is the part for testing the GET method.
def test_get_method(url_for_test, output_file):
    r = requests.get(url_for_test, cookies = cookies)
    output_file_path = os.path.join(output_path, output_file)
    write_file = open(output_file_path, 'w')
    write_file.write(r.text)
    write_file.close()

test_get_method('https://petrescueorganization.herokuapp.com/pets', 'get_all_pets.txt')
test_get_method('https://petrescueorganization.herokuapp.com/pets/64', 'get_single_pet.txt')
test_get_method('https://petrescueorganization.herokuapp.com/pets/features', 'get_pet_features.txt')
test_get_method('https://petrescueorganization.herokuapp.com/pet-types', 'get_all_pet_types.txt')
test_get_method('https://petrescueorganization.herokuapp.com/pet-types/44', 'get_single_pet_type.txt')
test_get_method('https://petrescueorganization.herokuapp.com/shelters', 'get_all_shelters.txt')
test_get_method('https://petrescueorganization.herokuapp.com/shelters/43', 'get_single_shelter.txt')
test_get_method('https://petrescueorganization.herokuapp.com/tracks', 'get_all_tracks.txt')
test_get_method('https://petrescueorganization.herokuapp.com/tracks/1', 'get_single_track.txt')
test_get_method('https://petrescueorganization.herokuapp.com/tracks/pets', 'get_track_pets.txt')

# this is the part for testing the POST method.
def test_post_method(url_for_test, input_file, output_file):
    input_file_path = os.path.join(input_path, input_file)
    read_file = open(input_file_path, 'r')
    data = json.loads(read_file.read())
    read_file.close()
    r = requests.post(url_for_test, json = data, cookies = cookies)
    output_file_path = os.path.join(output_path, output_file)
    write_file = open(output_file_path, 'w')
    write_file.write(r.text)
    write_file.close()

# note since the post is for insertion, after doing the insertion. I will do the same
# insertion again to see what will happen if I insert duplicated ids.
# also for deletion's sake, I set all the ID as 213 to let delete operate on that.
test_post_method('https://petrescueorganization.herokuapp.com/pets', 'insert_new_pet.txt', 'insert_single_pet.txt')
test_post_method('https://petrescueorganization.herokuapp.com/pets', 'insert_new_pet.txt', 'insert_single_pet_with_duplicate_id.txt')
test_post_method('https://petrescueorganization.herokuapp.com/pet-types', 'insert_new_pet_type.txt', 'insert_single_pet_type.txt')
test_post_method('https://petrescueorganization.herokuapp.com/pet-types', 'insert_new_pet_type.txt', 'insert_single_pet_type_with_duplicate_id.txt')
test_post_method('https://petrescueorganization.herokuapp.com/shelters', 'insert_new_shelter.txt', 'insert_single_shelter.txt')   
test_post_method('https://petrescueorganization.herokuapp.com/shelters', 'insert_new_shelter.txt', 'insert_single_shelter_with_duplicate_id.txt')
test_post_method('https://petrescueorganization.herokuapp.com/tracks', 'insert_new_track.txt', 'insert_single_track.txt')
test_post_method('https://petrescueorganization.herokuapp.com/tracks', 'insert_new_track.txt', 'insert_single_track_with_duplicate_id.txt')

# this is the part for testing the PUT method.
def test_put_method(url_for_test, input_file, output_file):
    input_file_path = os.path.join(input_path, input_file)
    read_file = open(input_file_path, 'r')
    data = json.loads(read_file.read())
    read_file.close()
    r = requests.put(url_for_test, json = data, cookies = cookies)
    output_file_path = os.path.join(output_path, output_file)
    write_file = open(output_file_path, 'w')
    write_file.write(r.text)
    write_file.close()

test_put_method('https://petrescueorganization.herokuapp.com/pets', 'update_pet.txt', 'updating_pet.txt')
test_put_method('https://petrescueorganization.herokuapp.com/pet-types', 'update_pet_type.txt', 'updating_pet_type.txt')
test_put_method('https://petrescueorganization.herokuapp.com/shelters', 'update_shelter.txt', 'updating_shelter.txt')
test_put_method('https://petrescueorganization.herokuapp.com/tracks', 'update_track.txt', 'updating_track.txt')

# this is the part for testing the DELETE method.
def test_delete_method(url_for_test, output_file):
    r = requests.delete(url_for_test, cookies = cookies)
    output_file_path = os.path.join(output_path, output_file)
    write_file = open(output_file_path, 'w')
    write_file.write(r.text)
    write_file.close()

# note I will do the same deletion to see what will happen if I delete something
# that is not appeared in the website database.
test_delete_method('https://petrescueorganization.herokuapp.com/pets/213', 'delete_pet.txt')
test_delete_method('https://petrescueorganization.herokuapp.com/pets/213', 'delete_pet_with_same_id.txt')
test_delete_method('https://petrescueorganization.herokuapp.com/pet-types/213', 'delete_pet_type.txt')
test_delete_method('https://petrescueorganization.herokuapp.com/pet-types/213', 'delete_pet_type_with_same_id.txt')
test_delete_method('https://petrescueorganization.herokuapp.com/shelters/213', 'delete_shelter.txt')
test_delete_method('https://petrescueorganization.herokuapp.com/shelters/213', 'delete_shelter_with_same_id.txt')
test_delete_method('https://petrescueorganization.herokuapp.com/tracks/213', 'delete_track.txt')
test_delete_method('https://petrescueorganization.herokuapp.com/tracks/213', 'delete_track_with_same_id.txt')
