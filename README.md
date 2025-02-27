<h1 align="center">JetBrains Maple Mono</h1>
<h3 align="center">- JetBrains Mono + Maple Mono -</h3>
</br>

## 自我介绍
**JetBrains Maple Mono**: 一只基于 **Github Workflow (Bash)** 的 [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono) + [Maple Mono](https://github.com/subframe7536/maple-font) 合成字体

* 适用平台: Any

## 字形特征
* 高可读性，等宽无衬线，中英文 2:1 宽完美对齐
* 丰富字重，智能连字，Nerd Font，Hints 原生支持
* 实时更新，构建合成发布全流程自动化
* JetBrains Mono (英文字形) + Maple Mono (中文字形) 双字形
* 中英文字形由前后文自动选择，选择规则可参考 [Fusion JetBrainsMapleMono Glyph](https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/wiki/Fusion-JetBrainsMapleMono-Glyph)

![Font Showcase](https://github.com/user-attachments/assets/e3b061f2-1c81-4021-8d73-9ea9bb741084)

## 下载地址
1. **Github (latest): [https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/latest](https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/latest)**
2. Github (preview): [https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/tag/pre](https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono/releases/tag/pre)

## 下载哪个
发布文件按 **JetBrainsMapleMono-[NF/XX]-[NR/XX]-[HT/XX].zip** 的格式命名:

1. XX: 占位符，表示该字体没有增加这一特性
2. NF: Nerd Font，为部分开发工具、命令行终端、代码编辑器等提供图标支持 (会导致字体文件体积略微增大)
3. NR: CN Narrow，实验性功能，缩小中文字体间距 (会导致中英文不再 2:1 宽完美对齐)
4. HT: Hinted，使字体在低分辨率屏幕上 (<=1080P) 的渲染更加均匀 (可能会导致字体在高分辨率屏幕上的渲染略微模糊)

> 如果依然不清楚如何选择请下载 **JetBrainsMapleMono-XX-XX-XX.zip**

## 脚本流程
1. 每 5 - 15 分钟自动向上游 JetBrains Mono & Maple Mono 存储库**检查 Release 和 Commit 更新**
2. 如有更新则**构建、合成字体，并覆写元数据**
3. 如构建、合成成功则**将字体发布到 Github Release** (Release 发布为 latest，Commit 发布在 preview)

> 可手动选择跳过检查更新强制合成字体

## 实时监测
最近一次检查更新的时间:

* 北京时间: <!--BJT_TIME-->2025-02-28 04:47:20<!--BJT_TIME-->
* UTC 时间: <!--UTC_TIME-->2025-02-27 20:47:20<!--UTC_TIME-->

## 致谢名单
* **JetBrains Mono: 为本项目提供所有非中文字体设计**
* **Maple Mono: 为本项目提供所有中文字体设计**

## 开发者
**Space Time**

## 联系方式
**邮箱: Zeus6_6@163.com**

## 开源协议
[OFL-1.1](https://github.com/SpaceTimee/Fusion-JetBrainsMapleMono?tab=OFL-1.1-1-ov-file)

•ᴗ•
