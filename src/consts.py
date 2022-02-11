import os
import platform

__dir__, abspath, join = os.path.dirname(__file__), os.path.abspath, os.path.join
root_path = abspath('.')
res_root_path = __dir__
config_path = join(root_path, 'settings.toml')
danser_config_path = join('settings', 'default.json')
danser_api_path = join('settings', 'api.txt')
danser_exec_file_name = 'danser.exe' if platform.system() == 'Windows' else 'danser'
langs_path = join(res_root_path, 'langs')


class LogPath:
	app = "app.log"

default_settings_toml = '''[General]
OsuRootDir = ''
OsuSongsDir = ''
OsuSkinsDir = ''
DanserRootDir = ''
DanserMode = 'danser' # danser/knockout/play/replay
IsRecord = false
SongsDBMode = 'osu!' # osu!/danser
OsuApi = '' # get it from https://osu.ppy.sh/api/
Language = 0 # 0: English, 1: Chinese (Simplified)

[Graphics]
Fullscreen = false
Width = 1280
Height = 720
VSync = false
MSAA = 0
FPSCap = 0
ShowFPS = true

[Recording]
FrameWidth = 1920
FrameHeight = 1080
FPS = 120
Encoder = 'cpu'
MotionBlur = false
OutputPath = 'video'
OutputName = '{Player} - {Artist}[{Creator}] - {MapTitle}[{Difficulty}].mp4'

[Recording.EncoderConfig]
VideoCodec = "libx264"
EncoderOptions = "-crf 21 -g 450"
Preset = "faster"
AudioCodec = "aac"
AudioOptions = "-b:a 192k"

[Audio]
GlobalVolume = 100
MusicVolume = 100
HitSoundVolume = 100

[Input]
LeftKey = "Z"
RightKey = "X"
RestartKey = "`"
SmokeKey = "C"
MouseButtonsDisabled = true

[Gameplay]
PlayUsername = 'danser-gui'

[Gameplay.HitErrorMeter]
Show = true
ShowUnstableRate = true

[Gameplay.Score]
Show = true

[Gameplay.HpBar]
Show = true

[Gameplay.ComboCounter]
Show = true

[Gameplay.PPCounter]
Show = true
UseLazerPP = false

[Gameplay.StrainGraph]
Show = true

[Gameplay.KeyOverlay]
Show = true

[Gameplay.ScoreBoard]
Show = true
HideOthers = true
ShowAvatars = false

[Gameplay.HitCounter]
Show = true

[Gameplay.AimErrorMeter]
Show = true

[Gameplay.Boundaries]
Show = true

[Gameplay.Mods]
Show = true
HideInReplays = false
FoldInReplays = false

[Gameplay.ResultsScreen]
Show = true
Time = 5
UseLocalTimeZone = true

[Skin]
CurrentSkin = ''
UseSkinColors = true
UseBeatmapColors = true
UseSkinCursor = true
UseSkinHitsounds = false

[Cursor]
ScaleToCS = false
CursorRainbow = false
CursorTrailGlow = false
CursorSize = 1
CursorRipples = true
ForceLongTrail = false
LongTrailDensity = 0
LongTrailLength = 0

[Objects]
DrawFollowPoints = true
DrawComboNumbers = true
ScaleToTheBeat = false
SliderMerge = false
Rainbow = false
FlashToTheBeat = false
UseHitCircleColor = true
SliderSnakingIn = true
SliderSnakingOut = true

[Playfield]
SeizureWarning = false
LoadStoryboard = true
LoadVideo = true
IntroBGDim = 0
InGameBGDim = 80
BreakBGDim = 50
BGParallax = false
ShowDanserLogo = true'''
