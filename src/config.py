import logging
from autologging import logged, traced
import toml, json, os
import consts
from munch import Munch, DefaultMunch
from os.path import isfile, join

def decode_config_file(toml_path):
    with open(toml_path, mode='rb') as f:
        content = f.read()
    if content.startswith(b'\xef\xbb\xbf'):
        content = content[3:]
    return content.decode('utf8')


@logged(logging.getLogger(__name__))
@traced
class DanserGUIConfig(object):
    def __init__(self, config_path = ''):
        self.config_path = config_path if isfile(config_path) else consts.config_path
        self.read()
        self.danser_config = DanserConfig(join(self.config.General.DanserRootDir, consts.danser_config_path))

    def no_api_config(self):
        osu_api = self.config.General.OsuApi
        self.config.General.OsuApi = ''
        config_dict = self.config.toDict()
        self.config.General.OsuApi = osu_api
        return config_dict

    def read(self, config_path = ''):
        if not isfile(config_path):
            config_path = self.config_path
        self.config = Munch.fromDict(toml.loads(decode_config_file(config_path)))
        logging.info(f"[GUI][CONFIG] GUI Config is read from: {config_path}")

    def write(self, config_path = ''):
        if not isfile(config_path):
            config_path = self.config_path
        # logging.info(f"[GUI][CONFIG] GUI Config is: {self.no_api_config()}")
        with open(config_path, 'w', encoding='utf-8') as f:
            toml.dump(self.config.toDict(), f)
        logging.info(f"[GUI][CONFIG] GUI Config is written to: {config_path}")

    
    def sync(self):
        danser_config, config = self.danser_config.config, self.config

        # General
        danser_config.General.OsuSongsDir = config.General.OsuSongsDir
        danser_config.General.OsuSkinsDir = config.General.OsuSkinsDir
        # danser_config.General.OsuSongsDir = join(config.General.OsuRootDir, 'Songs')
        # danser_config.General.OsuSkinsDir = join(config.General.OsuRootDir, 'Skins')

        # Graphics
        danser_config.Graphics.Fullscreen = config.Graphics.Fullscreen
        if config.Graphics.Fullscreen:
            danser_config.Graphics.Width = config.Graphics.Width
            danser_config.Graphics.Height = config.Graphics.Height
        else:
            danser_config.Graphics.WindowWidth = config.Graphics.Width
            danser_config.Graphics.WindowHeight = config.Graphics.Height
        danser_config.Graphics.VSync = config.Graphics.VSync
        danser_config.Graphics.MSAA = config.Graphics.MSAA
        danser_config.Graphics.FPSCap = config.Graphics.FPSCap
        danser_config.Graphics.ShowFPS = config.Graphics.ShowFPS


        # Recording
        encoder = config.Recording.Encoder
        frame_scale = config.Recording.FrameHeight / config.Recording.FrameWidth
        danser_config.Recording.FrameWidth = config.Recording.FrameWidth if config.Recording.FrameWidth <= 1920 else 1920
        danser_config.Recording.FrameHeight = config.Recording.FrameHeight if config.Recording.FrameWidth <= 1920 else int(1920 * frame_scale)
        danser_config.Recording.FPS = config.Recording.FPS
        danser_config.Recording.OutputDir = config.Recording.OutputPath
        danser_config.Recording.Container = os.path.splitext(config.Recording.OutputName)[1][1:] # Get Filename Extension

        danser_config.Recording.AudioCodec = "aac"
        danser_config.Recording.AudioOptions = "-b:a 192k"

        if encoder == 'cpu':
            danser_config.Recording.Encoder = "libx264"
            danser_config.Recording.EncoderOptions = "-crf 21 -g 450"
            danser_config.Recording.Preset = "faster"
        elif encoder == 'nvidia':
            danser_config.Recording.Encoder = "h264_nvenc"
            danser_config.Recording.EncoderOptions = "-rc constqp -qp 26 -g 450"
            danser_config.Recording.Preset = "slow"
        elif encoder == 'amd':
            danser_config.Recording.Encoder = "h264_amf"
            danser_config.Recording.EncoderOptions = "-rc cqp -qp_p 17 -qp_i 17 -quality quality"
            danser_config.Recording.Preset = "slow" # H264_amf doesn't support -preset, instead using -quality (for some reason), keeping preset so it doesn't break anything
        elif encoder == 'intel':
            danser_config.Recording.Encoder = "h264_qsv"
            # -global_quality was 31 before and looked okay-ish on 1080p but very bad on 720p
            if config.Recording.FrameWidth >= 1920:
                danser_config.Recording.EncoderOptions = "-global_quality 28 -g 450"
            else:
                danser_config.Recording.EncoderOptions = "-global_quality 25 -g 450"
            danser_config.Recording.Preset = "veryslow"
        else:
            danser_config.Recording.Encoder = config.Recording.EncoderConfig.VideoCodec or 'libx264'
            danser_config.Recording.EncoderOptions = config.Recording.EncoderConfig.EncoderOptions or '-crf 21 -g 450'
            danser_config.Recording.Preset = config.Recording.EncoderConfig.Preset or 'faster'
            danser_config.Recording.AudioCodec = config.Recording.EncoderConfig.AudioCodec or 'aac'
            danser_config.Recording.AudioOptions = config.Recording.EncoderConfig.AudioOptions or '-b:a 192k'
        
        if config.Recording.FrameWidth > 1920:
            danser_config.Recording.Filters = f"scale={config.Recording.FrameWidth}:{config.Recording.FrameHeight}:flags=lanczos"
        else:
            danser_config.Recording.Filters = ""

        if config.Recording.MotionBlur:
            danser_config.Recording.MotionBlur.Enabled = True
            danser_config.Recording.MotionBlur.OversampleMultiplier = 16
            danser_config.Recording.MotionBlur.BlendFrames = 22
        else:
            danser_config.Recording.MotionBlur.Enabled = False

        # Audio
        danser_config.Audio.GeneralVolume = round(config.Audio.GlobalVolume / 100, 2)
        danser_config.Audio.MusicVolume = round(config.Audio.MusicVolume / 100, 2)
        danser_config.Audio.SampleVolume = round(config.Audio.HitSoundVolume / 100, 2)
        
        # Gameplay
        danser_config.Gameplay.PlayUsername = config.Gameplay.PlayUsername
        danser_config.Gameplay.HitErrorMeter.Show = config.Gameplay.HitErrorMeter.Show
        danser_config.Gameplay.HitErrorMeter.ShowUnstableRate = config.Gameplay.HitErrorMeter.ShowUnstableRate
        danser_config.Gameplay.Score.Show = config.Gameplay.Score.Show
        danser_config.Gameplay.HpBar.Show = config.Gameplay.HpBar.Show
        danser_config.Gameplay.ComboCounter.Show = config.Gameplay.ComboCounter.Show
        danser_config.Gameplay.PPCounter.Show = config.Gameplay.PPCounter.Show
        danser_config.Gameplay.UseLazerPP = config.Gameplay.PPCounter.UseLazerPP
        danser_config.Gameplay.StrainGraph.Show = config.Gameplay.StrainGraph.Show
        danser_config.Gameplay.KeyOverlay.Show = config.Gameplay.KeyOverlay.Show
        danser_config.Gameplay.ScoreBoard.Show = config.Gameplay.ScoreBoard.Show
        danser_config.Gameplay.ScoreBoard.ShowAvatars = config.Gameplay.ScoreBoard.ShowAvatars
        danser_config.Gameplay.ScoreBoard.HideOthers = config.Gameplay.ScoreBoard.HideOthers
        danser_config.Gameplay.HitCounter.Show = config.Gameplay.HitCounter.Show
        danser_config.Gameplay.AimErrorMeter.Show = config.Gameplay.AimErrorMeter.Show
        danser_config.Gameplay.Boundaries.Enabled = config.Gameplay.Boundaries.Show
        danser_config.Gameplay.Mods.Show = config.Gameplay.Mods.Show
        danser_config.Gameplay.Mods.HideInReplays = config.Gameplay.Mods.HideInReplays
        danser_config.Gameplay.Mods.FoldInReplays = config.Gameplay.Mods.FoldInReplays
        danser_config.Gameplay.ShowResultsScreen = config.Gameplay.ResultsScreen.Show
        danser_config.Gameplay.ResultsScreenTime = config.Gameplay.ResultsScreen.Time
        danser_config.Gameplay.ResultsUseLocalTimeZone = config.Gameplay.ResultsScreen.UseLocalTimeZone

        # Input
        danser_config.Input.LeftKey = config.Input.LeftKey
        danser_config.Input.RightKey = config.Input.RightKey
        danser_config.Input.RestartKey = config.Input.RestartKey
        danser_config.Input.SmokeKey = config.Input.SmokeKey
        danser_config.Input.MouseButtonsDisabled = config.Input.MouseButtonsDisabled
        
        # Skin
        danser_config.Skin.CurrentSkin = config.Skin.CurrentSkin
        danser_config.Skin.Cursor.UseSkinCursor = config.Skin.UseSkinCursor
        danser_config.Skin.FallbackSkin = "default_fallback" if isfile(join(config.General.OsuSkinsDir, 'default_fallback', 'skin.ini')) else "default"
        danser_config.Skin.UseBeatmapColors = config.Skin.UseBeatmapColors
        danser_config.Skin.UseColorsFromSkin = config.Skin.UseBeatmapColors or config.Skin.UseSkinColors # double false will use danser colors?
        danser_config.Audio.IgnoreBeatmapSamples = config.Skin.UseSkinHitsounds

        # Cursor
        danser_config.Cursor.ScaleToCS = config.Cursor.ScaleToCS
        danser_config.Cursor.Colors.EnableRainbow = config.Cursor.CursorRainbow
        danser_config.Cursor.EnableTrailGlow = config.Cursor.CursorTrailGlow
        danser_config.Skin.Cursor.Scale = config.Cursor.CursorSize
        danser_config.Cursor.CursorRipples = config.Cursor.CursorRipples

        danser_config.Skin.Cursor.ForceLongTrail = config.Cursor.ForceLongTrail
        danser_config.Skin.Cursor.LongTrailDensity = config.Cursor.LongTrailDensity
        danser_config.Skin.Cursor.LongTrailLength = config.Cursor.LongTrailLength

        # Objects
        danser_config.Objects.DrawFollowPoints = config.Objects.DrawFollowPoints
        danser_config.Objects.DrawComboNumbers = config.Objects.DrawComboNumbers

        danser_config.Objects.ScaleToTheBeat = config.Objects.ScaleToTheBeat
        danser_config.Objects.Sliders.SliderMerge = config.Objects.SliderMerge

        if config.Objects.Rainbow:
            danser_config.Skin.UseBeatmapColors = False
            danser_config.Skin.UseColorsFromSkin = False
            danser_config.Objects.Colors.Color.EnableRainbow = True

        danser_config.Objects.Colors.Sliders.Border.Color.FlashToTheBeat = config.Objects.FlashToTheBeat
        danser_config.Objects.Colors.Sliders.Body.Color.FlashToTheBeat = config.Objects.FlashToTheBeat
        danser_config.Playfield.Background.FlashToTheBeat = config.Objects.FlashToTheBeat

        danser_config.Objects.Colors.Sliders.Body.UseHitCircleColor = config.Objects.UseHitCircleColor
        
        danser_config.Objects.Sliders.Snaking.In = config.Objects.SliderSnakingIn
        danser_config.Objects.Sliders.Snaking.Out = config.Objects.SliderSnakingOut
        
        # Playfield
        danser_config.Playfield.SeizureWarning.Enabled = config.Playfield.SeizureWarning
        danser_config.Playfield.Background.LoadStoryboards = config.Playfield.LoadStoryboard
        danser_config.Playfield.Background.LoadVideos = config.Playfield.LoadVideo

        danser_config.Playfield.Background.Dim.Intro = round(config.Playfield.IntroBGDim / 100, 2)
        danser_config.Playfield.Background.Dim.Normal = round(config.Playfield.InGameBGDim / 100, 2)
        danser_config.Playfield.Background.Dim.Breaks = round(config.Playfield.BreakBGDim / 100, 2)

        if config.Playfield.BGParallax:
            danser_config.Playfield.Background.Parallax.Amount = 0.1
        else:
            danser_config.Playfield.Background.Parallax.Amount = 0

        if config.Playfield.ShowDanserLogo:
            danser_config.Playfield.Logo.Dim.Intro = 0
        else:
            danser_config.Playfield.Logo.Dim.Intro = 1
        
        # OsuApi
        if config.General.OsuApi:
            with open(join(config.General.DanserRootDir, consts.danser_api_path), "w") as api:
                api.write(config.General.OsuApi)

@logged(logging.getLogger(__name__))
@traced
class DanserConfig(object):
    def __init__(self, config_path = ''):
        self.config_path = config_path if isfile(config_path) else join('danser-go', consts.danser_config_path)
        self.read()
    
    def read(self, config_path = ''):
        if not isfile(config_path):
            config_path = self.config_path
        self.config = Munch.fromDict(json.loads(decode_config_file(config_path)))
        logging.info(f"[DANSER][CONFIG] Danser Config is read from: {config_path}")

    def write(self, config_path = ''):
        if not isfile(config_path):
            config_path = self.config_path
        # logging.info(f"[DANSER][CONFIG] Danser Config is: {self.config.toDict()}")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(self.config.toDict(), f, ensure_ascii = False) # Skin name always contains unicode char.
        logging.info(f"[DANSER][CONFIG] Danser Config is written to: {config_path}")
