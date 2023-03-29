import pywinauto
from pywinauto.application import Application
import pyautogui
import time
import numpy as np

# x = pywinauto.findwindows.find_windows(title_re='iTunes')
# print(x)
# print(len(x))
# print(x[len(x)-1])
#
# App = Application().connect(title='iTunes', found_index=0, timeout=10)
# app_dialog = App.window(title_re='iTunes', found_index=0)
#
# if app_dialog.exists():
#     app_dialog.set_focus()
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')
#
# print("done!")
#
# TopHitsPlaylist = {
#     "name": "Todays_Top_Hits",
#     "link": "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M",
#     }
#
# TestPlaylist = {
#     "name": "Test",
#     "link": "https://open.spotify.com/playlist/3iuRup8fvHF8EO6WS7Wdyi?si=c703487dc3e4421f",
#     }
#
# AllPlaylists = [TopHitsPlaylist, TestPlaylist]
#
# print(AllPlaylists)
#
# print(sorted(AllPlaylists, key=lambda i: i['name']))

FirstPlaylist = (120, 550)
PlaylistIncrement = 72

playlistcount = 0

AllWindows = pywinauto.findwindows.find_windows(title_re='iTunes')
Handle = AllWindows[len(AllWindows)-1]
App = Application().connect(title='iTunes', found_index=0, timeout=10)
app_dialog = App.window(title_re='iTunes', found_index=0, handle=Handle)

if app_dialog.exists():
    app_dialog.set_focus()
for i in range(6):
    pyautogui.moveTo(FirstPlaylist + (0, PlaylistIncrement * i))
    pyautogui.click()
    time.sleep(5)