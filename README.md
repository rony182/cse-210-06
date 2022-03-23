# Zombie Invasion Game Specification
Zombie Invasion is a game in which the player seeks to shoot as many zombies as possible. 
The game continues as long as the player is alive.

## Rules:
1. The player has 3 lives per game.
2. If the player lets more than 10 zombies past him/her he/she will lose a life.
3. If the player gets touched by a zombie he/she will lose a life.
4. Some zombies will take more than one shot to die.
5. The game continues as long as the player is alive.

## Game Mockup
<<<<<<< HEAD
---
![Game's mockup](.\zombie_invasion\readme_elements\mockup.png)

## Wish List

You can check the wish list [here](.\zombie_invasion\readme_elements\WISHME.md).

## Feature List

You can check the wish list [here](.\zombie_invasion\readme_elements\FEATUREME.md).


## Getting Started
---
Make sure you have Python 3.9.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
python3 -m pip install pyray
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.
```
python3 zombie_invasion 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.


## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- zombie_invasion     (source code for game)
  +-- assets            (specific game assets)
    +-- data            (game data/level)
    +-- fonts           (game fonts)
    +-- images          (game images)
    +-- sounds          (game sounds)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
      +-- actor.py
      +-- animation.py
      +-- player.py
      +-- zombie.py
      +-- body.py
      +-- cast.py
      +-- color.py
      +-- image.py
      +-- label.py
      +-- point.py
      +-- gun.py
      +-- sound.py
      +-- stats.py
      +-- text.py
    +-- directing       (director and scene manager classes)
      +-- director.py
      +-- scene_manager.py
    +-- scripting       (various action classes)
      +-- action_callback.py
      +-- action.py
      +-- change_scene_action.py
      +-- check_scene_action.py
      +-- check_over_action.py
      +-- collide_borders_action.py
      +-- collide_player_action.py
      +-- shoot_zombie_action.py
      +-- control_player_action.py
      +-- draw_zombies_action.py
      +-- draw_dialog_action.py
      +-- draw_hud_action.py
      +-- draw_shot_action.py
      +-- draw_player_action.py
      +-- end_drawing_action.py
      +-- initialize_devices_action.py
      +-- load_assets_action.py
      +-- move_zombies_action.py
      +-- move_player_action.py
      +-- play_sound_action.py
      +-- release_devices_action.py
      +-- script.py
      +-- start_drawing_action.py
      +-- timed_change_scene_action.py
      +-- unload_assets_action.py
    +-- services        (various service classes)
      +--raylib
        +--raylib_audio_service.py
        +--raylib_keyboard_service.py
        +--raylib_mouse_service.py
        +--raylib_physics_service.py
        +--raylib_video_service.py
      +--audio_service.py
      +--keyboard_service.py
      +--mouse_service.py
      +--physics_service.py
      +--video_service.py
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
  +--readme_elements    (readme lists and mockup image)
    +-- FEATUREME.md        (features info)
    +-- WISHME.md           (desirable features info)
+-- README.md           (general info)
```

## Required Technologies
* Python 3.9.0

## Authors (CSE210 winter 2022: Team 08)
* Kwazeme Ogubie (ogu21006@byui.edu)
* A. Belén Chaparro (cha21065@byui.edu)
* Fabrizio Carlassara (car21101@byui.edu)
* Rony Nickson Calderon Sara (cal21043@byui.edu)