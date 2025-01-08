from src.update_remote_student import update_remote_student

def test_update_is_list_of_dict():
    result = update_remote_student([
  { "name": 'Hypatia', "age": 31, "location": 'leeds' },
  { "name": 'Ramanujan', "age": 22 },
  { "name": 'Tao', "age": 47, "location": 'manchester' }
])
    assert isinstance(result,list)

def test_update_remote_student_return_remote():
    result = update_remote_student([
  { "name": 'Hypatia', "age": 31, "location": 'leeds' },
  { "name": 'Ramanujan', "age": 22 },
  { "name": 'Tao', "age": 47, "location": 'manchester' }
])
    assert result == [
  { "name": 'Hypatia', "age": 31, "location": 'leeds' },
  { "name": 'Ramanujan', "age": 22, "location":"remote" },
  { "name": 'Tao', "age": 47, "location": 'manchester' }
]
    