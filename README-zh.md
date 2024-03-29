<p align="center">
  <img width="500px" src="assets/danser-gui.png"/>
</p>

# Danser GUI

<h2 align="center"><a href="https://github.com/Wieku/danser-go">DANSER</a> 的一个图形界面配置与启动工具。
<hr>

[English](README.md)

## DANSER 已经有了官方的 GUI 启动器，但对于中文用户，我暂时不推荐你去使用它

现在官方的启动器对于高 DPI 支持还不太好，同时对于 Unicode 字符暂时也没有支持（这意味着我们很多皮肤的名称它无法正常显示，因为皮肤的名称里普遍含有很多 Unicode 字符），暂时也不支持多语言，对于一般玩家来说体验不是很好。如果以后官方修复了这些问题，那么我会十分推荐你去使用它。对于轻度使用 Danser 导出回放的玩家，本项目足够了，但是注意本项目支持的 Danser 版本最高为 **0.6.9**，这也是我推荐大家使用的版本。

## 如何安装 Danser GUI

1. 进入最新发布页面[这里](https://github.com/spaceskynet/danser-gui/releases/latest)
2. 根据您的系统架构下载正确的文件。
3. 将其提取并放在您想要的位置。
4. 在 Windows 中运行 `DanserGUI.exe` 或在 Linux 终端中运行 `./DanserGUI`。
5. 更改配置然后点击 `Danser GUI` 的图标开始 `Danser` 之旅！

阅读 [WIKI（未完成）](https://github.com/spaceskynet/danser-gui/wiki)了解更多信息。

## 需要注意的几点 ！！

1. 如果您还没有 danser，可以按照[此设置指南](https://github.com/Wieku/danser-go/wiki/Setup-Guide)进行安装！（只需进行步骤 1 和 2）。
2. 如果您想使用`录制模式`，请确保`ffmpeg`已全局安装或放入了 danser 文件夹（或者放入了 danser 文件夹的 ffmpeg 文件夹下）。您可以在[这里](https://github.com/BtbN/FFmpeg-Builds/releases/)找到 ffmpeg，并且您可以按照[FFMPEG 安装指南](https://github.com/Wieku/danser-go/wiki/FFmpeg)来安装 ffmpeg。
3. 如果您已经有 osu! 本体，谱面数据库模式最好选择 `osu!` 模式，如果你只有 `Skins` 和 `Songs` 目录，请选择 `danser` 模式。
4. 如果要使用 osu! 默认皮肤作为备用皮肤，请下载 [default_fallback](https://github.com/spaceskynet/git-cloud/blob/master/osu!/Skins/default_fallback.osk) 皮肤并解压到你的 `Skins` 文件夹。
5. 该程序仍处于测试阶段，如果您想获得更多信息，可以使用 `-d` 或 `-debug` 标志进入 `debug` 模式。
6. 本程序只是配置了 danser 的部分常用设置，如果要编辑更多设置，请直接编辑 danser 的 json 配置文件。
7. `Knockout` 模式~~仍然在完善中~~差不多能用了。

## 界面预览

<details>
<summary>界面预览</summary>

![fig1](assets/fig1.png)

![fig2](assets/fig2.png)

![fig3](assets/fig3.png)

![fig4](assets/fig4.png)

![fig5](assets/fig5.png)

![fig6](assets/fig6.png)

![fig7](assets/fig7.png)

![fig8](assets/fig8.png)

![fig9](assets/fig9.png)

</details>

## Credits

这个程序（Danser GUI）主要由 [@SpaceSkyNet](https://github.com/spaceskynet) 编写，许可为 [MIT License](https://github.com/spaceskynet/danser-gui/blob/master/LICENSE)。如果您支持这个项目，您可以通过单击[此页面](https://github.com/spaceskynet/danser-gui/)右上角的星号给个star！

**感谢这些项目：**

1. [danser-go](https://github.com/Wieku/danser-go)：osu!standard 地图的 CLI 可视化工具。
2. [osu-db-tools](https://github.com/jaasonw/osu-db-tools)：用于操作 osu! 的 .db 数据库文件的脚本集合。
3. [osu-replay-parser](https://github.com/kszlim/osu-replay-parser)：一个用 Python 编写的库，用来解析 osu 回放文件（*.osr）。
4. [osr2mp4-app](https://github.com/uyitroa/osr2mp4-app)：将回放文件转换为视频的程序。
5. [ordr-client](https://github.com/MasterIO02/ordr-client) & [ordr-server](https://github.com/MasterIO02/ordr-server)：一个免费且易于使用的采用 danser 来渲染 osu! 回放并导出为视频的 API / [网站](https://ordr.issou.best/)。
