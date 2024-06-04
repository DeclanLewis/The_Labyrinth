# The author of this file is Declan Lewis. Made 27th of February 2024.
# This software will be distributed with a GNU lesser general public license
# Pygame also uses this GNU lesser general public license

from Door import Door
from Room import Room
from Door2 import Door2

# BUTTON: Returns player to the start.
Return = Door(-50, 630, "Images/Return.png", "start", 300, 100, 300, 100)

# ROOM: Main_meu.
start_button = Door2(440, 260, "Images/Start_button.png", "start", 400, 200, 450, 225)
main_menu = Room("Images/Main_menu_background.jpg", [start_button], "Sounds/no_sound.mp3", "Sounds/Introduction.mp3")

# ROOM: Starting room.
start_room_door_1 = Door2(730, 280,"Images/Doors/Door1.png", "front", 140, 120, 190, 170)
start_room = Room("Images/Backgrounds/StartRoom.jpg", [start_room_door_1, Return],"Sounds/StartRoom_music.wav" ,"Sounds/StartRoom_speech.mp3")

# ROOM: Front room.
front_room_door_1 = Door2(1150, 100, "Images/Doors/Side_Door.png", "lab", 130, 550, 180, 600)
front_room_door_2 = Door(280, 250, "Images/Doors/Hallway_Door.png", "hallway", 200, 120, 250, 170)
front_room = Room("Images/Backgrounds/Background_2.jpg", [front_room_door_2, front_room_door_1, Return], "Sounds/Hallway_music.wav", "Sounds/Front_room_speech.mp3")

# ROOM: Lab room.
lab_room = Room("Images/Backgrounds/Small_lab.jpg", [Return], "Sounds/no_sound.mp3", "Sounds/Lab_room_speech.mp3")

# ROOM: Hallway room.
hallway_room_door_1 = Door2(480, 260, "Images/Doors/Hallway_room_door.png", "forest", 150, 250, 200, 300)
hallway_room = Room("Images/Backgrounds/1_door_hallway.jpg", [hallway_room_door_1, Return], "Sounds/Hallway_music.wav", "Sounds/Hallway_speech.mp3")

# ROOM: Forest room.
forest_room_path_right = Door(850, 480, "Images/Arrows/Up_arrow.png", "park", 100, 200, 150, 250)
forest_room_path_left = Door(200, 450, "Images/Arrows/Up_arrow.png", "front", 100, 200, 150, 250)
forest_room = Room("Images/Backgrounds/Forest_1.jpg", [forest_room_path_right, Return, forest_room_path_left], "Sounds/Forest_sound.mp3", "Sounds/no_sound.mp3")

# ROOM: Park
Park_room_path1 = Door(770, 160, "Images/Arrows/Right_arrow.png", "bunker", 200, 100, 250, 150)
Park_room_path2 = Door(770, 260, "Images/Arrows/Left_arrow.png", "spider lair", 200, 100, 250, 150)
Park_room = Room("Images/Backgrounds/Forest_park.jpg", [Return, Park_room_path1, Park_room_path2], "Sounds/Park_music.wav", "Sounds/Park_speech.mp3")

# ROOM: Spider liar room:
Spider_lair_path = Door(1000, 450, "Images/Arrows/Up_arrow.png", "spider", 100, 200, 150, 250)
Spider_lair = Room("Images/Backgrounds/Spider_lair_entrance.jpg", [Return, Spider_lair_path], "Sounds/Spider_lair_entrance_music.wav", "Sounds/Spider_lair_entrance_speech.mp3")

# DEATH: Spider encounter
Spider_Fight = Door(440, 500, "Images/Doors/Fight_monster_text.png", "main", 400, 200, 400, 200)
Spider = Room("Images/Backgrounds/Spider_death.jpg", [Spider_Fight, Return], "Sounds/Boss.wav", "Sounds/Spider_speech.mp3")

# ROOM: Bunker entrance:
Bunker_entrance_door = Door2(300, 200, "Images/Doors/Bunker_Door.png", "bunker hallway", 400, 300, 450, 333)
Bunker_entrance = Room("Images/Backgrounds/Bunker_entrance.jpg", [Return, Bunker_entrance_door], "Sounds/Bunker_entrence_music.mp3", "Sounds/Bunker_entrence_speech.mp3")

# ROOM: Bunker hallway:
Bunker_hallway_door = Door2(450, 260, "Images/Doors/Bunker_hallway_door.png", "bunker common room", 450, 180, 500, 200)
Bunker_hallway = Room("Images/Backgrounds/Bunker_Hallway.jpg", [Return, Bunker_hallway_door],"Sounds/no_sound.mp3", "Sounds/no_sound.mp3")

# ROOM: Bunker_common room:
Bunker_common_room_door = Door2(560, 185, "Images/Doors/Bunker_commonroom_door.png", "bunker dark room", 450, 200, 500, 225)
Bunker_common_room_hatch = Door2(200, 270, "Images/Doors/Buner_commonroom_hatch.png", "", 100, 100, 125,125)
Bunker_common_room = Room("Images/Backgrounds/Bunker_commonroom.jpg", [Return, Bunker_common_room_hatch, Bunker_common_room_door], "Sounds/no_sound.mp3", "Sounds/no_sound.mp3")

# ROOM: Bunker_dark_room:
Bunker_dark_room_light_switch = Door2(1080, 250, "Images/Doors/Light_switch_in_dark.png", "", 180, 200, 200, 225)
Bunker_dark_room = Room("Images/Backgrounds/Dark_room.png", [Return, Bunker_dark_room_light_switch], "Sounds/no_sound.mp3", "Sounds/no_sound.mp3")

# The dictionary containing and identifying all the rooms
rooms = {
    "main": main_menu,
    "start": start_room,
    "front": front_room,
    "lab": lab_room,
    "hallway": hallway_room,
    "forest": forest_room,
    "park": Park_room,
    "bunker": Bunker_entrance,
    "spider lair": Spider_lair,
    "spider": Spider,
    "bunker hallway": Bunker_hallway,
    "bunker common room": Bunker_common_room,
    "bunker dark room": Bunker_dark_room,

}