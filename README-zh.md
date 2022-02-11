<p align="center">
  <img width="500px" src="assets/danser-gui.png"/>
</p>

# Danser GUI

<h2 align="center"><a href="https://github.com/Wieku/danser-go">DANSER</a> 的一个图形界面配置与启动工具。
<hr>

[English](README.md)

## 如何安装 Danser GUI

1. 进入最新发布页面[这里](https://github.com/spaceskynet/danser-gui/releases/latest)
2. 根据您的系统架构下载正确的文件。
3. 将其提取并放在您想要的位置。
4. 在 Windows 中运行 `DanserGUI.exe` 或在 Linux 终端中运行 `./DanserGUI`。

阅读 [WIKI（未完成）](https://github.com/spaceskynet/danser-gui/wiki)了解更多信息。

## 需要注意的几点 ！！

1. 如果您还没有 danser，可以按照[此设置指南](https://github.com/Wieku/danser-go/wiki/Setup-Guide)进行安装！（只需进行步骤 1 和 2）。
2. 如果您想使用`录制模式`，请确保`ffmpeg`已安装或放入了 danser 文件夹。您可以在[这里](https://github.com/BtbN/FFmpeg-Builds/releases/)找到 ffmpeg，并且您可以按照[FFMPEG 安装指南](https://github.com/Wieku/danser-go/wiki/FFmpeg)来安装 ffmpeg。
3. 如果您已经有 osu! 本体，谱面数据库模式最好选择 `osu!` 模式，如果你只有 `Skins` 和 `Songs` 目录，请选择 `danser` 模式。
4. 如果要使用 osu! 默认皮肤作为备用皮肤，请下载 [default_fallback](https://github.com/spaceskynet/git-cloud/blob/master/osu!/Skins/default_fallback.osk) 皮肤并解压到你的 `Skins` 文件夹。
5. 该程序仍处于测试阶段，如果您想获得更多信息，可以使用 `-d` 或 `-debug` 标志进入 `debug` 模式。
6. 本程序只是配置了 danser 的部分常用设置，如果要编辑更多设置，请直接编辑 danser 的 json 配置文件。
7. `Knockout` 模式仍然在完善中。

## Credits

这个程序（Danser GUI）主要由 [@SpaceSkyNet](https://github.com/spaceskynet) 编写，许可为 [MIT License](https://github.com/spaceskynet/danser-gui/blob/master/LICENSE)。

**感谢这些项目：**

1. [danser-go](https://github.com/Wieku/danser-go)：osu!standard 地图的 CLI 可视化工具。
2. [osu-db-tools]( https://github.com/jaasonw/osu-db-tools)：用于操作 osu! 的 .db 数据库文件的脚本集合。
3. [osu-replay-to-map](https://github.com/spawn18/osu-replay-to-map)：一个用 Python 编写的基于回放创建谱面的程序。
4. [osr2mp4-app](https://github.com/uyitroa/osr2mp4-app)：将回放文件转换为视频的程序。
5. [ordr-client](https://github.com/MasterIO02/ordr-client) & [ordr-server](https://github.com/MasterIO02/ordr-server)：一个免费且易于使用的采用 danser 来渲染 osu! 回放并导出为视频的 API / [网站](https://ordr.issou.best/)。
